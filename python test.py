#T4Q1
#Create a function generateNumbers(num) that takes in a positive number as argument and returns a list of
#number from 0 to that number inclusive. Note: The function range(5) will return a list of number [0, 1, 2, 3, 4]. 

def generateNumber(num):
         return (list(range(num+1)))

#T4Q2
#Create a function generateNumbers(start, end) that takes in two numbers as arguments and returns a list of
#numbers starting from start to the end number (inclusive) specified in the arguments. Note: The function
#range(x, y) can takes in 2 arguments. For example, range(1, 5) will return a list of numbers [1,2,3,4]. 

def make_list(a,b,c):
	l = list()
	for x in range(a,b+1,c):
		l.append(x)
	return l


