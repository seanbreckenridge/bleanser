Scripts in `scripts` are run manually, the `__main__` block imports from upstream [bleanser](https://github.com/karlicoss/bleanser)

## Modules

Since these are for my HPI modules, they require those to be installed, see my [HPI repo](https://github.com/seanbreckenridge/HPI#install)

- `zsh` and `bash`, using the format I use from HPI. See the top of the files [on the HPI repo](https://github.com/seanbreckenridge/HPI) for what those look like
- `ipython`, using the base `sqlite` normalizer
- `chess` (for `chess.com`/`lichess` dumps) using a custom JSON normalizer
- `discord` - **WARNING** see the top of [scripts/discord.py](scripts/discord.py) for how this works and some caveats

These are run while in this directory, so:

```bash
# install upstream bleanser
pip install git+https://github.com/karlicoss/bleanser

# clone/run stuff here
git clone https://github.com/seanbreckenridge/bleanser
python3 ./scripts/...
```

See [`bleanser-runall`](./bleanser-runall) for examples

`bin` includes some scripts that I add to my `$PATH` to make running bleanser scripts easier
