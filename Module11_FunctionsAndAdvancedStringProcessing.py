###### 11.1 ############## Help! Using Docstring to Document Functions ######
'''
Docstring: a string iteral placed in the first line of a function body
    represended by 3 single quotes(') or 3 double quotes (") as followed: """

help(): A function the can aid a programmer by providing them with all
    the documentation associated with an object
'''

###### 11.2 ############## Functions are Objects ############################
'''
Bytecode: Represents the statements to be executed by the function
'''

def print_hello_world():
    print('hello world')

func = print_hello_world
func() #output: hello world

###### 11.3 ############## Function Arguments ###############################
'''
pass-by-assignment: Arguments to functions are passed by object references

immutable: such as a s string or integer, then the modifcation is limited
    to inside the function. Any modifcation to an immutable object results
    in the creation of a new object in the function's local scope, thus 
    leaving the original argument object unchanged.

mutable: modification of the object is seen outside the scope of the
    function. Any operation like adding elements to a container or sorting
    a list that is performed within a function will also affect any other
    variables in the program that reference the same object.
'''

def modify(num_list):
    num_list[1] = 99

my_list = [10, 20, 30]
modify(my_list[:]) # Pass a copy of the list

print(my_list) # my_list does not contain 99!

modify(my_list) #Pass the actual list

print(my_list) # my_list does contain 99!

###### 11.4 ############## Multiple Function Outputs ########################
'''
Unpacking: An operation that allows a statement to perform multiple
    assignments at once to variables in a tuple or list.
'''

def return_tuple():
    return 1, '2', [3, '4']

n, s, l = return_tuple()

###### 11.5 ############## Dynamic Typing ###################################
'''
add(): Function used to add two integers together or concatenate to strings
    together

Polymorphism: The function's behavior of adding together different
    types as a concept.

Dynamic Typing: Determines the type of objects as a program executes

Static Typing: Programmer must define the type of every variable and
    every function parameter in a program's source code
'''

###### 11.6 ############## Keyword Arguments and Default Parameter Values ###
'''
Keyword Arguments: Allows arguments to map to parameters by name, instead of
    implicitity by position in the argument list.

All keyword arguments must come after every positional argument
'''

def show(a, b, c=16):
    print(f'{a}/{c}/{b}')

show(2, 1, c=8)
show(9, 4)

'''
Default Parameter Value: A Function call can optionally omit an argument,
    and the default parameter value will be substituted for the 
    correspoinding omitted argument.

Default Value: The value used in the absence of an argument in the
    function call
'''

def show(a, b, c):
    print(f'{a}\{b}\{c}')

show(a=1, c=6, b=9)


def show_time(year, month, day, hour, minutes):
    print(f'{month}-{day}-{year} {hour}:{minutes}')

show_time(2017, 2, minutes=14, day=27, hour=6)


def show(a, b=6, c=9):
    print(f'{b}\{c}\{a}')

show(b=3, a=8)
show(c=4, a=7)

###### 11.7 ############## String Methods ###################################
'''
replace(old, new): Returns a copy of a string with all occurrences of the
    the substring old replaced by the string new. The old and new arguments
    may be string variables or string literals

replace(old, new, count): Same as above, except replace(old, new, count)
    only replaces the first count occurrences of old.
'''

string = 'Hello World'
string = string.replace('Hello', 'Hello Hello')
print(string) #output: Hello Hello World
string = string.replace('Hello', 'Bye', 2)
print(string) #output: Bye Bye World

'''
find(x): Returns the index of the first occurece of item x in the string,
    otherwise, find(x) returns -1. x may be a string variable or string
    literal.
find(x, start): Same as find(x), but begins the search at index start
find(x, start, end): Same as find(x, start), but stops the search at index
    end -1
rfind(x): Same as find(x) but searches the string in reverse, returning
    the last occurrence in the string.

count(x): Returns the number of times x occurs in the string
'''

'''
'Hello' == 'Hello'	            True	
'Hello' == 'Hello!'	            False	
'Yankee Sierra' > 'Amy Wise'	True	
'Yankee Sierra' > 'Yankee Zulu'	False	
'seph' in 'Joseph'	            True	
'jo' in 'Joseph'	            False
'''

'''
isalnum() -- Returns True if all characters in the string are lowercase or 
    uppercase letters, or the numbers 0-9.
isdigit() -- Returns True if all characters are the numbers 0-9.
islower() -- Returns True if all cased characters are lowercase letters.
isupper() -- Returns True if all cased characters are uppercase letters.
isspace() -- Returns True if all characters are whitespace.
startswith(x) -- Returns True if the string starts with x.
endswith(x) -- Returns True if the string ends with x.
'''

'''
capitalize() -- Returns a copy of the string with the first character 
    capitalized and the rest lowercased.
lower() -- Returns a copy of the string with all characters lowercased.
upper() -- Returns a copy of the string with all characters uppercased.
strip() -- Returns a copy of the string with leading and trailing whitespace 
    removed.
title() -- Returns a copy of the string as a title, with first letters of 
    words capitalized.
'''

###### 11.9 ############## Splitting and Joining Strings ####################
'''
split(): Splits a string into a list of tokens
Token: A substring that forms a part of a larger string
Separator: A character or sequence of characters that indicates where to 
    split the string into tokens

join(): string method performs the inverse operation of split() by joining a
    list of strings together to create a single string.
'''

phrases = ['To be, ', 'or not to be.\n', 'That is the question.']

sentence = ''.join(phrases)
print(sentence)
'''
output: 
    To be, or not to be.
    That is the question.
'''