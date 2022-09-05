from pathlib import Path
from typing import Iterator, Any

from my.zsh import _parse_file

from ..line_normalizer import LineNormalizer


class Normalizer(LineNormalizer):
    @classmethod
    def parse_file(cls, path: Path) -> Iterator[Any]:
        for e in _parse_file(path):
            yield f"{e.dt.timestamp()} {e.duration} {e.command}"


if __name__ == "__main__":
    Normalizer.main()
