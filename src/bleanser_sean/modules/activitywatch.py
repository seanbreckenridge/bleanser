from pathlib import Path
from typing import Iterator, Any

from active_window.parse import parse_window_events

from ..line_normalizer import LineNormalizer


class Normalizer(LineNormalizer):
    @classmethod
    def parse_file(cls, path: Path) -> Iterator[Any]:
        for event in parse_window_events(path):
            yield int(event.timestamp.timestamp())


if __name__ == "__main__":
    Normalizer.main()
