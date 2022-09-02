from typing import Iterator, Any, Dict


from line_normalizer import JsonLineNormalizer


class Normalizer(JsonLineNormalizer):
    @classmethod
    def handle_json(cls, data: Dict[Any, Any]) -> Iterator[Any]:
        for b in data:
            yield b["listened_at"]


if __name__ == "__main__":
    Normalizer.main()
