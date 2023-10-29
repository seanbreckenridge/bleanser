"""
Remove unneeded zip backups from saved MAL data:
https://github.com/seanbreckenridge/malexport/#recover_deleted
"""

from pathlib import Path
from typing import Iterator, Any
from contextlib import contextmanager

from my.core.structure import match_structure
from malexport.parse.recover_deleted_entries import (
    recover_deleted_single,
    EXPECTED_FILES,
    Approved,
)

from bleanser.core.modules.extract import ExtractObjectsNormaliser


class Normaliser(ExtractObjectsNormaliser):
    @contextmanager
    def unpacked(self, path: Path, *, wdir: Path) -> Iterator[Path]:
        # match structure unzips the file if needed to /tmp
        with match_structure(path, expected=EXPECTED_FILES, partial=True) as matches:
            yield matches[0]

    def extract_objects(self, path: Path) -> Iterator[Any]:
        anime, manga = recover_deleted_single(
            username="",
            approved=Approved.parse_from_git_dir(),
            from_backup_dir=path,
            filter_with_activity=False,
        )
        anime.sort(key=lambda x: x.id)
        manga.sort(key=lambda x: x.id)

        for an in anime:
            yield an.id
            for episode in an.history:
                yield an.id, str(episode.at), episode.number

        for mn in manga:
            yield mn.id
            for chapter in mn.history:
                yield mn.id, str(chapter.at), chapter.number


if __name__ == "__main__":
    Normaliser.main()
