import json
from pathlib import Path
from typing import Iterator, Any


from shell import ShellNormalizer


class Normalizer(ShellNormalizer):
    @classmethod
    def parse_file(cls, path: Path) -> Iterator[Any]:
        # use timestamp from JSON blob to determine unique games
        json_blob = json.loads(path.read_text())
        for b in json_blob:
            # lichess/chess.com keys for time
            assert "createdAt" in b or "end_time" in b, f"missing end time key {b}"
            for key in ("createdAt", "end_time"):
                if key in b:
                    yield b[key]


if __name__ == "__main__":
    Normalizer.main()
