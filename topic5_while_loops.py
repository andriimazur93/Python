#T5Q1
#Create a function addNumbers(x) that takes a number as an argument and adds all the integers between 1
#and the number (inclusive) and returns the total number.

def addNumbers(num):
    total = 0
    i = 1
    while i<=num:
        total+=i
        i+=1
    return total

#T5Q2
#Create a function addNumbers(start, end) that adds all the integers between the start and end value (inclusive)
#and returns the total sum. 

def addNumbers(start, end):
    total = 0
    while start <= end :
        total += start
        start += 1
    return total

#T5Q4
#Create a function countPages(x) that takes the number of pages of a book as an argument and counts the number of
#times the digit '1' appears in the page number.

def countPages(num):
    total = 0
    i = 1
    while i<=num:
        page_no = str(i)
        total += page_no.count('1')
        i+=1 
    return total 

#T5Q5
#Create a function factorial(x) that takes an integer and returns the product of all the positive integers less than
#or equal to n. 

def factorial(num):
    product = 1
    i = 1
    while i <= num:
        product *=i
        i+=1
    return product 

#T5Q6
#Create a function doubleFactorial(n) that takes an odd integer and returns the product of all odd values up to the
#value n (where n=2k-1). 

def doubleFactorial(num):
    product = 1 
    i = 0
    k = 0 
    while k < num:
       k = 2*i+1
       product *= k 
       i += 1
    return product

#T5Q7
#Create a function that takes in a positive integer and return a list of prime numbers.
#A prime number is only divisible by 1 and itself. 

def primeNumbers(num):
    primes = []
    i = 2
    # iterates through range from 2 to num(inclusive)
    while i <= num     :     # add 'while' condition
        k = 2
        isPrime = True
        # check if prime number
        while k != i :      # add 'while' condition
            if i%k==0:
                isPrime = False
            k+=1            # update k
        if isPrime:
            primes.append(i)
        i+=1              # update i
    return primes

#T5Q9
#Create a function that takes in a positive number and return 2 integers such that the number is
#between the squares of the 2 integers. It returns the same integer twice if the number is a square
#of an integer.

from math import floor

def sqApprox(num):
    fnum = int(floor(num))
    i = 0
    while True:
        if i * i <= fnum:
            minsq = i
        if i * i >= num:
            maxsq = i
            break
        i = i + 1

    return minsq, maxsq

#T5Q10
#Create a function that computes the approximation of pi, based on the number of iterations specified. 

def piApprox(num):
    i = 1
    pi = 0
    k = 1
    while i <= num     :                # set 'while' termination condition
        if (i % 2 == 0):
            pi = pi - 1. / float(k)
        else:
            pi = pi + 1. / k
        k+=2                      # compute the ith term of the series
        i+=1                       # update i
    return 4.0*float(pi)

#T5Q11
#Write a function estimatePi() to estimate and return the value of pi based on the formula found
#by an Indian Mathematician Srinivasa Ramanujan. It should use a while loop to compute the terms
#of the summation until the last item is smaller than 1e -15.

def estimatePi():
        import math
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1) 
                    
        def series_term(k):
                a=factorial(4*k)
                b=(1103+26390*k)
                c=factorial(k)
                d=c**4
                e=396**(4*k)
                return float(a*b)/(d*e)
                
        k=0
        final=0
        while True:
            term = series_term(k)
            final += term
            if term < 1.0e-15:
                break
            else:
                k += 1
            f=2*math.sqrt(2)/9801        
            pi = 1.0/(final * f)
        return pi

#T5Q12
#Given a positive integer, write a function that computes the prime factors that can be multplied
#together to get back the same integer. 

def primeFactorization(num):
    result = []
    while(num != 1):
        for i in range(2, num):
            while(num % i == 0):
                result.append(i)
                num = num / i
                print(i)
                #i = 2
    return result

#T5Q13
#The smallest common multiple of two or more numbers is called the lowest common multiple (LCM).
#Given a list of integers, find the lowest common multiple. 

def LCM(nums):
    result = 1
    for i in nums:
        result *= i









    
