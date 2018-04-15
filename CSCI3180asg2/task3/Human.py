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
import Player
import sys
import Rifle

class Human(Player.Player):
	def __init__(self,posx,posy,index,game):
		Player.Player.__init__(self,80,2,posx,posy,index,game)
		self.myString = "H"+str(self.index)
		self.equipment = Rifle.Rifle(self)
	def teleport(self):
		Player.Player.teleport(self)
		self.equipment.enhance()
	def distance(self,posx,posy):
		return
	def askForMove(self):
		sys.stdout.write("You are a human (H"+str(self.index)+") using Rifle. (Range "
			+str(self.equipment.getRange())+", Ammo #: "+str(self.equipment.getAmmo())+
			", Damage per shot: "+str(self.equipment.getEffect() ))
		print ""
		Player.Player.askForMove(self)