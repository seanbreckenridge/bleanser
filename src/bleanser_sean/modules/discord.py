"""
WARNING: This only takes messages into account, it does not check activity
since those change so often and seem to be included/removed randomly over time

If you want to keep all of your activity, would recommend just keeping all your
discord exports, but I'm willing to forgo some activity blobs to minimize size
for all of my messages

WARNING: this uses the hpi tempdir to unzip the discord exports,
which can be gigs on their own, so if your tmpdir is /tmp it may fill
up your /tmp device

I would recommend configuring HPI tempdir in your core config like mine:
https://github.com/seanbreckenridge/dotfiles/blob/2303661bf2e3c66ccdd67c7039f000b88b54fb68/.config/my/my/config/__init__.py#L123-L127

So you can optionally set a different tempdir, and then run this while setting a tmpdir in ~/.cache instead:
mkdir -p ~/.cache/tdir
HPI_TEMPDIR=~/.cache/tdir python3 -m bleanser_sean.modules.discord prune ~/data/discord/ --move ~/.cache/removed
"""

from pathlib import Path
from typing import Iterator, Any
from contextlib import contextmanager

from my.core.structure import match_structure
from my.discord.data_export import EXPECTED_DISCORD_STRUCTURE
from discord_data.parse import parse_messages

from bleanser.core.modules.extract import ExtractObjectsNormaliser


class Normaliser(ExtractObjectsNormaliser):
    @contextmanager
    def unpacked(self, path: Path, *, wdir: Path) -> Iterator[Path]:
        # match structure unzips the file if needed to /tmp
        with match_structure(path, expected=EXPECTED_DISCORD_STRUCTURE) as matches:
            assert len(matches) == 1, matches
            yield matches[0]

    def extract_objects(self, path: Path) -> Iterator[Any]:
        for msg in parse_messages(path / "messages"):
            if isinstance(msg, Exception):
                continue
            yield msg.message_id


if __name__ == "__main__":
    Normaliser.main()
