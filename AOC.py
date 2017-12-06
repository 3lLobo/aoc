# AdventOfCode Day 7 - Florian Wolf


# Funtion to slip up the input in left side, operator and right side of the equation
def make_list(input):
	list = {}	
	for line in input:
		line.strip()
		left, right = line.split('->')
		list[right] = left.split()
	return list
	
# Function to find the value of the key using the eoperators
def inception(key,list,keys):
	try:
		return int(key)
	except TypeError:
	
	if key is not in keys:
		left = list(key)
		if len(left) == 1:
			solution = inception(left[0])
		else:
			if left[-2] == 'AND':
				solution = inception(left[0]) & inception(left[-1])
			if left[-2] == 'OR':
				solution = inception(left[0]) | inception(left[-1])
			if left[-2] == 'NOT':
				solution = 65535 inception(left[1])
			if left[-2] == 'LSHIFT':
				solution = inception(left[0]) << inception(left[-1])
			if left[-2] == 'RSHIFT':
				solution = inception(left[0]) >> inception(left[-1])
		keys [key] = solution
	return keys(key)
	
input = open('input.txt')
list = make_list(input)
keys = {}
a = inception('a',list,keys)	

print ('Answer to the quiz: a = ',a)
	
			
			
			
			
			