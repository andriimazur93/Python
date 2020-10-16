#T7Q1
#Write the function countA(word) that takes in a word as argument and
#returns the number of 'a' in that word. 

def countA(word):
	return word.count('a')

#T7Q2
#Write the function countLetter(word, letter) that takes in a word and
#a letter as arguments and returns the number of occurrence of that letter
#in the word. 

def countLetter(word, letter):
	return word.count(letter)

#T7Q3
#Write a function removeLetter(word, letter) that takes in a word and a
#letter as arguments and remove all the occurrence of that particular
#letter from the word. The function will returns the remaining leters
#in the word. 

def removeLetter(word, letter):
    return word.replace(letter, "")

#T7Q4
#Write the function changeCase(word) that changes the case of all the
#letters in a word and returns the new word. 

def changeCase(word):
    new_string = ""
    for i in word:
        if(i.isupper()):
            new_string += i.lower()
        else:
            new_string +=i.upper()
    return new_string

def changeCase2(word):
    return word.swapcase()

#T7Q5
#Write the function search(word, substring) that takes in a word and
#a substring as arguments and returns the position (0 indexed) of the
#substring if it is found in the word. The function returns -1 if the
#substring is not found. 

def search(word, substring):
    return word.find(substring)

#T7Q6

#A string contains a sequence of characters. Elements within a string can
#be accessed using index that starts from 0. Write the function getChar(word, pos)
#that takes in a word and a number as argument and returns the character at that position. 

def getChar(word, pos):
    if(pos > len(word)):
        return "Invalid range"
    return word[pos]

#T7Q7
#Write a function countVowels(word) that takes in a word as an argument and returns the
#number of vowels ('a', 'e', 'i', 'o', 'u') in the word. 

def countVowels(word):
    count = 0
    vowels = 'AaEeIiOoUu'
    for i in word:
        if(i in vowels):
            count+=1
    return count

#T7Q8
#Write the function getVowels(word) that takes in a word as an argument and returns
#the vowels ('a', 'e', 'i', 'o', 'u') in that word. 

def getVowels(word):
    vowels = 'AaEeIiOoUu'
    result = []
    for i in word:
        if(i in vowels):
            result+=i
    return result

#T7Q9
#Write the function capitalizeVowels(word) that returns the word with all the vowels capitalized.

def capitalizeVowels(word):
    vowels = 'AaEeIiOoUu'
    result = ""
    for i in word:
        if(i in vowels):
            result += i.upper()
        else:
            result += i
    return result

#T7Q10
#Write the function startEndVowels(word) that returns True if the word starts and ends with vowels.

def startEndVowels(word):
    vowels = 'AaEeIiOoUu'
    if(word == ""):
        return False
    if(word[0] in vowels and word[-1] in vowels):
        return True
    else:
        return False

#T7Q11
#Write the function removeVowels(word) that removes all the vowels ('a', 'e', 'i', 'o', 'u') in a word
#and returns the remaining letters in the word. 

def removeVowels(word):
    vowels = "AaEeUuIiOoYy"
    result = "" 
    for i in word.lower():
        if(i not in vowels):
            result+=i
    return result

#T7Q12
#Write the function reverseWord(word) that returns the word in the reverse order. 

def reverseWord(word):
    rev=""
    for i in word:
        rev=i+rev
    return rev

def reverseWord(word):
    return rev[::-1]



#T7Q13
#Write the function isReverse(word1, word2) that takes two words as arguments and returns True is the
#second word is the reverse of the first word. 

def isReverse(word1, word2):
    i = 0
    j = len(word2)
    flag = False
    if(len(word1)!=len(word2)):
        return False
    while(j>=0 and i<= len(word1)-1):
        if(word1[i] != word2[j-1]):
            return False
        i+=1
        j-=1
    return True

#T7Q14
#Write the function startWithVowel(word) that takes in a word as argument and returns a substring that starts
#with the first vowel found in the word. The function returns 'No vowel' if the word does not contain vowel. 

def startWithVowel(word):
    vowels = "aeuioy"
    i = 0
    index = -1
    length = len(word)-1
    while(i <= length):
        if(word[i] in vowels):
            index = i
            break
        i+=1
    if(index == -1):
        return 'No vowel'
    else:
        return word[index:]



#T7Q15
#Write the function getCommonLetters(word1, word2) that takes in two words as arguments and returns a new string
#that contains letters found in both string. Ignore repeated letters and sort the result in alphabetical order. 

def getCommonLetters(word1, word2):
   res = ""

   for letter in word1:
      if letter in word2:
         if letter not in res: # skip if we already found it
             # don't return yet, but rather accumulate the letters
             res = res + letter
   res = ''.join(sorted(res))
   return res

#T7Q16
#Write a function mirrorText(word1, word2) that takes in 2 words as arguments and returns a new word in the
#following order: word1word2word2word1. 

def mirrorText(word1, word2):
        return word1+word2+word2+word1

#T7Q17
#Write a function echoWord(word) that takes in a word as arguments and returns a word that repeats itself
#based on the number of letter in the word.

def echoWord(word):
    return (len(word)*word)

#T7Q18
#Write a function rightJustify(word) that takes in a word as argument and return a word with leading
#spaces so that the last letter of the word is in column 50 of the display. 

def rightJustify(word):
    return (50 - len(word))*" "+word

#T7Q19
#A palindrome is a word, phrase, number or other sequence of units that can be read the same way in
#either direction. Write a function that determines whether the given word or number is a palindrome. 

def isPalindrome(word):
    word = str(word)
    if(word == ""):
        return False
    word = word.lower()
    rev_word = word[::-1]
    if(word == rev_word):
        return True
    else:
        return False
        
#T7Q20
#Topic 7: Question 20
#Write a function isInAlphabeticalOrder(word) that takes in a word as argument and returns True if the
#word contains letters that are arranged in alphabetical order. For example, the letter 'c' should not
#appear before the letter 'a'. 

def isInAlphabeticalOrder(word):
    sorted_word = ''.join(sorted(word))
    if(word == sorted_word):
        return True
    return False

#T7Q21
#Write a function isAllLettersUsed(word, required) that takes in a word as the first argument and returns
#True if the word contains all the letters found in the second argument. 

def isAllLettersUsed(word, required):
    splited = list(word)
    for i in required:
        if i not in splited:
            return False
    return True

#T7Q22
#Write a function isTripleDouble(word) that takes in a word as argument and returns True if the word contains
#three consecutive double letters. 

def isTripleDouble(word): 
 	count = 0  
 	i = 1 
 	while i < len(word): 
 		if word[i] == word[i-1]: 
 			count += 1 
 			i+=2 
 		else: 
 			count = 0 
 			i+=1 
 	if count == 3: 
 		return True 
 	else: 
 		return False 

#T7Q23
#Write a function splitWord(word, numOfChar) that takes in a word and a number as arguments. The function will
#split the word into smaller segments with each segment containing the number of letter specified in the numOfChar
#argument. These segments are stored and returned in a list. 

def splitWord(word, numOfChar): 
 	output = [] 
 	for i in range(0,len(word),numOfChar): 
 		output.append(word[i:i+numOfChar]) 
 	return output 

#T7Q24
#An anagram is a word formed by reordering the letters of another word. Write a function isAnagram(w1, w2) that
#takes in two words as arguments and return True if one word is an anagram of the other word. 

def isAnagram(w1, w2):
     w1 = sorted(w1.lower())
     w2 = sorted(w2.lower())
     if(w1==w2):
         return True
     return False

print(isAnagram('google', 'gogole'))
print(isAnagram('google', 'gogoll'))
print(isAnagram('google', 'gogogo'))
print(isAnagram('Google', 'google'))










