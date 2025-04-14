#!/usr/bin/env python3
"""
Author : caroline scranton <carolinescranton@arizona.edu>
Date   : 2025-04-14
Purpose: Play tic tac toe
"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b', '--board',
                        metavar='str',
                        type=str,
                        help='The state of the board',
                        default='.' * 9)

    parser.add_argument('-p',
                        '--player',
                        help='Player',
                        metavar='str',
                        choices='XO',
                        type=str,
                        default=None)

    parser.add_argument('-c',
                        '--cell',
                        help='Cell 1-9',
                        metavar='int',
                        choices=range(1, 10),
                        type=int,
                        default=None)

    args = parser.parse_args()

    if any([args.player, args.cell]) and not all([args.player, args.cell]):
        parser.error('Must provide both --player and --cell')

    if not re.search('^[.XO]{9}$', args.board):
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')

    if args.player and args.cell and args.board[args.cell - 1] in 'XO':
        parser.error(f'--cell "{args.cell}" already taken')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    board = list(args.board)

    if args.player and args.cell:
        board[args.cell - 1] = args.player

    print(format_board(board))
    winner = find_winner(board)
    print(f'{winner} has won!'if winner else 'No winner.')


# --------------------------------------------------
def format_board(board):
    """format the board"""

    cells = [str(i) if c == '.' else c for i, c in enumerate(board, start=1)]
    bars = '-------------'
    cells_tmpl = '| {} | {} | {} |'
    return '\n'.join([
        bars,
        cells_tmpl.format(*cells[:3]), bars,
        cells_tmpl.format(*cells[3:6]), bars,
        cells_tmpl.format(*cells[6:]), bars
    ])


# --------------------------------------------------
def find_winner(board):
    """Return the winner"""

    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
               [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for player in ['X', 'O']:
        for i, j, k in winning:
            combo = [board[i], board[j], board[k]]
            if combo == [player, player, player]:
                return player


# --------------------------------------------------
if __name__ == '__main__':
    main()
