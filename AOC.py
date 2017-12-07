# AdventOfCode Day 7 - Florian Wolf

class advent:
	# Initialize class by creating empty result list and spliting up the input
	def __init__(self,input):
		self.keys =  {}
		self.list = self.make_list(input)
		
	
	# Funtion to slip up the input in left side, operator and right side of the equation
	def make_list(self,input):
		input1 = input.readlines()

		list ={}
		for line in input1:
			(left, right) = line.split(' -> ')
			
			list[right.strip('\n')] = left.split()

		return list
		
	# Function to find the value of the key using the eoperators
	def inception(self,key):
		try:
			return int(key)
		except ValueError:
			pass
		
		if key not in self.keys:
			inception = self.inception
			left1 = self.list[key]
			if len(left1) == 1:
				solution = inception(left1[0])
			else:
				if left1[-2] == 'AND':
					solution = inception(left1[0]) & inception(left1[-1])
				if left1[-2] == 'OR':
					solution = inception(left1[0]) | inception(left1[-1])
				if left1[-2] == 'NOT':
					solution = 65535 - inception(left1[1])
				if left1[-2] == 'LSHIFT':
					solution = inception(left1[0]) << inception(left1[-1])
				if left1[-2] == 'RSHIFT':
					solution = inception(left1[0]) >> inception(left1[-1])
			self.keys[key] = solution
		return self.keys[key] 
	
input = open('input.txt')
aoc = advent(input)
a = aoc.inception('a')	

print ('Answer to the quiz: a = ',a)
	
			
			
			
			
			