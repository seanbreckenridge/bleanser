import json
from pathlib import Path
from typing import Iterator, Any, Dict
from bleanser.core.modules.extract import ExtractObjectsNormaliser


class JsonObjectNormaliser(ExtractObjectsNormaliser):
    def handle_json(self, data: Dict[Any, Any]) -> Iterator[Any]:
        raise NotImplementedError

    def extract_objects(self, path: Path) -> Iterator[Any]:
        data = json.loads(path.read_text())
        yield from self.handle_json(data)
