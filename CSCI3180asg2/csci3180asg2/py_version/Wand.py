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
import sys
import Player

class Wand(object):
	def __init__(self,owner):
		self.effect = 10
		self.range = 5
		self.owner = owner
	def enhance(self):
		self.effect += 5
	def action(self,posx,posy):
		sys.stdout.write("You are using wand healing " + str(posx) + " " + str(posy) + ".\n")
		if self.owner.pos.distance(posx,posy) <= self.range:
			player = self.owner.game.getPlayer(posx,posy)
			if player != None:
				if self.owner.race != player.race:
					print "You are the different race, cannot do that."
				else:
					player.increaseHealth(self.effect)
		else:
			print "Out of reach."
	def getEffect(self):
		return self.effect
	def getRange(self):
		return self.range