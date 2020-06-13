# Codewars Kata Link: https://www.codewars.com/kata/56882731514ec3ec3d000009/python

from itertools import chain

def who_is_winner(l):
    class Four():
        board = [x[:] for x in [[None] * 6] * 7]
        cols = [0] * 7
        winner = None
        def __init__(self, col, player):
            self.col = col; self.player = player
            Four.board[self.col][Four.cols[self.col]] = player
            Four.cols[self.col] += 1
            self.check_winner()
        def check_winner(self):
            def check(line):
                for a, b, c, d in zip(line, line[1:], line[2:], line[3:]):
                    if all([a, b, c, d]) and a == b == c == d: Four.winner = self.player
            rows = ([Four.board[k][row] for k in range(7)] for row in range(6))
            diagonals_a = ([Four.board[b + n][a + n] for n in range(4)] for a, b in ((u, v) for u in range(3) for v in range(4)))
            diagonals_b = ([Four.board[b + n][a - n] for n in range(4)] for a, b in ((u + 3, v) for u in range(3) for v in range(4)))
            for line in chain(Four.board, rows, diagonals_a, diagonals_b): check(line)
    for k in l:
        c, p = k.split('_')
        Four('ABCDEFG'.index(c), p)
        if Four.winner: return Four.winner
    else:
        return 'Draw'
