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
import sys
import Player

RIFLE_RANGE = 4
RIFLE_INIT_DAMAGE = 10
AMMO_LIMIT = 6
AMMO_RECHARGE = 3
class Rifle(Weapon.Weapon):
	
	
	def __init__(self,owner):
		Weapon.Weapon.__init__(self,RIFLE_RANGE,RIFLE_INIT_DAMAGE,owner)
		self.ammo = AMMO_LIMIT
	def enhance(self):
		self.ammo = min(AMMO_LIMIT, self.ammo+AMMO_RECHARGE)
	def action(self,posx,posy):
		sys.stdout.write("You are using rifle attacking " + str(posx) + " " + str(posy) + ".\n")
		print "Type how many ammos you want to use."
		ammoToUse = int(input(""))
		if ammoToUse > self.ammo:
			print "You don't have that ammos."
			return
		if self.owner.pos.distance(posx,posy) <= self.range:
			player = self.owner.game.getPlayer(posx,posy)
			if player != None:
				if self.owner.race == player.race:
					print "You are the same race, cannot do that."
				else:
					player.decreaseHealth(self.effect * ammoToUse)
					self.ammo -= ammoToUse
		else:
			print "Out of reach."
	def getAmmo(self):
		return self.ammo