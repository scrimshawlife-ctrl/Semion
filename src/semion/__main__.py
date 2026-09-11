"""python -m semion classify '{...}'"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .classify import classify

VERSION = Path(__file__).resolve().parents[2].joinpath("VERSION").read_text().strip()


def main() -> None:
    parser = argparse.ArgumentParser(prog="semion")
    parser.add_argument("--version", action="version", version=VERSION)
    sub = parser.add_subparsers(dest="cmd")
    c = sub.add_parser("classify")
    c.add_argument("atom", help="JSON atom")
    args = parser.parse_args()
    if args.cmd == "classify":
        print(json.dumps(classify(json.loads(args.atom)), indent=2, sort_keys=True))
        return
    parser.print_help()


if __name__ == "__main__":
    main()
