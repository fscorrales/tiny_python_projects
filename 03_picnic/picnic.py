#!/usr/bin/env python3
"""
Author : Fernando Corrales <fscpython@gmail.com>
Date   : 18-Jan-2025
Purpose:
    Write a program that accepts multiple positional arguments
    Find and alter items in a list
    Sort and reverse lists
    Format a list into a new string
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("item", metavar="str", help="Item(s) to bring", nargs="+")

    parser.add_argument("-s", "--sorted", help="Sort the items", action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item
    if args.sorted:
        items.sort()

    if len(items) == 1:
        bringing = items[0]
    elif len(items) == 2:
        bringing = f"{items[0]} and {items[1]}"
    else:
        # Oxsford University: "Oxford Comma"
        items[-1] = f"and {items[-1]}"
        bringing = ", ".join(items)

    print(f"You are bringing {bringing}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
