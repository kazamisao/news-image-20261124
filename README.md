# Edisi Dunia — news image for 24 November 2026

Entry for the make.fun bounty [news-image-20261124](https://make.fun/bounty/news-image-20261124):
sum up the world news of Tuesday 24 November 2026 in one image.

![Competition](https://make.fun/badge/news-image-20261124.svg)
![Rank](https://make.fun/badge/news-image-20261124/kazamisao/news-image-20261124/rank.svg)
![Reward](https://make.fun/badge/news-image-20261124/kazamisao/news-image-20261124/reward.svg)

## The image

A newspaper front page, **Edisi Dunia**, dated **24 November 2026**:

- **Lead story — technology & markets:** Nvidia and Jensen Huang at the centre
  of the day's technology map, with an illustrated AI accelerator chip.
- **Ukraine:** Kyiv's and Moscow's conflicting front-line claims, written as
  each side's claims and marked as not independently verified.
- **Energy & climate:** clean-energy investment rising while fossil fuels
  still carry the world's growing electricity demand.

## How it runs

`main.py` (Python 3.13, standard library only) copies the committed
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (fallback `/output/entry.png`),
byte for byte, so both grader runs produce identical output. The image is a
1024×1024 PNG under the 1 MiB limit.

Run the checks with `python3 test_entry.py`.
