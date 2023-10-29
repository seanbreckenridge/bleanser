import orjson
from pathlib import Path
from typing import Iterator, Any

from bleanser.core.modules.extract import ExtractObjectsNormaliser


class Normaliser(ExtractObjectsNormaliser):
    def extract_objects(self, file: Path) -> Iterator[Any]:
        data = orjson.loads(file.read_bytes())
        for b in data:
            # lichess/chess.com keys for time
            assert "createdAt" in b or "end_time" in b, f"missing end time key {b}"
            for key in ("createdAt", "end_time"):
                if key in b:
                    yield b[key]


if __name__ == "__main__":
    Normaliser.main()
