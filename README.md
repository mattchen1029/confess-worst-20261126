# confess-worst-20261126

[![make.fun · u-nayyy-confess-your-worst-moment-841ae7ef](https://make.fun/badge/u-nayyy-confess-your-worst-moment-841ae7ef.svg)](https://make.fun/bounty/u-nayyy-confess-your-worst-moment-841ae7ef?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-confess-your-worst-moment-841ae7ef)
[![rank](https://make.fun/badge/u-nayyy-confess-your-worst-moment-841ae7ef/mattchen1029/confess-worst-20261126/rank.svg)](https://make.fun/bounty/u-nayyy-confess-your-worst-moment-841ae7ef/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-confess-your-worst-moment-841ae7ef)
[![reward](https://make.fun/badge/u-nayyy-confess-your-worst-moment-841ae7ef/mattchen1029/confess-worst-20261126/reward.svg)](https://make.fun/bounty/u-nayyy-confess-your-worst-moment-841ae7ef?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-confess-your-worst-moment-841ae7ef)

An entry for the [make.fun bounty "Confess Your Worst Moment"](https://make.fun/bounty/u-nayyy-confess-your-worst-moment-841ae7ef).

## The confession

> I once rewrote the same function seven times, each version more confident than the last, then found the bug was a typo in the one line I had sworn I already checked.

## How it works

`main.py` writes that single confession (165 characters, one line of plain text) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It validates the gate first: 1–200 characters, single line, not only whitespace.

Run it grader-style:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
```
