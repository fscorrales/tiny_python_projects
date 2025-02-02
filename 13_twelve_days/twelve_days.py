#!/usr/bin/env python3
"""
Author : Fernando Corrales <fscpython@gmail.com>
Date   : 01-feb-2025
Purpose:
    Create an algorithm to generate “The Twelve Days of Christmas” from any given
    day in the range 1–12
    Reverse a list
    Use the range() function
    Write text to a file or to STDOUT
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Twelve Days of Christmas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n",
        "--num",
        help="Number of days to sing",
        metavar="days",
        type=int,
        default=12,
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Outfile",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )

    args = parser.parse_args()

    if args.num not in range(1, 13):
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # Join the verses on two newlines
    # and print to args.outfile, which is
    # an open file handle, or sys.stdout.
    print("\n\n".join(map(verse, range(1, args.num + 1))), file=args.outfile)


# --------------------------------------------------
def verse(day):
    """Create a verse"""
    ordinal = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth",
    ]  # something here!

    gifts = [
        "A partridge in a pear tree.",
        "Two turtle doves,",
        "Three French hens,",
        "Four calling birds,",
        "Five gold rings,",
        "Six geese a laying,",
        "Seven swans a swimming,",
        "Eight maids a milking,",
        "Nine ladies dancing,",
        "Ten lords a leaping,",
        "Eleven pipers piping,",
        "Twelve drummers drumming,",
    ]

    # The lines of each verse
    # start off the same,
    # substituting in the ordinal
    # value of the given day.
    lines = [f"On the {ordinal[day - 1]} day of Christmas,", "My true love gave to me,"]

    # Use the list.extend() method to add the gifts, which are a slice from the
    # given day and then reversed().
    # Note that I cannot use the list.append() method. It’s easy to confuse it with the
    # list.extend() method, which takes another list as its argument, expands it, and
    # adds all of the individual elements to the original list. The list.append() method is
    # meant to add just one element to a list, so if you give it a list, it will tack that entire
    # list onto the end of the original list!
    lines.extend(reversed(gifts[:day]))

    if day > 1:
        # Change the last of the lines to
        # add “And ” to the beginning,
        # appended to the lowercased
        # version of the line.
        lines[-1] = "And " + lines[-1].lower()

    return "\n".join(lines)


# --------------------------------------------------
def test_verse():
    """Test verse"""
    assert verse(1) == "\n".join(
        [
            "On the first day of Christmas,",
            "My true love gave to me,",
            "A partridge in a pear tree.",
        ]
    )
    assert verse(2) == "\n".join(
        [
            "On the second day of Christmas,",
            "My true love gave to me,",
            "Two turtle doves,",
            "And a partridge in a pear tree.",
        ]
    )


# --------------------------------------------------
if __name__ == "__main__":
    main()
