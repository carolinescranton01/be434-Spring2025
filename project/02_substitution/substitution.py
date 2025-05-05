#!/usr/bin/env python3
"""
Author : Caroline Scranton <carolinescranton@arizona.edu>
Date   : 2025-05-01
Purpose: Substitution cipher
"""

import argparse
import random
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Substitution cipher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'))

    parser.add_argument('-s',
                        '--seed',
                        help='A random seed',
                        metavar='int',
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
                        action='store_true',
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def encode(text, shuffled, decode):
    """ encode the sequence"""
    results = []
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if decode:
        mapping = {shuffled[i]: alphabet[i] for i in range(len(alphabet))}
    else:
        mapping = {alphabet[i]: shuffled[i] for i in range(len(alphabet))}

    for char in text:
        if char.isalpha():
            results.append(mapping[char])
        else:
            results.append(char)

    return ''.join(results)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    random.seed(args.seed)

    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    shuffled = ''.join(random.sample(alphabet, len(alphabet)))

    text = args.file.read().rstrip().upper()
    decode = args.decode
    encoded_message = encode(text, shuffled, decode)

    print(f"{encoded_message}")


# --------------------------------------------------
if __name__ == '__main__':
    main()
