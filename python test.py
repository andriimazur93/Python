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

#T4Q3
#Create a function generateNumbers(start, end, step) that takes in three numbers as arguments and returns a list
#of numbers ranging from start to the end number (inclusive)and skipping numbers based on the step specified in the
#arguments. Note: The function range(x, y, z) can takes in 3 arguments. For example, range(1, 11, 2) will return a
#list of numbers [1,3,5,7,9].

def generateNumber(a,b,c):
	l = list()
	if(c>0):
		for x in range(a,b+1,c):
			l.append(x)
	elif(c<0):
		for x in range(a,b-1,c):
			l.append(x)
	return l
#T4Q4
#Create a function addNumbers(num) that takes in a positive number as argument and returns the sum of all the number
#between 0 and that number (inclusive). 

def addNumbers(num):
	l = list()
	a=0
	for x in range(0, num+1):
		a+=x
	return a
    
#T4Q5
#Create a function addNumbers(start, end) that takes in two positive numbers as arguments and returns the sum
#of all the number between the start and end number (inclusive). 

def addNumbers (a,b):
    return sum(range(a,b+1))

#T4Q6
#Create a function addEvenNumbers(start, end) that takes in two positive numbers as arguments and returns the sum
#of all the even numbers between the start and end number (inclusive). Note: x % 2 returns 0 if x is an even number.

def addEvenNumbers (a,b):
    if(a<0 or b<0): return False
    summ=0
    for x in range(a,b+1):
        if x%2==0:
            summ+=x
    #return sum(i for i in range(a, b + 1) if i % 2 == 0)
    return summ

#T4Q7
#Making use of the 'continue' statement to skip the rest of execution within a loop block for current iteration, and
#move to the next iteration. 

def skipVowels(word):
    novowels = ''
    for ch in word:
        if ch.lower() in 'aeiou': 
        	continue
        	novowels += ch
        novowels+=ch
    return novowels

#T4Q8
#Making use of the 'break' statement to abort a for/while loop, and move to the code after the loop block . 

def stripComment(sentence):
    codeonly  = ""
    for ch in sentence:
        if ch == '#':
            break
            codeonly += '#'
        codeonly+=ch  
    return codeonly

#T4Q9 Create a function genSet() that takes in a list of numbers and returns a sorted set.

def genSet(nums):
    new = sorted(set(nums))
    return new

#T4Q11
#Write a function sumOfDigit(number) that takes in a number as argument and returns the sum of the individual
#digit in the number.

def sumOfDigit (number):
    return sum(int(digit) for digit in str(number))

