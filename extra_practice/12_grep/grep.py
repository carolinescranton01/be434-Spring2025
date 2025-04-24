#!/usr/bin/env python3
"""
Author : Caroline Scranton <carolinescranton@arizona.edu
Date   : 2025-04-24
Purpose: Grep emulator
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Python grep"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('PATTERN',
                        metavar='PATTERN',
                        help='Search pattern')

    parser.add_argument('FILE',
                        metavar='FILE',
                        help='Input file(s)',
                        nargs='+')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case sensitive',
                        action='store_true',
                        default=False)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output',
                        metavar='OUTFILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)
    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    flags = re.IGNORECASE if args.insensitive else 0
    pattern = re.compile(args.PATTERN, flags)

    for file in args.FILE:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                if pattern.search(line):
                    if len(args.FILE) > 1:
                        args.outfile.write(f"{file}:{line}")
                    else:
                        args.outfile.write(line)


# --------------------------------------------------
if __name__ == '__main__':
    main()
