"""Entry program for make.fun news-image-20261124.

The repository holds the finished front-page image (entry.png) beside this
program. The grader runs the program in a read-only, stdlib-only sandbox, so
all it does is copy that committed image to the output directory, byte for
byte, which keeps repeated runs identical.
"""

import os
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
CHUNK = 65536


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    with open(SOURCE, "rb") as src, open(target, "wb") as dst:
        while True:
            block = src.read(CHUNK)
            if not block:
                break
            dst.write(block)
    return 0


if __name__ == "__main__":
    sys.exit(main())
