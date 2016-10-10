#T14Q1
#Write a function that returns 4 lists given a postive number.

def createLists(num): 
	return list(range(1,num+1)), list(range(num,0,-1)), \
               list(range(-num,0)), list(range(-1, -num-1,-1))

#T14Q2
#abs(x) Return the absolute value of a number or the magnitude of a complex
#number.

def diff(a, b):
	return abs(abs(a)-abs(b))

#T14Q3
#Write a function that returns a string of characters based on a
#list of ASCII codes.

def toString(alist):
    return "".join(chr(i) for i in alist)

#T14Q4
# Write a function that capitalizes the first character of each word.

def capitalize(phrase):
    return ' '.join([s[0].upper() + s[1:] for s in phrase.split(' ') if len(s)>0])
            
#T14Q6
#Write a function that returns minimum and maximum values of a list containing numbers in integer and string formats.

def mixedList(mlist):
    return min(map(int,mlist)),max(map(int,mlist))
    
#T14Q7
#Write a function that converts a decimal integer to both hexadecimal and octal format.

def dec2hexoct(x): 
    return hex(x),oct(x)

#T14Q8
#map(function, iterable, ...) Apply function to every item of iterable and return a list. 

def mapfn1(alist):
    return list(map(hex,  alist))

def mapfn2(alist):
    return list(map(lambda x:x%2,  alist))

def mapfn3(word):
   return list(map(lambda x:x.upper(), word))

#T14Q9
#Complete the code below so that the outputs are as shown in the examples above.

def lowercase(x):
    if str(x).isupper():
        return False
    else:
        return True

def fn1(word):
   return ''.join(filter(lowercase, word))

def fn2(word):
   return ''.join(filter(lambda x: x>=str('0') and x<=str('9'),  word)) 

#T14Q10
#Write a factorial function using the 'reduce' function

from functools import reduce
def factorial(num):
    start = 1
    return reduce(lambda x,y:x*y       ,range(1,num+1), start)

#T14Q16
#Write a function that checks if some or all of the items are true or false.
def checkItems(items):
    if all(items):
        return 'All are true.'
    elif any(items):
        return 'Some are true.'
    else:
        return 'All are false.'




























