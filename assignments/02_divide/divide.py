#!/usr/bin/env python3
"""
Author : Caroline Scranton <carolinescranton@arizona.edu>
Date   : 2025-02-05
Purpose: Divide two numbers
"""

import argparse
import sys

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Divide two numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('integer',
                        metavar="INT",
                        type=int,
                        help='Numbers to divide',
                        nargs=2)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    integer = args.integer
    integer_list = list(integer)
    numerator = integer_list[0]
    denominator = integer_list[1]
    if denominator == 0:
        print(
            "usage: divide.py [-h] INT INT divide.py: error:"
            "Cannot divide by zero, dum-dum!"
            )
        sys.exit(1)
    else:
        output = integer_list[0] / integer_list[1]
        print(f'{numerator} / {denominator} = {int(output)}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
