from typing import Iterator, Any, Dict

from ..json_extract import JsonObjectNormaliser


class Normaliser(JsonObjectNormaliser):
    def handle_json(self, data: Dict[Any, Any]) -> Iterator[Any]:
        for b in data:
            yield b["listened_at"]


if __name__ == "__main__":
    Normaliser.main()
