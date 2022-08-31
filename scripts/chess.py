from typing import Iterator, Any, Dict


from line_normalizer import JsonLineNormalizer


class Normalizer(JsonLineNormalizer):
    @classmethod
    def handle_json(cls, data: Dict[Any, Any]) -> Iterator[Any]:
        for b in data:
            # lichess/chess.com keys for time
            assert "createdAt" in b or "end_time" in b, f"missing end time key {b}"
            for key in ("createdAt", "end_time"):
                if key in b:
                    yield b[key]


if __name__ == "__main__":
    Normalizer.main()
