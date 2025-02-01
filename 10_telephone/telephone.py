#!/usr/bin/env python3
"""
Author : Fernando Corrales <fscpython@gmail.com>
Date   : 29-Jan-2025
Purpose:
    Round numbers
    Use the string module
    Modify strings and lists to introduce random mutations
"""

import argparse
import os
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Telephone",
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

    parser.add_argument(
        "-m",
        "--mutations",
        help="Percent mutations",
        metavar="mutations",
        type=float,
        default=0.1,
    )

    args = parser.parse_args()

    # mutations between 0 and 1
    if args.mutations < 0 or args.mutations > 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        with open(args.text) as file:
            args.text = file.read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    new_text = args.text

    # Get strings of all the letters and punctuation
    alpha = "".join(sorted(string.ascii_letters + string.punctuation))
    # Get the number of mutations
    num_mutations = round(len(args.text) * args.mutations)
    # Get the indexes
    indexes = random.sample(range(len(args.text)), num_mutations)
    # Make the mutations
    for i in indexes:
        # Use random.choice () to select a new_char from a string created
        # by replacing the current character (text[i]) in the alpha variable
        # with nothing. This ensures that the new character cannot be the
        # same as the one we are replacing.
        new_char = random.choice(alpha.replace(new_text[i], ""))
        new_text = new_text[:i] + new_char + new_text[i + 1 :]

    print(f'You said: "{args.text}"')
    print(f'I heard : "{new_text}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
