#!/usr/bin/env python3
"""
Author : Fernando Corrales <fscpython@gmail.com>
Date   : 01-feb-2025
Purpose:
    Learn how to use the random module to figuratively “flip a coin” to decide
    between two choices
    Explore ways to generate new strings from an existing one, incorporating ran-
    dom decisions
    Study the similarities of for loops, list comprehensions, and the map() function
"""

import argparse
import os
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Ransom Note",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-s",
        "--seed",
        help="Random seed",
        metavar="seed",
        type=int,
        default=None,
    )

    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text) as file:
            args.text = file.read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    print("".join(map(choose, args.text)))
    # print("".join([choose(char) for char in args.text]))


# --------------------------------------------------
def choose(char):
    return char.upper() if random.choice([False, True]) else char.lower()


# --------------------------------------------------
def test_choose():
    # The state of the random module is global to the program.
    # Any change we make here could affect unknown parts of
    # the program, so we save our current state.
    state = random.getstate()
    # Set the random seed to a known
    # value. This is a global change to our
    # program. Any other calls to
    # functions from the random module
    # will be affected!
    random.seed(1)
    assert choose("a") == "a"
    assert choose("b") == "b"
    assert choose("c") == "C"
    assert choose("d") == "d"
    # Reset the global state to the original value.
    random.setstate(state)


# --------------------------------------------------
if __name__ == "__main__":
    main()
