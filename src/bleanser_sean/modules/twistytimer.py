from pathlib import Path
from typing import Iterator, Any

from scramble_history.twistytimer import parse_file

from ..line_normalizer import LineNormalizer


class Normalizer(LineNormalizer):
    @classmethod
    def parse_file(cls, path: Path) -> Iterator[Any]:
        for solve in parse_file(path):
            yield int(solve.when.timestamp())


if __name__ == "__main__":
    Normalizer.main()
