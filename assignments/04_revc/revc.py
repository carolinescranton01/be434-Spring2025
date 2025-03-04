#!/usr/bin/env python3
"""
Author : Caroline Scranton <carolinescranton@arizona.edu>
Date   : 2025-02-18
Purpose: Print reverse complement of DNA
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add Your Purpose',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='DNA',
                        help='Input sequence or file')

    args = parser.parse_args()

    if os.path.isfile(args.DNA):
        args.DNA = open(args.DNA).read().rstrip()
    return args


# --------------------------------------------------
def main():
    """Print reverse complement to DNA sequence"""

    args = get_args()
    dna = args.DNA
    reverse_dna = dna[::-1]

    complementary_nucleotides = {
        'A': 'T', 'a': 't', 'C': 'G', 'c': 'g',
        'T': 'A', 't': 'a', 'G': 'C', 'g': 'c'
    }
    output = ''
    for char in reverse_dna:
        output += complementary_nucleotides.get(char, '')

    out_fh = open('output.txt', 'wt') if os.path.isfile(args.DNA) else sys.stdout
    out_fh.write(output + '\n')
    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
