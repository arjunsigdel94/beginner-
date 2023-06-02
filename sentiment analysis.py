# board
# display the board
# alternate user 
# checking win
# check rows
# check column
# check diagonal
# if entire board full, no clear winner than draw
board = ['-','-','-',
         '-','-','-',
         '-','-','-']

def display_board():
	print('|' + board[0] + '|' + board[1] + '|' +  board[2] +'|' )
	print('|' + board[3] + '|' + board[4] + '|' +  board[5] +'|' )
	print('|' + board[6] + '|' + board[7] + '|' +  board[8] +'|' )

def check_state(matrix):
	for i in matrix:
		if i == '-':
			return True


def count_empty_position():
	empty_list = []
	k = 0
	for i in board:
		if board[i] == '-':
			empty_list[k] = i + 1
			k = k + 1
    
    return empty_list



def check_winner(board1):






def player1(table):
	display_board()
	print("player 1")
	print (f'empty places are: {count_empty_position(board)}')
	entry = input('make your choice')
	board[int(entry-1)] = 'x'
	if check_state(board





         