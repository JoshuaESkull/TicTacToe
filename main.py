import sys
import numpy as np

# Creating the board #

new_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Current board status #

current_board = new_board

# Creating a render function that visually represents the board #

def render_board(current_board):
	print('    0     1     2')
	print('    --------------')
	print('0' ' | ', current_board[0][0], '   ', current_board[0][1], '   ', current_board[0][2], ' |')
	print('1' ' | ', current_board[1][0], '   ', current_board[1][1], '   ', current_board[1][2], ' |')
	print('2' ' | ', current_board[2][0], '   ', current_board[2][1], '   ', current_board[2][2], ' |')
	print('    ---------------')

render_board(current_board)

# User input for moves #

while True:
	x_coord = int(input('What is your desired X co-ordinate?: '))
	y_coord = int(input('What is your desired Y co-ordinate?: '))
	assign_player = input('What is your token (X or O)?: ')
	current_board[x_coord][y_coord] = assign_player
	render_board(current_board)

# Checking to see if a player has won #
# Needs to take in the current board state (post-move) and then return whether there is a current win #
# Execute this within the while True loop as a break-if statement #
