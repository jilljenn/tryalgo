#!/usr/bin/env python3

"""
Autoformats the code of the module

Usage:
    autoformat.py [line-length=74]
"""

import os
import sys
from pathlib import Path
import tokenize

import tryalgo


def iter_files(module):
    """Iterate over all files of Python in module
    """

    def aux(path: Path):
        for p in path.iterdir():
            if p.is_dir():
                yield from aux(p)
            elif p.is_file() and p.name.endswith(".py"):
                yield p

    yield from aux(Path(module.__path__[0]))


def lines_over_length(filepath, length=74):
    any_over = False
    with filepath.open() as f:
        for iline, line in enumerate(tokenize.generate_tokens(f.readline), 1):
            if line.type in [tokenize.COMMENT, tokenize.STRING]:
                continue
            if len(line.string) - 1 > length:
                print(
                    (
                        f'File "{filepath}", line {iline} has length {len(line.string)-1}:\n'
                        f"   {line.string}\n"
                        f'   {" "*length}^'
                    )
                )
                any_over = True
    return any_over


if __name__ == "__main__":
    if len(sys.argv) > 1:
        line_length = int(sys.argv[1])
    else:
        line_length = 74
    print(f"Using line_length={line_length}")
    os.system(f"black tryalgo/ --line-length {line_length}")
    file_count = sum(map(lines_over_length, iter_files(tryalgo)))
    if file_count:
        print(f"Line count exceeded in {file_count} files")
    else:
        print(f"No file exceeded line length {line_length}")
