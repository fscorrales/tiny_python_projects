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
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ""))
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
