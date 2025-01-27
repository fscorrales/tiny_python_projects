#!/usr/bin/env python3
"""
Author : Fernando Corrales <fscpython@gmail.com>
Date   : 26-Jan-2025
Purpose: Write a Python program called apples.py tha takes some text,
given as a single positional argument, and replaces all the vowels in
the text with the given -v or --vowel options (with the default being a)
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Apples and bananas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-v",
        "--vowel",
        help="The vowel to substitute",
        metavar="vowel",
        choices=list(
            "aeiou"
        ),  # Use “choices” to restrict the user to one of the listed vowels.
        type=str,
        default="a",
    )

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel

    for v in "aeiou":
        text = text.replace(v, vowel).replace(v.upper(), vowel.upper())

    print(text)


# --------------------------------------------------
if __name__ == "__main__":
    main()
