#!/usr/bin/env python3
"""
Author : Fernando Corrales <fscpython@gmail.com>
Date   : 02-feb-2025
Purpose:
    Learn more about using regular expressions
    Use both re.match() and re.search() to find patterns anchored to the beginning
    of a string or anywhere in the string, respectively
    Learn how the $ symbol in a regex anchors a pattern to the end of a string
    Learn how to use re.split() to split a string
    Explore how to write a manual solution for finding two-syllable “-ing” words or
    the word “you”
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Southern fry text",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.text.splitlines():
        print("".join(map(fry, re.split(r"(\W+)", line.rstrip()))))


# --------------------------------------------------
def fry(word):
    # if word.lower() == "you":
    #     return word[0] + "'all"

    # if word.endswith("ing"):
    #     if any(map(lambda c: c.lower() in "aeiouy", word[:-3])):
    #         return word[:-1] + "'"
    #     else:
    #         return word

    # return word

    # Search for “ing” anchored to the end of
    # word. Use a capture group to remember
    # the part of the string before the “ing.”
    ing_word = re.search("(.+)ing$", word)
    # Search for “you” or “You” starting
    # from the beginning of word. Capture
    # the [yY] alternation in a group.
    you = re.match("([Yy])ou$", word)

    if ing_word:
        prefix = ing_word.group(1)
        if re.search("[aeiouy]", prefix, re.IGNORECASE):
            return prefix + "in'"
    elif you:
        return you.group(1) + "'all"

    return word


# --------------------------------------------------
def test_fry():
    assert fry("you") == "y'all"
    assert fry("You") == "Y'all"
    assert fry("fishing") == "fishin'"
    assert fry("Aching") == "Achin'"
    assert fry("swing") == "swing"


# --------------------------------------------------
if __name__ == "__main__":
    main()
