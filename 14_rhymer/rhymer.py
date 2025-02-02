#!/usr/bin/env python3
"""
Author : Fernando Corrales <fscpython@gmail.com>
Date   : 02-feb-2025
Purpose:
    Learn to write and use regular expressions
    Use a guard with a list comprehension
    Explore the similarities of list compre-
    hension with a guard to the filter() function
    Entertain ideas of “truthiness” when evaluating Python types in a Boolean
    context
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="word", help="A word to rhyme")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args.word)


# --------------------------------------------------
def stemmer():
    """Return leading consonants (if any), and 'stem' of word"""
    pass


# --------------------------------------------------
if __name__ == "__main__":
    main()
