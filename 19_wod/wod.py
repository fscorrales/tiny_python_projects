#!/usr/bin/env python3
"""
Author : Fernando Corrales <fscpython@gmail.com>
Date   : 08-feb-2025
Purpose:
    Parse delimited text files using the csv module
    Coerce text values to numbers
    Print tabular data using the tabulate module
    Handle missing and malformed data
"""

import argparse
import csv
import io
import random
import re
import sys
from pprint import pprint

# to look at the input file on the command line.
# More info in: https://csvkit.readthedocs.io/en/1.0.3/
# For example: csvlook --max-rows 3 inputs/exercises.csv
import csvkit

# to format the output table
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Create Workout Of (the) Day (WOD)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        help="CSV input file of exercises",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="inputs/exercises.csv",
    )

    parser.add_argument(
        "-s",
        "--seed",
        help="Random seed",
        metavar="seed",
        type=int,
        default=None,
    )

    parser.add_argument(
        "-n",
        "--num",
        help="Number of exercises",
        metavar="exercises",
        type=int,
        default=4,
    )

    parser.add_argument("-e", "--easy", help="Halve the reps", action="store_true")

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    random.seed(args.seed)
    exercises = read_csv(args.file)
    if not exercises:
        sys.exit(f'No usable data in --file "{args.file.name}"')

    num_exercises = len(exercises)
    if args.num > num_exercises:
        sys.exit(f'--num "{args.num}" > exercises "{num_exercises}"')

    wod = []
    # Randomly select the given number of exercises.
    for name, low, high in random.sample(exercises, k=args.num):
        reps = random.randint(low, high)
        if args.easy:
            reps = int(reps / 2)
        wod.append((name, reps))

    print(tabulate(wod, headers=("Exercise", "Reps")))


# --------------------------------------------------
def read_csv(fh):
    """Read the CSV input"""
    # Create a csv.DictReader() that will
    # create a dictionary for each record
    # in the file. It zips the headers in the
    # first line with the data values in the
    # subsequent lines. It uses the
    # delimiter to indicate the string value
    # for splitting the columns of text.
    reader = csv.DictReader(fh, delimiter=",")
    # records = list(reader)
    exercises = []
    for rec in reader:
        name, reps = rec["exercise"], rec["reps"]
        low, high = map(int, (reps.split("-")))
        exercises.append((name, low, high))
    return exercises
    # for row in csv.DictReader(fh, delimiter=","):
    # Use the dict.get() function to try toretrieve the values
    # for “exercise” and “reps.”
    #     name, reps = row.get("exercise"), row.get("reps")
    #     if name and reps:
    # Use a regex to look for one or more digits,
    # followed by a dash, followed by one or more
    # digits. Use capturing parentheses for the
    # digits so they can be extracted later.
    #         match = re.match("(\d+)-(\d+)", reps)
    #         if match:
    #             low, high = map(int, match.groups())
    #     exercises.append((name, low, high))
    # return exercises

    #     # Use fh.readline() to read only the first line of the file.
    #     headers = fh.readline().rstrip().split(",")
    #     records = []
    #     for line in fh:
    #         # Strip and split the line of text into a list of field
    #         # values. Use the zip() function to create a new list of
    #         # tuples containing each of the headers paired with
    #         # each of the values.
    #         rec = dict(zip(headers, line.rstrip().split(",")))
    #         records.append(rec)


# --------------------------------------------------
def test_read_csv():
    """Test read_csv"""
    # Use io.StringIO() to create a mock file handle to wrap
    # around a valid text that we might read from a file. The
    # \n represents the newlines that break each line in the
    # input data, and each line uses commas to separate the
    # fields.
    text = io.StringIO("exercise,reps\nBurpees,20-50\nSitups,40-100")
    assert read_csv(text) == [("Burpees", 20, 50), ("Situps", 40, 100)]


# --------------------------------------------------
if __name__ == "__main__":
    main()
