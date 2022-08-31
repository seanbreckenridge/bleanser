import re
import json
from pathlib import Path
from typing import Iterator, TextIO, Any, Dict
from contextlib import contextmanager

from bleanser.core.processor import BaseNormaliser


class LineNormalizer(BaseNormaliser):
    """
    Given a input path, the `parse_file` function returns something that
    can be converted to a string, to represent a unique 'snapshot' for this file

    those can then be compared to elliminate redundant backups
    """

    MULTIWAY = True
    PRUNE_DOMINATED = True

    # should probably override this to return a line from the history file
    # see zsh.py for an example
    @classmethod
    def parse_file(cls, path: Path) -> Iterator[Any]:
        for line in path.open():
            yield line

    @classmethod
    def emit_history_file(cls, path: Path, fo: TextIO) -> None:
        for ent in cls.parse_file(path):
            # remove newlines from stringified representation
            print(re.sub("\n", "", str(ent)), file=fo)

    @contextmanager
    def do_cleanup(self, path: Path, *, wdir: Path) -> Iterator[Path]:
        assert path.stat().st_size > 0, path

        with self.unpacked(path=path, wdir=wdir) as upath:
            pass
        del path

        source = upath.absolute().resolve()
        # name/location in tmpdir
        cleaned = wdir / Path(*source.parts[1:]) / (source.name + "-cleaned")
        cleaned.parent.mkdir(parents=True, exist_ok=True)

        with cleaned.open("w") as fo:
            self.__class__.emit_history_file(upath, fo)

        # this gives it a bit of a speedup
        from subprocess import check_call

        check_call(["sort", "-o", cleaned, cleaned])

        yield cleaned


class JsonLineNormalizer(LineNormalizer):
    """
    this finds duplicates by emitting unique IDs from a JSON file
    similar to above, just handles parsing the file as JSON
    """

    MULTIWAY = True
    PRUNE_DOMINATED = True

    @classmethod
    def handle_json(cls, data: Dict[Any, Any]) -> Iterator[Any]:
        raise NotImplementedError

    @classmethod
    def parse_file(cls, path: Path) -> Iterator[Any]:
        data = json.loads(path.read_text())
        yield from cls.handle_json(data)


if __name__ == "__main__":
    # if some file is just lines of commands, could also run this
    # does not have to be specifically bash/zsh
    LineNormalizer.main()
