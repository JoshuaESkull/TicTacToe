import sys

print(r"""
	  _______ _   _______      _______         
 |__   __(_) |__   __|    |__   __|        
    | |   _  ___| | __ _  ___| | ___   ___ 
    | |  | |/ __| |/ _` |/ __| |/ _ \ / _ \
    | |  | | (__| | (_| | (__| | (_) |  __/
    |_|  |_|\___|_|\__,_|\___|_|\___/ \___|
    """)

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

render_board(current_board)

# User input for moves #

while True:
	x_coord = int(input('What is your desired X co-ordinate?: '))
	y_coord = int(input('What is your desired Y co-ordinate?: '))
	assign_player = input('What is your token (X or O)?: ')
	current_board[x_coord][y_coord] = assign_player
	render_board(current_board)
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
		break
	if o1 == 3:
		print('O wins!')
		break
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
		break
	if o2 == 3:
		print('O wins!')
		break
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
		break
	if o3 == 3:
		print('O wins!')
		break
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
		break
	if o1 == 3:
		print('O wins!')
		break
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
		break
	if o2 == 3:
		print('O wins!')
		break
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
		break
	if o3 == 3:
		print('O wins!')
		break
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
		break
	if o1 == 3:
		print('O wins!')
		break
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
		break
	if o2 == 3:
		print('O wins!')
		break

# making a test change #
# another test change #