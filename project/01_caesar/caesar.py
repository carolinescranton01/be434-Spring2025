#!/usr/bin/env python3
"""
Author : Caroline Scranton <carolinescranton@arizona.edu>
Date   : 2025-04-30
Purpose: Caeser shift
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Cesear shift',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--number',
                        help='A number to shift',
                        metavar='NUMBER',
                        type=int,
                        default=3)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        action='store_true')

    args = parser.parse_args()
    return args


# --------------------------------------------------
def encode(text, shift, decode):
    """ shift the sequence """
    results = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shift = shift % 26

    if decode:
        shift = -shift
    for char in text:
        if char.isalpha():
            letters = alphabet.index(char)
            shifted_letters = (letters + shift) % len(alphabet)
            shifted_char = alphabet[shifted_letters]
            results.append(shifted_char)
        else:
            results.append(char)
    return ''.join(results)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    message = args.file.read().rstrip().upper()
    shifted_message = encode(message, args.number, args.decode)

    if args.outfile:
        args.outfile.write(shifted_message + '\n')
    else:
        print(shifted_message)


# --------------------------------------------------
if __name__ == '__main__':
    main()
