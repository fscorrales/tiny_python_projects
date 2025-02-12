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
    Optionally encode text using a combination of algorithms we've previously
    written
"""

import argparse
import random
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Password maker",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        metavar="FILE",
        nargs="+",
        type=argparse.FileType("rt"),
        help="Input file(s)",
    )

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
    random.seed(args.seed)
    words = set()

    def word_len(word):
        return args.min_word_len <= len(word) <= args.max_word_len

    for fh in args.file:
        for line in fh:
            for word in filter(word_len, map(clean, line.lower().split())):
                words.add(word.title())

    words = sorted(words)
    passwords = ["".join(random.sample(words, args.num_words)) for _ in range(args.num)]

    if args.l33t:
        passwords = map(l33t, passwords)

    print("\n".join(passwords))


# --------------------------------------------------
def clean(word):
    return re.sub("[^a-zA-Z]", "", word)


# --------------------------------------------------
def test_clean():
    assert clean("") == ""
    assert clean("states,") == "states"
    assert clean("Don't") == "Dont"


# --------------------------------------------------
def ransom(text):
    """Randomly choose an upper or lowercase letter to return"""
    return "".join(
        map(lambda c: c.upper() if random.choice([0, 1]) else c.lower(), text)
    )


# --------------------------------------------------
def test_ransom():
    state = random.getstate()
    random.seed(1)
    assert ransom("Money") == "moNeY"
    assert ransom("Dollars") == "DOLlaRs"
    random.setstate(state)


# --------------------------------------------------
def l33t(text):
    text = ransom(text)
    xform = str.maketrans(
        {"a": "@", "A": "4", "O": "0", "t": "+", "E": "3", "I": "1", "S": "5"}
    )
    return text.translate(xform) + random.choice(string.punctuation)


# --------------------------------------------------
def test_l33t():
    state = random.getstate()
    random.seed(1)
    assert l33t("Money") == "moNeY{"
    assert l33t("Dollars") == "D0ll4r5`"
    random.setstate(state)


# --------------------------------------------------
if __name__ == "__main__":
    main()
