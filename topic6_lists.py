#T6Q1
#A list behaves like a container, and it is able to contain more than one value. Create a list with the
#values as shown in the example below.

aList = ['Hello', 0, 20.0, 'World']

#T6Q2
#A list can be modified, and more elements can be added to an existing list. Use the append(x) function
#to add some more items to the list to produce the same content shown in the sample below.

aList = ['Hello', 0] 
aList.append(20.0)
aList.append('World')

#T6Q3
#A list can be modified, and elements can be removed from an existing list. Use the remove(x) function
#to remove some items from the list shown in the sample given below so that the list is left with the
#following content: ['hello', 'python','programming'].

aList = ['hello', 'i', 'love', 'python', 'programming']
aList.remove('i')
aList.remove('love')

#T6Q4
#Write a function addNumbersInList(numbers) to add all the numbers in a list. To access each element in
#a list, you can use the statement 'for num in numbers:'.

def addNumbersInList(numbers):
    return sum(i for i in numbers)

#T6Q5
#Write a function addOddNumbers(numbers) to add all the odd numbers in a list. To access each element in
#a list, you can use the statement 'for num in numbers:'. 

def addOddNumbers(numbers):
    return sum(i for i in numbers if i%2 == 1)

#T6Q6
#Write a function countOddNumbers(numbers) to count the number of odd numbers in a list.

def countOddNumbers(numbers):
    return (i for i in numbers if i%2 == 1)

#T6Q7
#Write a function getEvenNumbers(numbers) to return all the even numbers in a list. 

def getEvenNumbers(numbers): 
    new = []
    for i in numbers:
        even = i%2
        if(even == 0):
            new.append(i)
    return new

#T6Q8
#Write a function removeFirstAndLast(list) that takes in a list as an argument and remove the first and last
#elements from the list. The function will return a list with the remaining items. 

def removeFirstAndLast(numbers):
    new = list(numbers)
    new.pop(0)
    if not new:
        return new
    new.pop()
    return new

#T6Q9
#Write a function getMaxNumber(numbers) that returns the maximum number in a list. 

def getMaxNumber(numbers):
        if(numbers == []):
            return "N.A"
        a = list(numbers)
        return max(a)

#T6Q10
#Write a function getMinNumber(numbers) that returns the minimum number in a list. 

def getMinNumber(numbers): 
        if(numbers == []):
            return "N.A"
        a = list(numbers)
        return min(a)

#T6Q11
#Write a function that does matrix multiplication.
#The product of a mxn matrix with a nxp matrix results in a mxp matrix.
#A mxn matrix, with m rows and n columns, can be represented using nested lists.
#Am,n = [ [x11, x12, ..., x1n], ..., [xm1, ..., xmn] ] 

def MatrixProduct(m1, m2): 
    s=0     #sum
    t=[]    #temporary
    m3=[]   #final matrix
    if len(m2)!=len(m1[0]):
        print("Matrices cannot be multiplicated")        
    else:
        r1=len(m1)      #number of rows in the first matrix
        c1=len(m1[0])   #number of columns in the first matrix   
        r2=c1           #number of rows in the second matrix
        c2=len(m2[0])   #number of columns in the second matrix
        for z in range(0,r1):
            for j in range(0,c2):
                for i in range(0,c1):
                   s=s+m1[z][i]*m2[i][j]
                t.append(s)
                s=0
            m3.append(t)
            t=[]           
    return m3

#T6Q13
#A mxn matrix, m rows and n columns, can be represented using
#nested lists. Write a function that returns the diminensions of a matrix. 

def matrixDimensions(m):
    column_list = []
    a = len(m)              # number of rows
    b = len(m[0])           # number of columns in the first row
    for i in range(0, a):
        if(b != len(m[i])):
           return 'This is not a valid matrix.'
    return "This is a %dx%d matrix." % (a, b)

#T6Q16
#Write a function combine(la, lb) that takes in two lists and return
#a list with the contents of both list sorted in ascending order.

def combine(la, lb):
    result_list = []
    result_list.extend(la)
    result_list.extend(lb)
    result_list.sort()
    return result_list

#T6Q17
#The transpose of a matrix M, denoted MT, is formed by interchanging
#the rows and columns of M. That is, a mxn matrix is transformed into
#a nxm matrix.[MT]ij = [M]ji. Write a function that returns the
#transpose of a matrix. 

def transpose(matrix):
    return map(list, zip(*matrix))
    
#T6Q19
#Write a function calCumulativeSum(numbers) that takes in a list of
#numbers as argument and returns the cumulative sum of the list. That
#is, the new list where the i element is the sum of the first i + 1
#elements from the original list. For example, the cumulative sum of
#[1, 2, 3] is [1, 3, 6]. 

def calCumulativeSum(numbers):
    result_list = []
    i = 0
    while(i<=len(numbers)-1):
        result_list.append((sum(numbers[j] for j in range(0,i+1))))
        i+=1
    return result_list

#T6Q20
#Write a function combineList(list1, list2) that takes in two lists
#as arguments and return a list that combines all the elements in
#the two list. 

def combineList(list1, list2):
    res_list = []
    res_list.extend(list1)
    res_list.extend(list2)
    return res_list

#T6Q21
#Write a function (list1, list2) that takes in two lists as arguments
#and return a list that is the result of removing elements from list1
#that can be found in list2. 

def subtractList(list1, list2):
    new_list = []
    for i in (list1):
        if i not in list2:
           new_list.append(i)
    return new_list

#T6Q22
#Write a function countLetters(word) that takes in a word as argument
#and returns a list that counts the number of times each letter appears.
#The letters must be sorted in alphabetical order. 

##def countLetters(word):
##    from collections import Counter
##    return Counter(word)

def countLetters(word):
    letter = []
    cnt = []
    for c in sorted(word):
        if c not in letter:
            letter.append(c)
            cnt.append(1)
        else:
            cnt[-1] += 1
    return zip(letter, cnt)

#T6Q23
#Write a function getNumbers(number) that takes in a number as argument
#and return a list of numbers as shown in the samples given below
#>>> getNumbers(10)
#    [100, 64, 36, 16, 4, 0, 4, 16, 36, 64, 100]

def getNumbers(num): 
    final_list = []
    for i in range(-num,num+1,2):
        final_list.append(i*i)
    return final_list

#T6Q24
#Write a function getSumOfFirstDigit(numList) that takes in a list of
#positive numbers and returns the sum of all the first digit in the list. 



#T6Q26
#List comprehension offers a concise way to derive a new list from an
#existing list or sequence. Given a list of numbers, write a function
#that returns the numbers that are greater than the average. 

def getAboveAverage(nums):
    return [ x for x in nums if x > (sum(nums)/float(len(nums))) ]








 
