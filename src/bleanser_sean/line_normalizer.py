# TODO: migrate to ExtractObjectsNormaliser in all related modules
# where it makes sense to, and remove this file

import json
from pathlib import Path
from typing import Iterator, Any, Dict
from bleanser.core.modules.extract import ExtractObjectsNormaliser


class LineNormalizer(ExtractObjectsNormaliser):
    MULTIWAY = True
    PRUNE_DOMINATED = True

    # HACK: while im migrating to the new version, instance method
    # just calls the classmethod I used previously
    def extract_objects(self, path: Path) -> Iterator[Any]:
        yield from self.parse_file(path=path)

    @classmethod
    def parse_file(cls, path: Path) -> Iterator[Any]:
        raise NotImplementedError


class JsonLineNormalizer(LineNormalizer):
    @classmethod
    def handle_json(cls, data: Dict[Any, Any]) -> Iterator[Any]:
        raise NotImplementedError

    @classmethod
    def parse_file(cls, path: Path) -> Iterator[Any]:
        data = json.loads(path.read_text())
        yield from cls.handle_json(data)
