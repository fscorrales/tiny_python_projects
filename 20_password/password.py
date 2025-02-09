#!/usr/bin/env python3
"""
Author : Fernando Corrales <fscpython@gmail.com>
Date   : 09-feb-2025
Purpose:
    Take a list of one or more input files as positional arguments
    Use a regular expression to remove non-word characters
    Filter words by some minimum length requirement
    Use sets to create unique lists
    Generate a given number of passwords by combining some given number of
    randomly selected words
    Optionally encode text using a combination of algorithms we’ve previously
    written
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Password maker",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("FILE", metavar="FILE", nargs="+", help="Input file(s)")

    parser.add_argument(
        "-n",
        "--num",
        help="Number of passwords to generate",
        metavar="num_passwords",
        type=int,
        default=3,
    )

    parser.add_argument(
        "-w",
        "--num_words",
        help="Number of words to use for password",
        metavar="num_words",
        type=int,
        default=4,
    )

    parser.add_argument(
        "-m",
        "--min_word_len",
        help="Minimum word length",
        metavar="minimum",
        type=int,
        default=3,
    )

    parser.add_argument(
        "-x",
        "--max_word_len",
        help="Maximum word length",
        metavar="maximum",
        type=int,
        default=6,
    )

    parser.add_argument(
        "-s",
        "--seed",
        help="Random seed",
        metavar="seed",
        type=int,
        default=None,
    )

    parser.add_argument("-l", "--l33t", help="Obfuscate letters", action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()


# --------------------------------------------------
if __name__ == "__main__":
    main()
