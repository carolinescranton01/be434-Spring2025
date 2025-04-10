#!/usr/bin/env python3
"""
Author : Caroline Scranton <carolinescranton@arizona.edu
Date   : 2025-04-09
Purpose: Find conserved sequences
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    fh = args.FILE

    lines = [line.strip() for line in fh]

    for line in lines:
        print(line)

    max_length = max(len(line) for line in lines)

    output = []

    for position in range(max_length):
        chars_at_position = [line[position] for line in lines]

        if all(char == chars_at_position[0] for char in chars_at_position):
            output.append('|')
        else:
            output.append('X')

    output_string = ''.join(output)
    print(output_string)


# --------------------------------------------------
if __name__ == '__main__':
    main()
