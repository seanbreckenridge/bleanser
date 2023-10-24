from typing import Any, Iterator
from pathlib import Path

from my.ipython import _parse_database
from ..line_normalizer import LineNormalizer


class Normaliser(LineNormalizer):
    @classmethod
    def parse_file(cls, path: Path) -> Iterator[Any]:
        items = list(_parse_database(str(path)))
        assert len(items) > 0, f"No history items in ipython database {path}"
        for h in items:
            yield f"{h.dt} {h.command}"


if __name__ == "__main__":
    Normaliser.main()
