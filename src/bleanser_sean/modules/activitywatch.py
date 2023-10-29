from pathlib import Path
from typing import Iterator, Any

from active_window.parse import parse_window_events

from bleanser.core.modules.extract import ExtractObjectsNormaliser


class Normaliser(ExtractObjectsNormaliser):
    def extract_objects(self, path: Path) -> Iterator[Any]:
        for event in parse_window_events(path):
            yield int(event.timestamp.timestamp())


if __name__ == "__main__":
    Normaliser.main()
