#!/usr/bin/env python3
"""
Author : Fernando Corrales <fscpython@gmail.com>
Date   : 19-Jan-2025
Purposes:
    Accept text input from the command line or from a file
    Print output either to the command line or to a file that needs to be created
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler (upper-cases input)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input string or file")

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output filename (default: )",
        metavar="str",
        type=str,
        default="",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    is_file = os.path.isfile(args.text)

    if is_file:
        with open(args.text) as file:
            args.text = file.read().rstrip()

    # My solution
    if args.outfile == "":
        print(args.text.upper())
    else:
        with open(args.outfile, "wt") as output:
            print(args.text.upper(), file=output)

    # Author solution
    # out_fh = open(args.outfile, "wt") if args.outfile else sys.stdout
    # out_fh.write(args.text.upper() + "\n")
    # out_fh.close()

    # STDOUT (standard output) is always available via the special
    # sys.stdout file handle, which is always open.
    # The print() function takes an optional file argument specifying where to put
    # the output. That argument must be an open file handle, such as sys.stdout
    # (the default) or the result of open().


# --------------------------------------------------
if __name__ == "__main__":
    main()
