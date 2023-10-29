from pathlib import Path
from typing import Iterator, Any

from my.bash import _parse_file

from bleanser.core.modules.extract import ExtractObjectsNormaliser


class Normaliser(ExtractObjectsNormaliser):
    def extract_objects(self, path: Path) -> Iterator[Any]:
        for e in _parse_file(path):
            yield f"{e.dt.timestamp()} {e.command}"


if __name__ == "__main__":
    Normaliser.main()
