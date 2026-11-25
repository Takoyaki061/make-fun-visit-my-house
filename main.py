#!/usr/bin/env python3
"""Write the invitation letter image to the grader's output directory.

The letter artwork (letter.png) was generated in the recorded build session
with PIL and bundled in this repository. This entrypoint only copies it to
the output file, using the standard library alone.
"""

import os
import shutil
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "letter.png"
MAX_BYTES = 1_048_576
MAX_SIDE = 1024


def png_dimensions(path: Path) -> tuple[int, int]:
    """Read width/height from a PNG header without any third-party code."""
    with path.open("rb") as f:
        header = f.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{path} is not a PNG file")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main() -> None:
    if not SOURCE.is_file():
        print(f"missing artwork: {SOURCE}", file=sys.stderr)
        raise SystemExit(1)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    width, height = png_dimensions(target)
    size = target.stat().st_size
    if size > MAX_BYTES or width > MAX_SIDE or height > MAX_SIDE:
        print(
            f"gate failed: {target} is {width}x{height}, {size} bytes",
            file=sys.stderr,
        )
        raise SystemExit(1)
    print(f"wrote {target} ({width}x{height}, {size} bytes)")


if __name__ == "__main__":
    main()
