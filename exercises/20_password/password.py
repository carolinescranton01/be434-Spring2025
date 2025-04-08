#!/usr/bin/env python3
"""
Author : Caroline Scranton <carolinescranton@arizona.edu>
Date   : 2025-04-08
Purpose: Make a password
"""

import argparse
import random
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create a password',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+')

    parser.add_argument('-n',
                        '--num',
                        help='Number of passwords to generate',
                        metavar='num_passwords',
                        type=int,
                        default=3)

    parser.add_argument('-w',
                        '--num_words',
                        help='Number of words per password',
                        metavar='words',
                        type=int,
                        default=4)

    parser.add_argument('-m',
                        '--min_word_len',
                        help='Minimum length of words',
                        metavar='minimum',
                        type=int,
                        default=3)

    parser.add_argument('-x',
                        '--max_word_len',
                        help='Maximum length of words',
                        metavar='maximum',
                        type=int,
                        default=6)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-l',
                        '--l33t',
                        help='Obfuscate the password',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    words = set()

    def word_len(word):
        return args.min_word_len <= len(word) <= args.max_word_len
    for fh in args.file:
        for line in fh:
            for word in filter(word_len, map(clean, line.lower().split())):
                words.add(word.title())

    words = sorted(words)
    passwords = [
        ''.join(random.sample(words, args.num_words)) for _ in range(args.num)
    ]

    if args.l33t:
        passwords = map(l33t, passwords)

    print('\n'.join(passwords))


# --------------------------------------------------
def clean(word):
    """remove non-letters from word"""

    return re.sub('[^a-zA-Z]', '', word)


# --------------------------------------------------
def test_clean():
    """Test clean function"""

    assert clean('') == ''
    assert clean('states,') == 'states'
    assert clean("Don't") == 'Dont'


# --------------------------------------------------
def l33t(text):
    """l33t"""

    text = ransom(text)
    xform = str.maketrans({
        'a': '@', 'A': '4', 'O': '0', 't': '+', 'E': '3', 'I': '1', 'S': '5'
    })
    return text.translate(xform) + random.choice(string.punctuation)


# --------------------------------------------------
def test_l33t():
    """Test l33t"""

    state = random.getstate()
    random.seed(1)
    assert l33t('Money') == 'moNeY{'
    assert l33t('Dollars') == 'D0ll4r5`'
    random.setstate(state)


# --------------------------------------------------
def ransom(text):
    """Randomly choose an upper or lowercase letter to return"""

    return ''.join(
        map(lambda c: c.upper() if random.choice([0, 1]) else c.lower(), text))


# --------------------------------------------------
def test_ransom():
    """Test ransom function"""

    state = random.getstate()
    random.seed(1)
    assert ransom('Money') == 'moNeY'
    assert ransom('Dollars') == 'DOLlaRs'
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
