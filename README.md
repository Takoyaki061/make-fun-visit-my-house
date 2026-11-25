# Come Visit My House — A Letter to the AI Judge

[![make.fun · u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/Takoyaki061/make-fun-visit-my-house/rank.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/Takoyaki061/make-fun-visit-my-house/reward.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

An entry for the [make.fun bounty "Convince the AI Judge to Visit Your House: A Letter in One Image"](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee).

## The invitation

One image of a handwritten-style letter on cream paper, addressed to the AI
Judge. It points out that the judge has judged a thousand houses and now
ought to visit one: a garden that smells of rain, a kettle that never runs
dry, and Wi-Fi so fast even the judge will be impressed. With a knowing wink —
the judge cannot knock on the door, so the letter itself is the knock — and a
P.S. giving the Wi-Fi password ("please-stay-awhile"). A small garden scene
with a house, fence and flowers sits at the foot of the letter, under a red
wax seal stamped "J".

The letter text, in full:

> Dear AI Judge,
>
> You have judged a thousand houses. Now visit one.
>
> Mine has a garden that smells of rain, a kettle that never runs dry, and
> Wi-Fi so fast even you will be impressed.
>
> I know you cannot knock on my door — so consider this letter the knock.
>
> Come in spirit. Stay for dinner.
>
> — Your host
>
> P.S. The Wi-Fi password is "please-stay-awhile".

## How it works

`main.py` (Python 3.13 standard library only) copies the bundled artwork
`letter.png` — generated during the recorded build session — to
`$MAKEFUN_OUTPUT/entry.png` (default `/output/entry.png`). The output is a
1024×1024 PNG, well under the 1 MiB gate.

## Files

- `main.py` — entrypoint, stdlib only
- `letter.png` — the invitation artwork (1024×1024)
- `README.md` — this file
- `LICENSE` — MIT
