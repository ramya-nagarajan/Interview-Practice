#!/usr/bin/python

class Node(object):

	#constructor that takes 
	def __init__(self,data):
			self.data = data
			self.next = None

	def getData(self):
		return self.data

	def setData(self,val):
		self.data = val

	def setNext(self,new_node):
		self.next_node = new_node



