from math import inf
from TicTacToe import *


class Player:
    def __init__(self, symbol: str, game: TicTacToe):
        self.symbol = 1 if symbol == 'X' else 2
        self.game = game

    # Prompt human player for their move
    def play(self):
        self.game.move(self.symbol, list(
            map(lambda x: int(x), input('i j: ').split())))


class CPU(Player):
    def play(self):
        self.game.move(self.symbol, self._minimax(self.game.getState()))

    def _minValue(self, s, prev):
        if self.game.terminal(s):
            return self.game.utility(s)

        v = inf
        for action in self.game.actions(s):
            v = min(v, self._maxValue(self.game.result(s, action), v))
            if v < prev:
                break

        return v

    def _maxValue(self, s, prev):
        if self.game.terminal(s):
            return self.game.utility(s)

        v = -inf
        for action in self.game.actions(s):
            v = max(v, self._minValue(self.game.result(s, action), v))
            if v > prev:
                break

        return v

    def _minimax(self, s):
        v = -inf if self.symbol == 1 else inf
        action = None

        for a in self.game.actions(s):
            value = self._maxValue(self.game.result(
                s, a), v) if self.symbol == 2 else self._minValue(self.game.result(s, a), v)
            if self.symbol == 1:
                if value > v:
                    v = value
                    action = a
            else:
                if value < v:
                    v = value
                    action = a

        return action
