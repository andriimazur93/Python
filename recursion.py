#T11Q1
#The factorial of a number N is simply the number multiplied by the factorialof (N-1).
#Complete the code given below to calculate and returns the factorial of a number.

def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

#T11Q2
#Write a recursive function power(x, y) to calculate the value of x raised to the
#power of y. 

def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x,y-1)

#T11Q3
#The Fibonacci numbers are the integer sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, ...,
#in which each item is formed by adding the previous two. 

def fibonacci(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1)+fibonacci(number-2)

#T11Q4
#The greatest common divisor (gcd) of 2 or more non-zero integers, is the largest
#positive integer that divides the numbers without a remainder. Write a function to
#compute the gcd of 2 integers using Euclid's algorithm:

def gcd(a, b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

#T11Q5
#A palindrome is a word, phrase, number or other sequence of units that can be read
#the same way in either direction. Write a recursive function that determines whether
#the given word is a palindrome. 

def isPalindrome(new_word):
    word = new_word.upper()
    if(len(word) <=1):
        return True
    if(word[0] == word[len(word)-1]):
        print(word)
        word = word[1:len(word)-1]
        return isPalindrome(word)
    else:
        return False

#T11Q6
#Write a recursive function sumOfDigits that takes in an integer and returns the
#sum of the digit in the integer. 

def sumdigits(number):
  if number == 0:
    return 0
  else:
    return (number%10) + sumdigits(number//10)
    
#T11Q7
#Write a recursive function countX that takes in a string and returns the number
#of uppercase character 'X' in the String. 

def countX(s):
    if len(s) < 1:
        return 0
    else:
        count = 0
        str = s
        if s[0] == 'X':
            count = 1          
            return count + countX(s[1:])
    return countX(s[1:])

#T11Q8
#Write a recursive function addDashes() that takes in a string and returns a new string
#with all the characters separated by a "-". 

def addDashes(s):
    if len(s) < 1:
        return None
    elif len(s) == 1:
        return s
    else:
        return s[0] + '-' + addDashes(s[1:])

#T11Q9
#Write a recursive function sumNumbersFromOne(number) that takes in a number and returns
#the sum of all the numbers from one to the number passed in as argument. 

def sumNumbersFromOne(number):
    if number < 1:
        return 'Invalid'
    if number == 1:
        return '%d'  %number
    else:
        return int(number) + int(sumNumbersFromOne(number-1))

#T11Q10
#Write a recursive function numbersInbetween(start, end) that takes in two numbers and
#returns a common-separated string with all the numbers in between the start and end number
#inclusive of both numbers. 

def numbersInbetween(a, b):
    if a>b:
        return "Invalid"
    if a == b:
        return '%d' %a
    else:
        return  '%s %s' % (a,numbersInbetween(a+1,b))

#T11Q11
#Write a function createStars(num) that takes in a number as argument and returns
#a string of stars 2num long. 

def createStars(x):
    if x == 0:
        return '*'
    else:
        return createStars(x-1) + createStars(x-1) 

#T11Q12
#Write a function createPattern(n) that takes in a number as argument and returns a
#string based on the following rules. The middle character of the string should always
#be an asterisk ('*'). There will be 2 asterisks if there is an even number of characters.
#The string will contain the less-than character ('<') before the asterisk and the
#greater-than character ('>') after the asterisk. 

def createPattern(x):
    if x == 0:
        return ''
    if x == 1:
        return '*'
    if x == 2:
        return '**'
    else:
        return '<' + createPattern(x-2) + '>'

#T11Q13
#Write a function printTwos(n) that takes in a number as argument and returns a string
#composed of an odd number multiplied by 2s such that the final value is equal to n. There
#should be equal number of 2s on both sides. Extra 2 should appear at the front of the
#string. Note: The value of the odd number can be 1. 

def printTwos(n): 
    if(n%2==1):return str(n)
    else:
        if(n%4==0):return str('2 * ')+ printTwos(n/4) +str(' * 2')
        else: return str('2 * ')+ printTwos(n/2)
        

#T11Q14
#The Pascal's Triangle is formed by filling the top 2 rows with '1's. For subsequent row,
#the numbers at the edge are all '1's. Each element inside the triangle is the sum of the
#2 elements above it. Write a recursive function to compute the value of each element
#given the row and column. 

def pascal(row, col):
    if(col == 0 or col == row):
        return 1
    else:
        return pascal(row-1,col-1) + pascal(row-1, col)

def time12hr(time):
    hours = int(time[0:2])
    minutes = int(time[2:])
    #print(minutes)
    #return True
    if(hours>12):
        return '%02d' %(hours-12) + ':' + '%02d' %(minutes)+' p.m.'
    return '%02d' %(hours+12) + ':' + '%02d' %(minutes)+ ' a.m.'

print(time12hr('1619'))


