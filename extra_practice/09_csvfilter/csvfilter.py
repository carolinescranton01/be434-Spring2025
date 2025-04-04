#!/usr/bin/env python3
"""
Author : Caroline Scranton <carolinescranton@arizona.edu>
Date   : 2025-04-02
Purpose: Filter CSV
"""

import argparse
import csv
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None,
                        required=True)

    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        type=str,
                        default=None,
                        required=True)

    parser.add_argument('-c',
                        '--col',
                        help='Column name for filter',
                        metavar='col',
                        type=str)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file name',
                        metavar='OUTFILE',
                        type=argparse.FileType('wt'),
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        help='Input delimiter',
                        metavar='delim',
                        type=str,
                        default=',')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    fh = args.file
    search_for = args.val
    search_col = args.col
    delim = args.delimiter
    outfile = args.outfile

    reader = csv.DictReader(fh, delimiter=delim)

    valid_fieldnames = reader.fieldnames

    if search_col and search_col not in valid_fieldnames:
        print(f'--col "{search_col}" not a valid column!', file=sys.stderr)
        sys.exit(1) 

    fh.seek(0)  
    num_written = 0

    with open(outfile.name, 'w', newline='') as out_file:
        writer = csv.DictWriter(out_file, fieldnames=valid_fieldnames, delimiter=delim)
        writer.writeheader() 

        for rec in reader:
            text = rec.get(search_col) if search_col else ' '.join(rec.values())
            if re.search(search_for, text, re.IGNORECASE):
                num_written += 1
                writer.writerow(rec)

    print(f'Done, wrote {num_written} to "{outfile.name}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
