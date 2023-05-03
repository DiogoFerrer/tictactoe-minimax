from TicTacToe import *
from Player import *


game: TicTacToe = TicTacToe()

playerGoesFirst = True

# 'X' goes first, 'O' goes second.
player: Player = Player('X' if playerGoesFirst else 'O', game)
cpu: CPU = CPU('O' if playerGoesFirst else 'X', game)

turn: Player = player if playerGoesFirst else cpu

while not game.terminal(game.getState()):
    game.print()

    turn.play()
    turn = cpu if turn == player else player

game.print()
