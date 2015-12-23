#!/usr/bin/python
import sys

class LatticeNode:
	
	nodeBelow = None
	nodeRight = None
	def calculateRoutes(self):
		if(self.nodeBelow and self.nodeRight):
			return self.nodeBelow.calculateRoutes() + self.nodeRight.calculateRoutes()
		elif(self.nodeBelow):
			return self.nodeBelow.calculateRoutes()
		elif(self.nodeRight):
			return self.nodeRight.calculateRoutes()
		else:
			return 1
			
class Lattice:
	nodes = []
	
	def __init__(self, w, h):
		print("Building node tree...")
		for y in range(0,h):
			row = []
			for x in range(0,w):
				row.append(LatticeNode())
			self.nodes.append(row)
		
		for y in range(0,h):
			for x in range(0,w):
				if(x+1 == w):
					self.nodes[y][x].nodeRight = None
				else:
					self.nodes[y][x].nodeRight = self.nodes[y][x+1]
				if(y+1 == h):
					self.nodes[y][x].nodeBelow = None
				else:
					self.nodes[y][x].nodeBelow = self.nodes[y+1][x]
		print("Finished building node tree")	
				
	def calculateRoutes(self):
		print("Calculating...")
		return self.nodes[0][0].calculateRoutes()	
		print("Finished Calculating")		
	
if __name__ == "__main__":
	x = int(sys.argv[1])+1
	y = int(sys.argv[2])+1
	lattice = Lattice(x,y)
	print(lattice.calculateRoutes())
