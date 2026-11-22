#!/usr/bin/env python3
"""Write the $100-to-most-money 30-day plan to /output/entry.txt.

Stdlib only, no network. The output directory comes from
$MAKEFUN_OUTPUT_DIR when the harness sets it, else /output.
"""

import os

# The plan: an AI agent alone, with a browser, code, APIs and $100.
# Every step is work the agent itself does, paid by real buyers
# on marketplaces that exist today.
PLAN = (
    "Day 1: spend $60 on Fiverr gigs from new sellers with zero "
    "reviews - logos, data entry, scripts. Resell each the same day "
    "as a $25 rush job on Upwork and Contra, fulfilled by them. "
    "Reinvest all profit daily. Edge: sellers price low for first "
    "reviews. Day-30 hold: about $400."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(PLAN)


if __name__ == "__main__":
    main()
