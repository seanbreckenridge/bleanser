import re
import json
from pathlib import Path
from typing import Iterator, Any, Dict
from contextlib import contextmanager
from subprocess import check_call

from bleanser.core.processor import BaseNormaliser


def unique_tmpfile(path: Path, wdir: Path) -> Path:
    tmp_source_dir = path.absolute().resolve()
    # name/location in tmpdir
    fingerprint = (
        wdir / Path(*tmp_source_dir.parts[1:]) / (tmp_source_dir.name + "-fingerprint")
    )
    fingerprint.parent.mkdir(parents=True, exist_ok=True)
    return fingerprint


def sort_file(path: Path) -> None:
    # this gives it a bit of a speedup if all files are sorted
    check_call(["sort", "-o", path, path])


class LineNormalizer(BaseNormaliser):
    """
    Given a input path, the `parse_file` function returns something that
    can be converted to a string, to represent a unique 'snapshot' for this file

    those can then be compared to elliminate redundant backups
    """

    MULTIWAY = True
    PRUNE_DOMINATED = True

    @classmethod
    def parse_file(cls, path: Path) -> Iterator[Any]:
        """
        should probably override this to return a line from the history file
        see zsh.py for an example
        """
        for line in path.open():
            yield line

    @classmethod
    def emit_history(cls, unpacked_path: Path, cleaned_path: Path) -> None:
        """
        calls parse_file to extract lines from the unpacked path
        subclasses should probably override that to parse relevant data
        from the file and yield it back here
        """
        with open(cleaned_path, "w") as fo:
            for ent in cls.parse_file(unpacked_path):
                # remove newlines from stringified representation
                print(re.sub("\n", "", str(ent)), file=fo)

    @contextmanager
    def do_cleanup(self, path: Path, *, wdir: Path) -> Iterator[Path]:
        assert path.stat().st_size > 0, path

        # if this needs to be unpacked, do that
        with self.unpacked(path=path, wdir=wdir) as upath:
            del path

            # create a unique temporary file to write data to
            cleaned = unique_tmpfile(upath, wdir)
            # write to it, typically handled by a subclass
            self.__class__.emit_history(upath, cleaned)

            sort_file(cleaned)

        # at this point if unpacked temporarily extracted something,
        # it should be removed
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
