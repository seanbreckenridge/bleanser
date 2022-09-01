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
HPI_TEMPDIR=~/.cache/tdir python3 scripts/discord.py prune ~/data/discord/ --move ~/.cache/removed
"""

from pathlib import Path
from typing import Iterator
from contextlib import contextmanager

from my.core.structure import match_structure
from my.discord.data_export import EXPECTED_DISCORD_STRUCTURE
from discord_data.parse import parse_messages

from bleanser.core.processor import BaseNormaliser


class Normalizer(BaseNormaliser):
    MULTIWAY = True
    PRUNE_DOMINATED = True

    @contextmanager
    def unpacked(self, path: Path, *, wdir: Path) -> Iterator[Path]:
        # match structure unzips the file if needed to /tmp
        with match_structure(path, expected=EXPECTED_DISCORD_STRUCTURE) as matches:
            assert len(matches) == 1, matches
            yield matches[0]

    @contextmanager
    def do_cleanup(self, path: Path, *, wdir: Path) -> Iterator[Path]:
        assert path.stat().st_size > 0, path

        with self.unpacked(path=path, wdir=wdir) as upath:

            tmp_source_dir = upath.absolute().resolve()
            # name/location in tmpdir
            # to normalize this, just write msg IDs to the file,
            # one per line. If a file is a full subset of another, it can be removed
            fingerprint = (
                wdir
                / Path(*tmp_source_dir.parts[1:])
                / (tmp_source_dir.name + "-fingerprint")
            )
            fingerprint.parent.mkdir(parents=True, exist_ok=True)

            message_ids = [
                m.message_id for m in parse_messages(tmp_source_dir / "messages")
            ]
            message_ids.sort()

            with fingerprint.open("w") as fo:
                for m in message_ids:
                    print(f"message_{m}", file=fo)

            # this gives it a bit of a speedup
            from subprocess import check_call

            check_call(["sort", "-o", fingerprint, fingerprint])

        # yield outside unpacked contextmanager so unzipped structure is removed
        yield fingerprint


if __name__ == "__main__":
    Normalizer.main()
