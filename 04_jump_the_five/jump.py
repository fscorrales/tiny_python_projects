#!/usr/bin/env python3
"""
Author : Fernando Corrales <fscpython@gmail.com>
Date   : 18-Jan-2025
Purpose:
    Use a for loop and a list comprehension to process text, character by character
    Check if items exist in a dictionary
    Retrieve values from a dictionary
    Print a new string with the numbers substituted with their encoded values
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="str", help="Input text")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    jumper = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }

    # msg = ""
    # for char in args.text:
    #     msg += jumper.get(char, char)
    # print(msg)

    # Method 2: for loop
    for char in args.text:
        print(jumper.get(char, char), end="")

    # Method 3: list comprehension
    # print("".join([jumper.get(char, char) for char in args.text]))

    # Method 4: str.translate
    # print(args.text.translate(str.maketrans(jumper)))


# --------------------------------------------------
if __name__ == "__main__":
    main()
