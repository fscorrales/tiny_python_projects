#!/usr/bin/env python3
"""
Author : Fernando Corrales <fscpython@gmail.com>
Date   : 20-Jan-2025
Purpose:
    Accept one or more positional arguments that we’ll call letter.
    Accept an optional --file argument, which must be a readable text file. The
default value will be 'gashlycrumb.txt' (provided).
    Read the file, find the first letter of each line, and build a data structure that
associates the letter to the line of text. (We’ll only be using files where each line
starts with a single, unique letter. This program would fail with any other format
of text.)
    For each letter provided by the user, either print the line of text for the let-
ter if present, or print a message if it isn’t.
Learn how to “pretty-print” a data structure.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gashlycrumb",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("letter", metavar="letter", help="Letter(s)", nargs="+")

    parser.add_argument(
        "-f",
        "--file",
        help="Input file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="gashlycrumb.txt",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    lookup = {}
    for line in args.file:
        lookup[line[0].upper()] = line.rstrip()

    for letter in args.letter:
        if letter.upper() in lookup:
            print(lookup[letter.upper()])
        else:
            print(f'I do not know "{letter}".')


# --------------------------------------------------
if __name__ == "__main__":
    main()
