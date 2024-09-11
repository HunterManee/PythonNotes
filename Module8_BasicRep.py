###### 8.1 ############## Loops (General) ###################################
'''
Loop: Program construct that repeatedly executes the loop's statements
    (Know as the LOOP BODY) while the loop's expession is true; when
    the expression is false, execution proceeds past the loop.

Iteration: Each time through a loop's statements is called.

'''
###### 8.2 ############## While Loops #######################################
'''
While Loop: A construct that repeatedly executes an idented block of code
    As long as the loop's expression is True.

Sentinel Value: A value that when evaluated by the loop expression causes
    the loop to terminate.

Infinite Loop: a loop that will always execute because the loop's expression
    is always True.
'''
num = 0
while num < 10: #Iterate until num >= 10
    num += 1
###### 8.3 ############## More while Examples ###############################
'''
Docstring: A multi-line string literal delimited at the beginning and end
    by triple quotes
'''
###### 8.4 ############## Counting ##########################################
'''
Loop Variable: The programmer can use a variable to count the number of
    iterations
'''
###### 8.5 ############## For Loop ##########################################
'''
For Loop: statement over each element in a container one at a time, 
    assigning a variable with the next element that can the be
    used in the loop body
'''
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number)

string = 'Chickens'
for char in string:
    print(char)

#Start from end of list and go to the beginning of list
for numbers in reversed(numbers):
    print(number)

dictionary = {
    'word1': 'def',
    'word2': 'def',
    'word3': 'def'
}
for key in dictionary:
    print(f'{key}: {dictionary[key]}')
###### 8.6 ############## Iterating Over a List #############################
'''
Index Error: Accessing an index that is out of range causes the program to 
    automatically abort execution.

enumerate(array) => list(pos, token)
    for pos, token in enumerate(array):
        pos: index
        token: value

all(array): True if every element in list is True(!=0), or if the list is empty.
any(array): True if any element in the array is True(!=0)
max(array): Get the max element in array
min(array): Get the min element in array
sum(array): Get the sum of all elements in the array 
'''
