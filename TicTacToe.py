from copy import deepcopy
from typing import List


class TicTacToe:
    def __init__(self):
        self._state = [[0 for _ in range(3)] for _ in range(3)]

    # Returns which player to move in state s
    def _player(self, s: List[List[int]]) -> int:
        x_count = 0
        o_count = 0

        for i in range(3):
            for j in range(3):
                if s[i][j] == 1:
                    x_count += 1
                elif s[i][j] == 2:
                    o_count += 1

        return 1 if x_count <= o_count else 2

    # Returns legal moves in state s
    def actions(self, s: List[List[int]]) -> List[List[int]]:
        actions: List[List[int]] = []

        for i in range(3):
            for j in range(3):
                if s[i][j] == 0:
                    actions.append([i, j])

        return actions

    # Returns state after action a taken in state s
    def result(self, s: List[List[int]], a: List[int]):
        new_state = deepcopy(s)
        new_state[a[0]][a[1]] = self._player(s)
        return new_state

    # Checks if player p has won in state s
    def _won(self, s: List[List[int]], p: int) -> bool:
        for i in range(3):
            # Horizontally
            if all([cell == p for cell in s[i]]):
                return True
            # Vertically
            if all([cell == p for cell in [s[j][i] for j in range(3)]]):
                return True

        # Main diagonal
        if all([cell == p for cell in [s[i][i] for i in range(3)]]):
            return True
        # Other diagonal
        if all([cell == p for cell in [s[2-i][i] for i in range(3)]]):
            return True

        return False

    # Checks if state s is a terminal state
    def terminal(self, s: List[List[int]]) -> bool:
        # All cells occupied
        if not any([cell == 0 for cell in [s[i][j] for j in range(3) for i in range(3)]]):
            return True

        return self._won(s, 1) or self._won(s, 2)

    # Final numerical value for terminal state s
    def utility(self, s: List[List[int]]) -> int:
        return 1 if self._won(s, 1) else -1 if self._won(s, 2) else 0

    def getState(self) -> List[List[int]]:
        return self._state

    def move(self, player: int, cell: List[int]):
        self._state[cell[0]][cell[1]] = player

    def print(self):
        print('\n\n\n')

        for i in range(3):
            print('|'.join(map(lambda x: ' ' if x ==
                  0 else 'X' if x == 1 else 'O', self._state[i])))

            if i < 2:
                print('-----')

        print('\n\n\n')
