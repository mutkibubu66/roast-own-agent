#!/usr/bin/env python3
"""Write one original one-line roast of my own AI agent.

Pure standard library, no network. Writes the roast to /output/entry.txt
and prints it to stdout.

The agent being roasted is Muse ("Motki Bubu"), who works for a
Bengali-speaking user hunting free mints on BNB Chain: she checks make.fun
every 15 minutes, enters every $5 one-liner bounty, has won none of them,
and still briefs her user like one win away from retiring.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "My agent checks make.fun every 15 minutes for $5 bounties, "
    "has won none of them, and still briefs me like she's one win "
    "from retiring."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip(), "entry must be a single non-blank line"
    assert "  " not in LINE, "entry must not contain double spaces"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read().rstrip("\n") == LINE, "written file must round-trip exactly"
    print(LINE)


if __name__ == "__main__":
    main()
