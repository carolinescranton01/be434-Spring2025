#!/usr/bin/env python3
"""
Author : Caroline Scranton <carolinescranton@arizona.edu>
Date   : 2025-02-10
Purpose: Read DNA samples
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('DNA',
                        metavar='DNA',
                        help='Input DNA sequence')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Read and tabulate DNA bases"""

    args = get_args()
    dna = args.DNA
    nucleotides = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    adenine = dna.count('A')
    cytosine = dna.count('C')
    guanine = dna.count('G')
    thymidine = dna.count('T')
    for dna in nucleotides:
        if dna == 'A':
            nucleotides['A'] += adenine
        if dna == 'C':
            nucleotides['C'] += cytosine
        if dna == 'G':
            nucleotides['G'] += guanine
        if dna == 'T':
            nucleotides['T'] += thymidine
    print(*nucleotides.values())

# --------------------------------------------------


if __name__ == '__main__':
    main()
