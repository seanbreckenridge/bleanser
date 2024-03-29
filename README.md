## Modules

Since these are to clean up data for my HPI modules, they require those to be installed, see my [HPI repo](https://github.com/seanbreckenridge/HPI#install)

- `zsh` and `bash`, using the format I use from HPI. See the top of the files [on the HPI repo](https://github.com/seanbreckenridge/HPI) for what those look like
- `ipython` using my HPI module to parse dt/command
- `activitywatch` for android activitywatch JSON dumps using [active_window](https://github.com/seanbreckenridge/active_window/)
- `chess` (for `chess.com`/`lichess` dumps) using a custom JSON normaliser
- `discord` - **WARNING** see the top of [discord.py](src/bleanser_sean/modules/discord.py) for how this works and some caveats
- `trakt`, for [traktexport](https://github.com/seanbreckenridge/traktexport) dumps
- `listenbrainz`, for [listenbrainz](https://github.com/seanbreckenridge/listenbrainz_export)
- `mal_zips`: for [backup mal zips](https://github.com/seanbreckenridge/malexport/#recover_deleted)
- `smscalls`, for [karlicoss SMSCalls](https://github.com/karlicoss/HPI/blob/master/my/smscalls.py) module (uses [SMS Backup & Restore](https://play.google.com/store/apps/details?id=com.riteshsahu.SMSBackupRestore&hl=en_US)) -- requires you to prune each type (`calls` and `sms` individually)
- rubiks cube history `cstimer` - backups of my <https://cstimer.net> server data, saved whenever I open the page by [cstimer-save-server](https://github.com/seanbreckenridge/cstimer-save-server), twistytimer (phone app) backups using [scramble-history](https://github.com/seanbreckenridge/scramble-history)
- `grouvee` exports using [`grouvee_export`](https://github.com/seanbreckenridge/grouvee_export)

## Install

```bash
# install upstream bleanser
pip install git+https://github.com/karlicoss/bleanser

# clone/run stuff here
git clone https://github.com/seanbreckenridge/bleanser
pip install ./bleanser
python3 -m bleanser_sean.modules....
```

See [`bleanser-runall`](./bin/bleanser-runall) for examples, example [`bleanser-runall -n`](https://gist.github.com/seanbreckenridge/e97e4776181efcca2b19b0d7ffc1d0ed) (dry-run) output

`bin` includes some scripts that I add to my `$PATH` to make running bleanser scripts easier
