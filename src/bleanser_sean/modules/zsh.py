from pathlib import Path
from typing import Iterator, Any

from my.zsh import _parse_file

from bleanser.core.modules.extract import ExtractObjectsNormaliser


class Normaliser(ExtractObjectsNormaliser):
    def extract_objects(self, path: Path) -> Iterator[Any]:
        for e in _parse_file(path):
            yield f"{int(e.dt.timestamp())} {e.duration} {e.command}"


if __name__ == "__main__":
    Normaliser.main()
