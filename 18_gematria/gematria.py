#!/usr/bin/env python3
"""
Author : Fernando Corrales <fscpython@gmail.com>
Date   : 08-feb-2025
Purpose:
    Gematria is a system for assigning a number to a word by
    summing the numeric values of each of the characters
    (https://en.wikipedia.org/wiki/Gematria).
    Learn about the ord() and chr() functions
    Explore how characters are organized in the ASCII table
    Understand character ranges used in regular expressions
    Use the re.sub() function
    Learn how map() can be written without lambda
    Use the sum() function and see how that relates to using reduce()
    Learn how to perform case-insensitive string sorting
"""

import argparse
import os
import re
from functools import reduce


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gematria",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text) as file:
            args.text = file.read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for line in args.text.splitlines():
        print(" ".join(map(word2num, line.split())))


# --------------------------------------------------
def product(vals):
    # The reduce() function from the functools module
    # provides a generic way to reduce a list. This is
    # another higher-order function that wants another
    # function as the first argument
    return reduce(lambda x, y: x * y, vals)


# --------------------------------------------------
def word2num(word):
    """Sum the ordinal values of all the characters"""
    word = re.sub("[^A-Za-z0-9]", "", word)
    return str(sum(map(ord, word)))
    # return str(sum(map(ord, re.sub("[^A-Za-z0-9]", "", word))))


# --------------------------------------------------
def test_word2num():
    """Test word2num"""
    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c,") == "346"


# --------------------------------------------------
if __name__ == "__main__":
    main()
