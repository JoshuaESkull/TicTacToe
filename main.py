import sys
import numpy as np
import win_checking

# Creating the board #

new_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Current board status #

current_board = new_board

# Creating a render function that visually represents the board in the command line #

def render_board(current_board):
	print('    0     1     2')
	print('    --------------')
	print('0' ' | ', current_board[0][0], '   ', current_board[0][1], '   ', current_board[0][2], ' |')
	print('1' ' | ', current_board[1][0], '   ', current_board[1][1], '   ', current_board[1][2], ' |')
	print('2' ' | ', current_board[2][0], '   ', current_board[2][1], '   ', current_board[2][2], ' |')
	print('    ---------------')

# Defining functions that determine whether a player has won #

def horizontal_winner(current_board):
	# row one #
	x1 = 0
	o1 = 0
	for i in range(3):
		if current_board[0][i] == 'X':
			x1 += 1
		elif current_board[0][i] == 'O':
			o1 += 1
	if x1 == 3:
		print('X wins!')
	if o1 == 3:
		print('O wins!')
	# row two #
	x2 = 0
	o2 = 0
	for i in range(3):
		if current_board[1][i] == 'X':
			x2 += 1
		if current_board[1][i] == 'O':
			o2 += 1
	if x2 == 3:
		print('X wins!')
	if o2 == 3:
		print('O wins!')
	# row 3 #
	x3 = 0
	o3 = 0
	for i in range(3):
		if current_board[2][i] == 'X':
			x3 += 1
		if current_board[2][i] == 'O':
			o3 += 1
	if x3 == 3:
		print('X wins!')
	if o3 == 3:
		print('O wins!')

def vertical_winner(current_board):
	# column one #
	x1 = 0
	o1 = 0
	for i in range(3):
		if current_board[i][0] == 'X':
			x1 += 1
		elif current_board[i][0] == 'O':
			o1 += 1
	if x1 == 3:
		print('X wins!')
	if o1 == 3:
		print('O wins!')
	# row two #
	x2 = 0
	o2 = 0
	for i in range(3):
		if current_board[i][1] == 'X':
			x2 += 1
		if current_board[i][1] == 'O':
			o2 += 1
	if x2 == 3:
		print('X wins!')
	if o2 == 3:
		print('O wins!')
	# row 3 #
	x3 = 0
	o3 = 0
	for i in range(3):
		if current_board[i][2] == 'X':
			x3 += 1
		if current_board[i][2] == 'O':
			o3 += 1
	if x3 == 3:
		print('X wins!')
	if o3 == 3:
		print('O wins!')

def diagonal_winner(current_board):
	# diagonal 1 checking from (0,0) to (2,2)
	x1 = 0
	o1 = 0
	for i in range(3):
		if current_board[i][i] == 'X':
			x1 += 1
		if current_board[i][i] == 'O':
			o1 += 1
	if x1 == 3:
		print('X wins!')
	if o1 == 3:
		print('O wins!')
	# diagonal 2 checking from (0, 2) to (2, 0)
	x2 = 0
	o2 = 0
	for i in range(3):
		if current_board[i][-i+2] == 'X':
			x2 += 1
		if current_board[i][-i+2] == 'O':
			o2 += 1
	if x2 == 3:
		print('X wins!')
	if o2 == 3:
		print('O wins!')

render_board(current_board)

# User input for moves #

while True:
	x_wins = False
	o_wins = False
	x_coord = int(input('What is your desired X co-ordinate?: '))
	y_coord = int(input('What is your desired Y co-ordinate?: '))
	assign_player = input('What is your token (X or O)?: ')
	current_board[x_coord][y_coord] = assign_player
	render_board(current_board)
	horizontal_winner(current_board)
	vertical_winner(current_board)
	diagonal_winner(current_board)

