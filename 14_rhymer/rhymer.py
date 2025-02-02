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
import re
import string as s


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
    prefixes = (
        list("bcdfghjklmnpqrstvwxyz")
        + (
            "bl br ch cl cr dr fl fr gl gr pl pr sc "
            "sh sk sl sm sn sp st sw th tr tw thw wh wr "
            "sch scr shr sph spl spr squ str thr"
        ).split()
    )

    start, rest = stemmer(args.word)
    if rest:
        print("\n".join(sorted([p + rest for p in prefixes if p != start])))
    else:
        print(f'Cannot rhyme "{args.word}"')


# --------------------------------------------------
def stemmer(word: str) -> tuple:
    """Return leading consonants (if any), and 'stem' of word"""
    consonants = "".join([c for c in s.ascii_lowercase if c not in "aeiou"])
    # We can put a '+' sign after the character class to say we want one or more
    # Moreover, to capture everything that comes after the consonants, we can use
    # a period (.) to match anything, and add a asterisk sign (*) to mean zero or more.
    # Finally,We can add a question mark (?) at the end of the consonants pattern
    # to make it optional
    word = word.lower()
    match = re.match(f"([{consonants}]+)?([aeiou])(.*)", word)
    if match:
        p1 = match.group(1) or ""
        p2 = match.group(2) or ""
        p3 = match.group(3) or ""
        return (p1, p2 + p3)
    else:
        return (word, "")


# --------------------------------------------------
def test_stemmer():
    """Test stemmer"""
    # always returns a 2-tuple of the (start, rest) of the word
    assert stemmer("") == ("", "")
    assert stemmer("cake") == ("c", "ake")
    assert stemmer("chair") == ("ch", "air")
    assert stemmer("APPLE") == ("", "apple")
    assert stemmer("RDNZL") == ("rdnzl", "")
    assert stemmer("123") == ("123", "")


# --------------------------------------------------
if __name__ == "__main__":
    main()
