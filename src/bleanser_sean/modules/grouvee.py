from pathlib import Path
from typing import Iterator, Any

from grouvee_export.dal import parse_export

from bleanser.core.modules.extract import ExtractObjectsNormaliser


class Normaliser(ExtractObjectsNormaliser):
    def extract_objects(self, path: Path) -> Iterator[Any]:
        for game in parse_export(path):
            yield game.grouvee_id


if __name__ == "__main__":
    Normaliser.main()
