#
# CSCI3180 Principles of Programming Languages
#
# --- Declaration ---
#
# I declare that the assignment here submitted is original except for source
# material explicitly acknowledged. I also acknowledge that I am aware of
# University policy and regulations on honesty in academic work, and of the
# disciplinary guidelines and procedures applicable to breaches of such policy
# and regulations, as contained in the website
# http://www.cuhk.edu.hk/policy/academichonesty/ 
#
# Assignment 2
# Name : YAN Shen
# Student ID : 1155092213
# Email Addr : syan6@cse.cuhk.edu.hk 
#


import random

class Gomoku(object):
	def __init__(self):
		self.gameBoard = [[0,0,0,0,0,0,0,0,0],
		                  [0,0,0,0,0,0,0,0,0],
		                  [0,0,0,0,0,0,0,0,0],
		                  [0,0,0,0,0,0,0,0,0],
		                  [0,0,0,0,0,0,0,0,0],
		                  [0,0,0,0,0,0,0,0,0],
		                  [0,0,0,0,0,0,0,0,0],
		                  [0,0,0,0,0,0,0,0,0],
		                  [0,0,0,0,0,0,0,0,0]]
		self.player1 = Player('O',self.gameBoard)
		self.player2 = Player('X',self.gameBoard)
		self.turn = 'O'
	def createPlayer(self,symbol,playerNum):
		user_input = 0
		while user_input != 1 and user_input != 2:
			user_input = int(input("Your choice is: "))
			if user_input == 1:
				if playerNum == 1:
					print "Player O is Human."
				else:
					print "Player X is Computer."
				print ""
				return 1
			elif user_input == 2:
				if playerNum == 1:
					print "Player O is Human."
				else:
					print "Player X is Computer."
				print ""
				return 2
				
			else:
				print "invalid input!"
		
	def checkWin(self):
		for i in range(2,7):
			for j in range(2,7):
				a = self.gameBoard
				if a[i][j] != 0:
					if a[i-2][j-2] == a[i][j] and a[i-1][j-1] == a[i][j]:
						if a[i][j] == a[i+2][j+2] and a[i][j] == a[i+1][j+1]:
							return True
					if a[i+2][j-2] == a[i][j] and a[i+1][j-1] == a[i][j]:
						if a[i][j] == a[i-2][j+2] and a[i][j] == a[i-1][j+1]:
							return True
		for i in range(2,7):
			for j in range(9):
				a = self.gameBoard
				if a[i][j] != 0:
					if a[i-2][j] == a[i][j] and a[i-1][j] == a[i][j]:
						if a[i+2][j] == a[i][j] and a[i+1][j] == a[i][j]:
							return True
		for i in range(9):
			for j in range(2,7):
				a = self.gameBoard
				if a[i][j] != 0:
					if a[i][j-2] == a[i][j] and a[i][j-1] == a[i][j]:
						if a[i][j+2] == a[i][j] and a[i][j+1] == a[i][j]:
							return True
		return False
	def checkTie(self):
		for i in range(9):
			for j in range(9):
				if self.gameBoard[i][j] == 0:
					return False
		return True
	def startGame(self):
		print "Please choose player 1 (O):"
		print "1. Human"
		print "2. Computer Player"
		if self.createPlayer('O',1) == 1:
			self.player1 = Human('O',self.gameBoard)
		else:
			self.player1 = Computer('O',self.gameBoard)
		print "Please choose player 2 (X):"
		print "1. Human"
		print "2. Computer Player"
		if self.createPlayer('X',2) == 1:
			self.player2 = Human('X',self.gameBoard)
		else:
			self.player2 = Computer('X',self.gameBoard)
		
		self.printGameBoard()

		row = 0
		column = 0
		while True:
			if self.turn == 'O':
				row,column=self.player1.nextMove(self.gameBoard)
				self.gameBoard[row][column] = 1
			else:
				row,column=self.player2.nextMove(self.gameBoard)
				self.gameBoard[row][column] = 2
			self.printGameBoard()
			if self.checkWin():
				print "Player",self.turn,"win!"
				break
			if self.checkTie():
				print "The game draw!"
				break
			
			print ""
			if self.turn == 'O':
				self.turn = 'X'
			else:
				self.turn = 'O'
			
	def printGameBoard(self):
		print "  |",
		for i in range(9):
			print i+1,
			print "|",
		print ""	
		print "--------------------------------------"
		for i in range(9):
			print i+1,
			print "|",
			for j in range(9):
				if self.gameBoard[i][j] == 0:
					print " ",
				elif self.gameBoard[i][j] == 1:
					print "O",
				elif self.gameBoard[i][j] == 2:
					print "X",
				print "|",
			print ""
			print "--------------------------------------"
			
class Player(object):
	def __init__(self, symbol, gameboard):
		self.symbol = symbol
		self.gameboard = gameboard
	def nextMove(self,gameboard):
		return

class Human(Player):
	def nextMove(self,gameboard):
		self.gameboard = gameboard
		row = -1
		column = -1
		while True:
			if self.symbol == 'O':
				print "Player O's turn!"
			else:
				print "Player X's turn!"
			row,column = raw_input("Type the row and col to put the disc: ").split(' ')		
			row = int(row)
			column = int(column)
			if self.gameboard[row-1][column-1] == 0:
				break
			print "Invalid input!"
		return row-1,column-1

class Computer(Player):
	def nextMove(self,gameboard):
		self.gameboard = gameboard
		row = random.randint(0,8)
		column = random.randint(0,8)
		while self.gameboard[row][column] != 0:
			row = random.randint(0,8)
			column = random.randint(0,8)
		return row,column

game=Gomoku()
game.startGame()


