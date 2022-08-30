from pathlib import Path
from typing import Iterator, Any

from my.bash import _parse_file

from shell import ShellNormalizer


class Normalizer(ShellNormalizer):
    @classmethod
    def parse_file(cls, path: Path) -> Iterator[Any]:
        yield from _parse_file(path)


if __name__ == "__main__":
    Normalizer.main()
