import re
from pathlib import Path
from typing import Iterator
from contextlib import contextmanager

from my.zsh import _parse_file

from bleanser.core.processor import BaseNormaliser


class ZshNormalizer(BaseNormaliser):
    MULTIWAY = True
    PRUNE_DOMINATED = True

    @contextmanager
    def do_cleanup(self, path: Path, *, wdir: Path) -> Iterator[Path]:
        assert path.stat().st_size > 0, path

        with self.unpacked(path=path, wdir=wdir) as upath:
            pass
        del path

        zsh_hist = _parse_file(upath)

        source = upath.absolute().resolve()
        # name/location in tmpdir
        cleaned = wdir / Path(*source.parts[1:]) / (source.name + "-cleaned")
        cleaned.parent.mkdir(parents=True, exist_ok=True)

        with cleaned.open("w") as fo:
            for z in zsh_hist:
                # remove newlines from stringified representation
                zs = re.sub("\n", "", str(z))
                print(zs, file=fo)

        # this gives it a bit of a speedup
        from subprocess import check_call

        check_call(["sort", "-o", cleaned, cleaned])

        yield cleaned


if __name__ == "__main__":
    ZshNormalizer.main()
