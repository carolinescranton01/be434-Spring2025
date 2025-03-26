#!/usr/bin/env python3
"""
Author : Caroline Scranton <carolinescranton@arizona.edu>
Date   : 2025-03-25
Purpose: Find words in common
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('FILE2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        help='Input file 2')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def words(filehandle):
    """ get words """
    words = set()
    for line in filehandle:
        words.update(line.strip().split())
    return words


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    outfile = args.outfile
    with args.FILE1 as f1, args.FILE2 as f2:
        words1 = words(f1)
        words2 = words(f2)

    common = sorted(words1.intersection(words2))

    if args.outfile:
        with outfile as outfile:
            for word in common:
                print(word)
    else:
        for word in common:
            print(common)


# --------------------------------------------------
if __name__ == '__main__':
    main()
