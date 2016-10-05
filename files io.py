#T13Q1
#The open method returns a file object. Syntax: open(name[, mode]). where mode
#can be 'r' (read), 'w'(write) or 'a'(append). The default mode is 'r'.The
#close method closes an opened file object.

filename = 'tmp.txt'      
mode = 'w'

f = open(filename, mode)  # open a file
f.write('hello')          # write to file
f.close()                 # close a file

#T13Q2
#Create a function that appends the name and email to the end of a named file.
def addEmail(filename, name, email):    
    mode = 'a'
    f = open(filename, mode) # replace the mode 
    f.write("%s %s\n" % (name, email))
    f.close()
    return f # do not remove this line 

#T13Q4
#read([size]). Read size bytes from the file, unless EOF is hit. If size is
#omitted or negative, the full data is returned. 

def readFile(filename):
    f = open(filename)
    count = 0
    lines = 0
    while 1:
        char = f.read(1)
        if not char: break
        count+=1
        if(char == '\n'):
            lines+=1
    f.close()                  # close file
    return (count, lines) 

#T13Q6
#Write a function to read the scores and compute the average score of the
#class. (Ignore the first line which contains the field headers).


print(readFile('test.txt'))
