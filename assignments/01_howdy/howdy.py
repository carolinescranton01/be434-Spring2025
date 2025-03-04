#!/usr/bin/env python3
"""
Author : Caroline <carolinescranton@arizona.edu>
Date   : 2025-01-23
Purpose: Print a greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print greeting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n',
                        '--name',
                        help='Name to greet',
                        metavar='name',
                        type=str,
                        default='Stranger')

    parser.add_argument('-g',
                        '--greeting',
                        help='Greeting',
                        metavar='greeting',
                        type=str,
                        default='Howdy')

    parser.add_argument('-e',
                        '--excited',
                        help='Adds an exclamation point',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Greeting"""
    args = get_args()
    greeting = args.greeting + ', ' + args.name
    if args.excited:
        greeting += "!"
    else:
        greeting += "."

    print(greeting)

# --------------------------------------------------


if __name__ == '__main__':
    main()
