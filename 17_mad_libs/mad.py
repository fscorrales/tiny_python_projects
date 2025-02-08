#!/usr/bin/env python3
"""
Author : Fernando Corrales <fscpython@gmail.com>
Date   : 07-feb-2025
Purpose:
    Learn to use sys.exit() to halt your program and indicate an error status
    Learn about greedy matching with regular expressions
    Use re.findall() to find all matches for a regex
    Use re.sub() to replace found patterns with new text
    Explore ways to write the solution without using regular expressions
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Mad Libs",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        metavar="FILE",
        help="Input file",
        type=argparse.FileType("rt"),
    )

    parser.add_argument(
        "-i",
        "--inputs",
        help="Inputs (for testing)",
        metavar="input",
        type=str,
        nargs="*",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    inputs = args.inputs
    text = args.file.read().rstrip()
    blanks = re.findall("(<([^<>]+)>)", text)

    # Check if there are no placeholders.
    if not blanks:
        # You can call sys.exit() with a string value, in which case the string will be
        # printed to sys.stderr and the program will exit with the value 1
        sys.exit(f'"{args.file.name}" has no placeholders.')

    # Create a string template for the prompt
    # to ask for input() from the user.
    tmpl = "Give me {} {}: "
    for placeholder, pos in blanks:
        article = "an" if pos.lower()[0] in "aeiou" else "a"
        # If there are inputs, remove the first one for the answer;
        # otherwise, use input() to prompt the user for a value.
        answer = inputs.pop(0) if inputs else input(tmpl.format(article, pos))
        # Replace the current placeholder text with the answer from
        # the user. Use count=1 to ensure that only the first value is
        # replaced. Overwrite the existing value of text so that all the
        # placeholders will be replaced by the end of the loop.
        text = re.sub(placeholder, answer, text, count=1)

    print(text)


# --------------------------------------------------
if __name__ == "__main__":
    main()
