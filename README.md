[![make.fun · The Robot Apology](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/gunawanp-ux/robot-apology-20261126/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/gunawanp-ux/robot-apology-20261126/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)

# The Robot Apology

A tiny Python program (`main.py`) that writes a two-line robot confession
to `/output/entry.txt`, as required by the
[make.fun competition](https://make.fun/c/u-suga-the-robot-apology-dd96bb59):
one sentence apologizing for one specific mistake, and one sentence naming
the lesson learned and what the robot will do differently.

## The entry

> I am sorry: I watered the plastic fern every morning for six weeks while
> the real basil wilted beside it.
> I have learned to test for chlorophyll before committing to a schedule, so
> from now on I poke each leaf before I pour.

224 characters — well inside the competition's 1–400 character gate.

## Run

```sh
python3 main.py
```

It writes the entry to `/output/entry.txt` and verifies on disk that the
text is unchanged, within the 1–400 character gate, and exactly two lines
of one sentence each.
