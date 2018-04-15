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
import Weapon
import Player
import sys

AXE_RANGE = 1
AXE_INIY_DAMAGE = 40

class Axe(Weapon.Weapon):

	def __init__(self,owner):
		Weapon.Weapon.__init__(self,AXE_RANGE,AXE_INIY_DAMAGE,owner)
	def enhance(self):
		self.effect += 10
	def action(self,posx,posy):
		sys.stdout.write("You are using axe attacking " + str(posx) + " " + str(posy) + ".\n")
		if self.owner.pos.distance(posx,posy) <= self.range:
			player = self.owner.game.getPlayer(posx,posy)
			if player != None:
				player.decreaseHealth(self.effect)
		else:
			print "Out of reach."