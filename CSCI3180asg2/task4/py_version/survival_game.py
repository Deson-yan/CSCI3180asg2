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
import Human
import Chark
import Obstacle
import sys
import Wand

class SurvivalGame(object):
	def __init__(self):
		self.D = 10
		self.O = 2
		print "Welcome to Kafustrok. Light blesses you. \nInput number of players: (a even number)"
		self.n = int(input(""))
		self.teleportObjects = [0 for i in range(self.n+self.O)]
		for i in range(self.n/2):
			self.teleportObjects[i] = Human.Human(0,0,i,self)
			self.teleportObjects[i+self.n/2] = Chark.Chark(0,0,i,self)
		# last one get Wand
		self.teleportObjects[(self.n/2) - 1].equipment = Wand.Wand(self.teleportObjects[(self.n/2) - 1])
		self.teleportObjects[self.n - 1].equipment = Wand.Wand(self.teleportObjects[self.n - 1])
		for i in range(self.O):
			self.teleportObjects[i+self.n] = Obstacle.Obstacle(0,0,i,self)
	def printBoard(self):
		printObject=[[0 for x in range(self.D)] for y in range(self.D)]
		for i in range(self.D):
			for j in range(self.D):
				printObject[i][j] = "  "
		for i in range(self.n):
			pos = self.teleportObjects[i].getPos()
			printObject[pos.getX()][pos.getY()] = self.teleportObjects[i].getName()
		for i in range(self.n, self.n+self.O):
			pos = self.teleportObjects[i].getPos()
			printObject[pos.getX()][pos.getY()] = "O" + str(i-self.n)
       #priting
		print " ",
		for i in range(self.D):
			sys.stdout.write("| "+str(i)+"  ")
		print "|"
		for i in range(int(self.D*5.5)):
			sys.stdout.write("-")
		print ""
		for row in range(self.D):
			sys.stdout.write(str(row))
			for col in range(self.D):
				sys.stdout.write("| "+printObject[row][col]+" ")
			print "|"
			for i in range(int(self.D*5.5)):
				sys.stdout.write("-")
			print ""
	def positionOccupied(self,randx,randy):
		for i in range(self.n + self.O):
			pos = self.teleportObjects[i].getPos()
			if pos.getX() == randx and pos.getY() == randy:
				return True
		return False
	def getPlayer(self,randx,randy):
		for i in range(self.n+self.O):
			if isinstance(self.teleportObjects[i],Human.Human) or isinstance(self.teleportObjects[i],Chark.Chark):
				pos = self.teleportObjects[i].getPos()
				if pos.getX() == randx and pos.getY() == randy:
					return self.teleportObjects[i]
		return None
	def gameStart(self):
		turn = 0
		numOfAliveHuman = self.n/2
		numOfAliveChark = self.n/2
		while numOfAliveHuman > 0 and numOfAliveChark > 0:
			if turn == 0:
				for i in range(self.n + self.O):
					self.teleportObjects[i].teleport()
				print "Everything gets teleported.."
			self.printBoard()
			t = self.teleportObjects[turn]
			if t.health > 0:
				t.askForMove()
				print ""
				print ""
			turn = (turn + 1) % self.n
			numOfAliveHuman = 0
			numOfAliveChark = 0
			for i in range(self.n/2):
				if self.teleportObjects[i].health > 0:
					numOfAliveHuman += 1
				if self.teleportObjects[i+self.n/2] > 0:
					numOfAliveChark += 1
		print "Game over."
		self.printBoard()



game = SurvivalGame()
game.gameStart()