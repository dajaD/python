from random import randrange

board = [['1','2','3'],['4','X','6'],['7','8','9']]
#declares the board a three element list and every element has a three element list
#this is the default board
#because the board is concatednated,can only concatednate string to string not int to string



def DisplayBoard(board):
# The function accepts one parameter containing the board's current status
# and prints it out to the console.
#contains immutable and mutable variables.
# x will not update as that is the default the computer will always go first
	print("+-------+-------+-------+")
	print("|       |       |       |")
	print('|   '+board[0][0]+   '   |   '+   board[0][1]+    '   |   '+board[0][2]+'   |')
	print('|       |       |       |')
	print("+-------+-------+-------+")
        print("|       |       |       |")
        print('|   '+board[1][0]+   '   |   '+   board[1][1]+    '   |   '+board[1][2]+'   |')
        print('|       |       |       |')
      	print("+-------+-------+-------+")
        print("|       |       |       |")
        print('|   '+board[2][0]+   '   |   '+   board[2][1]+    '   |   '+board[2][2]+'   |')
        print('|       |       |       |')
        print("+-------+-------+-------+")


#user defined exception

class Errors(Exception):
#base class for future exceptions
    pass

class taken(Errors):
#raised when the user picks a square that is taken
    pass


def enterMove(board):
# The function accepts the board's current status, asks the user about their move,
# checks the input, and updates the board according to the user's decision.

	while True:
        	move = int(input('Enter your move by choosing a number in the range of squares (1-9) '))
		try:		
            		if int(move) < 1 or int(move) > 9:
#print("Please pick a square within the range!")
                    		raise ValueError
				continue
            		elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
#print("Please pick a square that is not take")
                        	raise taken
				continue
		        	
    			for row in range(0,3):
                        	for column in range(0,3):
                        		if board[row][column] == str(move):
                                		board[row][column] = 'O'
            		break
		except ValueError:
			print("Please pick a square within the range")
		except taken:
			print("Please pick a square that is not taken")

#this will be not as efficient. can become more efficent.
#            		if move == 1:
#                		board[0][0] = 'O'
#            		elif move == 2:
#                		board[0][1] = 'O'
#            		elif move == 3:
#                		board[0][2] = 'O'
#
#            		elif move == 4:
#                		board[1][0] = 'O'
#            		elif move == 6:
#                		board[1][2] = 'O'
#
#            		elif move == 7:
#                		board[2][0] = 'O'
#            		elif move == 8:
#                		board[2][1] = 'O'
#            		elif move == 9:
#                		board[2][2] = 'O'


#nested for loop will check every square to make sure its not taken.
#less lines of codes, and should be more efficient.
#changing freeSquares to a global variable to allow access from draw function.            

def makeListOfFreeValues(board):
	global freeSquares
	freeSquares = [] 
	#holds all the values
#everytime this is called, it will be an empty list. everytime user or cp makes a selection the list of free squares and the touples will change
#will hold all of values
	
#the same nested for loop from enter move, that iterates over all the squares in the board
# range(inclusive, exclusive) 
	for row in range (0,3):
		for column in range(0,3):
#checks to see if the square is taken
			if board[row][column] == 'X' or board[row][column] == 'O':
				pass
			else:
				freeSquares.append(([row],[column]))
#prints the touple of the remaining squares that are not taken				
	print(freeSquares)
 	

def winner(board, sign):
#there are 8 total possible ways to win the game.
#will manipulate the board
#pass sign in to check to see if cpu or user won
	if sign == 'O':
		print("Checking to see if you are the winner")
	else:
		print('checking to see if if the computer is the winner')	
#print('Checking to see if', sign, 'is a winner')
	
	if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
              return True
        elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
                return True
        elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
                return True
        elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
                return True
        elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
                return True
        elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
                return True
        elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
                return True
        elif board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
                return True
	else:
		print('There is not a winner yet!')



#will use the randrange() function
#will use a for loop to decide what row x column combo can be given to the cpu
#using the randrange(3) gives a random integer between 0-2
def draw(board):

#this loop will continue until it finds a row and column that is not already taken.
	while True:
		row = randrange(3)
		column = randrange(3)	
#checks touple list that was printed to verify whether or not its taken
		if([row],[column]) not in freeSquares:
			continue
#if the value is taken continue checking
#if the value is not taken changes the value for the square
		else:
			board[row][column] = 'X'
			return

board = [['1','2','3'],['4','X','6'],['7','8','9']]
numOfMoves = 1
users = 'O'
CPU = 'X'
#the back and forth between the user and cpu until there is an actual winner
print('Hello, this is tic tac toe!')
print('Current status of the game: ')
DisplayBoard(board)
print()

while numOfMoves < 9:
#counts the users turns each round

	enterMove(board)
	numOfMoves += 1
	DisplayBoard(board)

#checks for winner
	if winner(board, users) == True:
		print('You beat the computer! You are a super human!')
		break
	else:
		print('Here is the current list of free squares left on the board: ')
		makeListOfFreeValues(board)
		print()
		DisplayBoard(board)
#computer turn! cpu always goes after user as the first move (squaee 5) is the cpus first move technically
	print()
	print("Now it is the Computers turn")
	draw(board)
	numOfMoves += 1
	DisplayBoard(board)
	print()

	if winner(board, CPU) == True:
		print('Computer Wins!')
		break
	else:
		print('Here is the current list of free squares left on the board: ')
		makeListOfFreeValues(board)
		print()
		DisplayBoard(board)
else:
	print('We have a tie! It\'s a cat\'s game!!!')
print('Thanks for playing, play again!')
