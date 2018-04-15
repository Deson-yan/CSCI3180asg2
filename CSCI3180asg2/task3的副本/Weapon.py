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
class Weapon(object):
	def __init__(self,range1,damage,owner):
		self.range = range1
		self.effect = damage
		self.owner = owner
	def action(self,posx,posy):
		return
	def enhance(self):
		return
	def getEffect(self):
		return self.effect
	def getRange(self):
		return self.range