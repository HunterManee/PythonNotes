###### 9.1 ############## Developing Programs Incrementally #################
'''
Incremental Programming: Experienced programmers start with a simple version
    of the program, and grwoing the program little by little into a complete
    version

FIXME Comment: attracts attention to code that needs to be fixed in the 
    future

'''
###### 9.2 ############## Nested Loops ######################################
'''
Nested Loop: A loop that appears as part of the body of another loop

Outer Loop: Parent Loop

Inner Loop: Loop that appears inside the Parent Loop
'''
###### 9.3 ############## Break and Continue ################################
'''
break: a statement the immediatley exits the loop
continue: a statement the immediatley jumps the the loop's header statemnent
'''

for i in range(100000000000000000000000000000000000000000000000000000000000):
    if i >= 10:
        print('Break: {i}')
        break
   
for i in range(10):
    if i % 2 == 0:
        print(i, end='')
        continue
    print('_', end='')
print()
###### 9.4 ############## Looping Enumerate() ###############################
'''
enumerate(): retrieves both the index and corresponding element value at the
    same time.

Unpacking: is a process that performs multiple assignments at once, binding
    comma-separated names on the left to the elements of a sequence on the
    right. Ex: num1, num2 = [350, 400] => num1 = 350, num2 = 400
'''

my_list = [4, 3, 2, 1, 0]
for index, value in enumerate(my_list):
    print(f'Index: {index}, Value: {value}')
###### 9.5 ############## Reading Files #####################################
'''
open(): A common programming task is to tetrieve input from a file instead
    of using keyboard entry

file.close(): Method to close the file, afte which no more reads or writes
    to the file are allowed

file.read(): Method returns the files contents as a string
file.read(INT): Only read INT bytes of a file

file.readlines() method returns a list of strings, where the first element
    is the contents of the first line, second element os the contents of 
    the second line, and so on.

EOF (end-of-file): Is detectd when no more data is availiable
'''

myFile = open('myFile.txt')
content = myFile.read()
myFile.close()
print(content)

myFile = open('myFile.txt')
lines = myFile.readlines()
myFile.close()
print(lines)
###### 9.6 ############## Writing Files #####################################
'''
file.write(STRING): method writes a STRING argument to a file

Mode: indicates how a file is opened such as whether or not writing to the
    file is allowed

        Read mode 'r': opens a file for reading. If the file is missing, 
            then an error will occur.

        Write mode 'w': opens a file for writing. If the file is missing, 
            then a new file is created. Contents of any existing file 
            are overwritten.

        Append mode 'a': opens a file for writing. If the file is missing, 
            then a new file is created. Writes to the file are appended to 
            the end of an existing file's contents.

****************************************************************************      
Additionally, a programmer can add a '+' character to the end of a mode, 
    like 'r+' and 'w+' to specify an update mode. Update modes allow for 
    both reading and writing of a file at the same time.
****************************************************************************      
'''
#Open in read mode
myFile = open('myFile.txt', 'r')
myFile.close()
#Open in write mode
myFile = open('myFile.txt', 'w')
myFile.close()
#Open in append mode
myFile = open('myFile.txt', 'a')
myFile.close()

'''
file.flush(): method can be called to tforce the interpreter to flush the
    output buffer to disk.

****************************************************************************      
 Additionally, the os.fsync() function may have to be called on some 
    operating systems. Closing an open file also flushes the output buffer.
**************************************************************************** 
'''
import os

myFile = open('myFile.txt', 'w')

myFile.write('Hello,\n\nThis is example of content in a text file')

myFile.flush()
#os.fsync(f.fileno())

myFile.close()
###### 9.7 ############## Handling Exceptions Using Try and Except ##########
'''
Error-Checking Code: Code that a programmer introduces to detect and 
    handle errors that occur while the program executes.

Exception-Handling: Handles exceptional circumstances, or errors, during 
    execution
'''
try:
    x = 1 / 0
except:
    print("Can't divide by 0")

'''
EOFError:	input() hits an end-of-file condition (EOF) without reading any input.
KeyError:	A dictionary key is not found in the set of keys.
ZeroDivisionError:	Divide by zero error
ValueError:	Invalid value (Ex: Input mismatch)
IndexError:	Index is out of bounds.
'''