#!/usr/bin/env python3
"""
Author : Caroline Scranton <carolinescranton@arizona.edu>
Date   : 2025-02-26
Purpose: Count GC content
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        nargs='*',
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Tabulate GC percentage"""

    args = get_args()
    if args.file:
        files = args.file
    else:
        files = sys.stdin

    highest_gc = 0.000000
    highest_gc_info = None

    for file in files:
        g_count, c_count = 0, 0
        seq_id = ''
        total_count = 0

        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if g_count + c_count > 0:
                    gc_percentage = ((g_count + c_count) / total_count) * 100
                    if gc_percentage > highest_gc:
                        highest_gc = gc_percentage
                        highest_gc_info = (seq_id, gc_percentage)

                seq_id = line[1:]
                g_count, c_count = 0, 0
                total_count = 0
            else:
                for char in line.strip():
                    if char == 'G':
                        g_count += 1
                    elif char == 'C':
                        c_count += 1
                total_count += len(line)

        if g_count + c_count > 0:
            gc_percentage = ((g_count + c_count) / total_count) * 100
            if gc_percentage > highest_gc:
                highest_gc = gc_percentage
                highest_gc_info = (seq_id, gc_percentage)

    seq_id, gc_percentage = highest_gc_info
    print(f'{seq_id} {gc_percentage:.6f}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
