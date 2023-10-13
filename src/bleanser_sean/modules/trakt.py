import orjson
from pathlib import Path
from typing import Iterator, Any

from bleanser.core.modules.extract import ExtractObjectsNormaliser


class Normalizer(ExtractObjectsNormaliser):
    def extract_objects(self, path: Path) -> Iterator[Any]:
        data = orjson.loads(path.read_bytes())
        for b in data["history"]:
            yield b["id"]


if __name__ == "__main__":
    Normalizer.main()
