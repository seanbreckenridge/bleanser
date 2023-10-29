from pathlib import Path
from typing import Iterator, Any

from scramble_history.cstimer import parse_file

from bleanser.core.modules.extract import ExtractObjectsNormaliser


class Normaliser(ExtractObjectsNormaliser):
    def extract_objects(self, path: Path) -> Iterator[Any]:
        for session in parse_file(path):
            for scramble in session.solves:
                yield int(scramble.when.timestamp())


if __name__ == "__main__":
    Normaliser.main()
