"""Light checks for the news-image-20261124 entry.

Runs main.py into a temporary output directory and verifies the copy is a
whole, in-limits PNG identical to the committed entry.png.
"""

import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_BYTES = 1048576
MAX_DIM = 1024


def png_size(path):
    with open(path, "rb") as fh:
        head = fh.read(24)
    assert head[:8] == b"\x89PNG\r\n\x1a\n", "not a PNG"
    width = int.from_bytes(head[16:20], "big")
    height = int.from_bytes(head[20:24], "big")
    return width, height


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
        proc = subprocess.run(
            [sys.executable, "-P", "-s", os.path.join(HERE, "main.py")],
            env=env, capture_output=True, text=True, timeout=60,
        )
        assert proc.returncode == 0, proc.stderr
        out = os.path.join(tmp, "entry.png")
        assert os.path.isfile(out), "entry.png not written"
        with open(os.path.join(HERE, "entry.png"), "rb") as fh:
            original = fh.read()
        with open(out, "rb") as fh:
            copied = fh.read()
        assert copied == original, "output bytes differ from committed image"
        assert len(copied) <= MAX_BYTES, "image over 1 MiB"
        width, height = png_size(out)
        assert width <= MAX_DIM and height <= MAX_DIM, "image over 1024x1024"
    print("test_entry: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
