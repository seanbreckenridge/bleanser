from pathlib import Path
from typing import Iterator, Any

from my.zsh import _parse_file

from line_normalizer import LineNormalizer


class Normalizer(LineNormalizer):
    @classmethod
    def parse_file(cls, path: Path) -> Iterator[Any]:
        yield from _parse_file(path)


if __name__ == "__main__":
    Normalizer.main()
