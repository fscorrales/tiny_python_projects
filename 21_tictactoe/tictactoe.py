#!/usr/bin/env python3
"""
Author : Fernando Corrales <fscpython@gmail.com>
Date   : 12-feb-2025
Purpose:
    Consider how to use elements like strings and lists to represent aspects of a program’s state
    Enforce the rules of a game in code, such as preventing a player from playing in
    a cell that has already been taken
    Use a regular expression to validate the initial board
    Use and and or to reduce combinations of Boolean values to a single value
    Use lists of lists to find a winning board
    Use the enumerate() function to iterate a list with the index and value
"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Tic-Tac-Toe",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("positional", metavar="str", help="A positional argument")

    parser.add_argument(
        "-b",
        "--board",
        help="The state of the board",
        metavar="str",
        type=str,
        default="." * 9,
    )

    parser.add_argument(
        "-p",
        "--player",
        help="Player",
        choices="XO",
        metavar="player",
        type=str,
        default=None,
    )

    parser.add_argument(
        "-c",
        "--cell",
        help="Cell 1-9",
        metavar="cell",
        type=int,
        choices=range(1, 10),
        default=None,
    )

    args = parser.parse_args()

    if len(args.board) != 9 or set(args.board) - set("XO."):
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')

    # # Use a regular expression to check that --board is comprised of exactly
    # # nine valid characters
    # if not re.search("^[.XO]{9}$", args.board):
    #     parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')

    # The combination of any() and all() is a way to test that both arguments
    # are present or neither is.
    if any([args.player, args.cell]) and not all([args.player, args.cell]):
        parser.error("Must provide both --player and --cell")

    if args.player not in "XO":
        parser.error(
            f"argument -p/--player: invalid choice: {args.player} (choose from 'X', 'O')"
        )

    if args.cell not in range(1, 10):
        parser.error(
            f"invalid choice: {args.cell} (choose from 1, 2, 3, 4, 5, 6, 7, 8, 9)"
        )

    # If both --player and --cell are present and valid, verify that the cell
    # in the board is not currently occupied.
    if args.player and args.cell and args.board[args.cell - 1] in "XO":
        parser.error(f'--cell "{args.cell}" already taken')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args.board)


# --------------------------------------------------
if __name__ == "__main__":
    main()
