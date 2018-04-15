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
import sys
import Pos
import Weapon

class Player(object):
	def __init__(self,healthCap,mob,posx,posy,index,game):
		self.MOBILITY = mob
		self.health = healthCap
		self.pos = Pos.Pos(posx,posy)
		self.index = index
		self.game = game
		self.myString = ""
		self.equipment = Weapon.Weapon(1,1,1)
		self.race = ""
	def getPos(self):
		return self.pos
	def teleport(self):
		randx = random.randint(0,self.game.D - 1)
		randy = random.randint(0,self.game.D - 1)
		while self.game.positionOccupied(randx,randy):
			randx = random.randint(0,self.game.D - 1)
			randy = random.randint(0,self.game.D - 1)
		self.pos.setPos(randx,randy)
	def increaseHealth(self,h):
		if self.race == "H":
			self.health = min(80,self.health + h)
		else:
			self.health = min(100,self.health + h)
		if self.health > 0:
			self.myString = self.race + str(self.index)
	def decreaseHealth(self,h):
		self.health = self.health - h
		if self.health <= 0:
			self.myString = "C" + self.race
	def getName(self):
		return self.myString
	def askForMove(self):
		sys.stdout.write("Your health is "+str(self.health)+". your position is ("+str(self.pos.getX())+","
			+str(self.pos.getY())+"). Your mobility is "+str(self.MOBILITY))
		print "."
		print "You now have following options: "
		print "1. Move"
		print "2. Attack/Heal"
		print "3. End tne turn"
		a = input("")
		a = int(a)
		if a == 1:
			print "Specify your target position (Input 'x y')."
			x,y = raw_input("").split(' ')
			x = int(x)
			y = int(y)
			if self.pos.distance(x,y) > self.MOBILITY:
				print "Beyond your reach. Staying still."
			elif self.game.positionOccupied(x,y):
				print "Position occupied. Cannot move there."
			else:
				self.pos.setPos(x,y)
				self.game.printBoard()
				print "You can now \n1.attack/heal\n2.End the turn"
				user_input = int(input(""))
				if user_input == 1:
					print "Input position to attack/heal. (Input 'x y')"
					attx,atty = raw_input("").split(' ')
					attx = int(attx)
					atty = int(atty)
					self.equipment.action(attx,atty)				
		elif a == 2:
			print "Input position to attack/heal."
			attx,atty = raw_input("").split(' ')
			attx = int(attx)
			atty = int(atty)
			self.equipment.action(attx,atty)
		elif a == 3:
			return

