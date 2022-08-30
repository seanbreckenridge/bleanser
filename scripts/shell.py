import re
from pathlib import Path
from typing import Iterator, TextIO, Any
from contextlib import contextmanager

from bleanser.core.processor import BaseNormaliser


class ShellNormalizer(BaseNormaliser):
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


if __name__ == "__main__":
    # if some file is just lines of commands, could also run this
    # does not have to be specifically bash/zsh
    ShellNormalizer.main()
