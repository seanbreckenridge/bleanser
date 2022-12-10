from pathlib import Path
from typing import Iterator, Any

from ..line_normalizer import LineNormalizer
from grouvee_export.dal import parse_export


class Normalizer(LineNormalizer):
    @classmethod
    def parse_file(cls, path: Path) -> Iterator[Any]:
        for game in parse_export(path):
            yield game.grouvee_id


if __name__ == "__main__":
    Normalizer.main()
