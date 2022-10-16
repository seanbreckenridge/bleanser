from pathlib import Path
from typing import Iterator, Any

from scramble_history.cstimer import parse_file

from ..line_normalizer import LineNormalizer


class Normalizer(LineNormalizer):
    @classmethod
    def parse_file(cls, path: Path) -> Iterator[Any]:
        for session in parse_file(path):
            for scramble in session.solves:
                yield int(scramble.when.timestamp())


if __name__ == "__main__":
    Normalizer.main()
