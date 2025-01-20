#!/usr/bin/env python3
"""
Author : Fernando Corrales <fscorrales@gmail.com>
Date   : 20-Jan-2025
Purpose:
    Learn how to process zero or more positional arguments
    Validate input files
    Read from files or from standard input
    Use multiple levels of for loops
    Break files into lines, words, and bytes
    Use counter variables
    Format string output
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Emulate wc (word count)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        metavar="FILE",
        help="Input file(s)",
        type=argparse.FileType(
            "rt"
        ),  # If arguments are provided, they must be readable text files. The files will be opened by argparse and will be provided as file handles
        nargs="*",  # ?Zero or one | *Zero or more | +One or more
        default=[
            sys.stdin
        ],  # The default will be a list containing sys.stdin, which is like an open file handle to STDIN. We do not need to open it.
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    total_lines, total_bytes, total_words = 0, 0, 0
    for fh in args.file:  # ONE LOOP!
        num_lines, num_words, num_bytes = 0, 0, 0
        for line in fh:  # TWO LOOPS!
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)
        total_lines += num_lines
        total_bytes += num_bytes
        total_words += num_words
        print(f"{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}")

    if len(args.file) > 1:
        print(f"{total_lines:8}{total_words:8}{total_bytes:8} total")


# --------------------------------------------------
if __name__ == "__main__":
    main()
