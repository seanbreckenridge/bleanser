## Modules

Since these are to clean up data for my HPI modules, they require those to be installed, see my [HPI repo](https://github.com/seanbreckenridge/HPI#install)

- `zsh` and `bash`, using the format I use from HPI. See the top of the files [on the HPI repo](https://github.com/seanbreckenridge/HPI) for what those look like
- `ipython`, using the base `sqlite` normalizer
- `chess` (for `chess.com`/`lichess` dumps) using a custom JSON normalizer
- `discord` - **WARNING** see the top of [discord.py](src/bleanser_sean/modules/discord.py) for how this works and some caveats
- `trakt`, for [traktexport](https://github.com/seanbreckenridge/traktexport) dumps
- `listenbrainz`, for [listenbrainz](https://github.com/seanbreckenridge/listenbrainz_export)

## Install

```bash
# install upstream bleanser
pip install git+https://github.com/karlicoss/bleanser

# clone/run stuff here
git clone https://github.com/seanbreckenridge/bleanser
pip install ./bleanser
python3 -m bleanser_sean.modules....
```

See [`bleanser-runall`](./bin/bleanser-runall) for examples

`bin` includes some scripts that I add to my `$PATH` to make running bleanser scripts easier
