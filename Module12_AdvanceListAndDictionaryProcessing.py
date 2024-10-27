###### 12.1 ############## List Nesting #####################################
'''
List Nesting: A list that holds a list(s)

Multi-dimensional Data Structure: Nesting data structures into each other 
    such as list in a list

Nested for loop: placing a for loop in another for loop
'''

###### 12.2 ############## List Methods #####################################
'''
List Method: Useful operation on a list such as adding or removing elements, 
    sorting, reversing, etc
'''

'''
ADD
list.append(x)	    Add an item to the end of list.	
list.extend([x])	Add all items in [x] to list.
list.insert(i, x)	Insert x into list before position i.	

REMOVING
list.remove(x)	Remove first item from list with value x.
list.pop()	    Remove and return last item in list.
list.pop(i)	    Remove and return item at position i in list.

MODIFYING
list.sort()	    Sort the items of list in-place.
list.reverse()	Reverse the elements of list in-place.	

MISCELLANEOUS
list.index(x)   Return index of first item in list with value x.
list.count(x)   Count the number of times value x is in list.
'''
###### 12.3 ############## List Comprehensions ##############################
'''
List Comprehension: Iterates over a list, modifies each element, and returns
    a new list of the modified elements.
'''

#Add 10 to every element
my_list = [5, 20, 50]
for i in range(len(my_list)):
    my_list[ i ] += 10
print(my_list)

my_list = [5, 20, 50]
my_list = [(i + 10)for i in my_list]
print(my_list)

#Convert every element to a string
my_list = [5, 20, 50]
for i in range(len(my_list)):
    my_list[ i ] = str(my_list[ i ])
print(my_list)

my_list = [5, 20, 50]
my_list = [str(i) for i in my_list]
print(my_list)

#Convert every element to a int
my_list = ['5', '20', '50']
for i in range(len(my_list)):
    my_list[ i ] = int(my_list[ i ])
print(my_list)

my_list = ['5', '20', '50']
my_list = [int(i) for i in my_list]
print(my_list)

#Find the sum of each row in a two-dimensional list
my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = []
for row in my_list:
    sum_list.append(sum(row))
print(sum_list)

my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = [sum(row) for row in my_list]
print(sum_list)

#Find the sum of the row with the smallest sum in a two-dimensional table
my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = []
for row in my_list:
    sum_list.append(sum(row))
min_row = min(sum_list)
print(min_row)

my_list = [[5, 10, 15], [2, 3, 16], [100]]
min_row = min([sum(row) for row in my_list])
print(min_row)

###### 12.4 ############## Loops Modifying Lists ############################
'''
for num in list(my_list):

creates a compy of my list so that way 
you can remove elements from the list while in the loop
'''
my_list = [20, 30, 40, 50, 60]

for num in list(my_list):
    if num < 35:
        my_list.remove(num)

###### 12.5 ############## Sorting Lists ####################################
'''
sort(): Sorts your from lowest to highest. Numbers compared their values,
    strings compare ASCII/Unicode encoded values, lists compare element-by-
    element, etc

sorted(): A built-in function provides the same sorting functionality as
    list.sort() method, however, sorted() creates and reurns a new list
    instead of modifying an existing list

key: specifies a function to be applided to each element prior to being compared
    EX. key_sort = sorted(names, key=str.lower)
'''

sorted([15, 20, 25], reverse=True) #[25, 20, 15]

###### 12.6 ############## Dictionary Methods ###############################
'''
Dictionary Method: A function provided by the dicitonary type (dict) that 
    operates on a specific dictionary object.

my_dict.clear(): Removes all items from the dictionary

my_dict.get(key, default): Reads the value of the key from the dictionary.
    If the key does not exist in the dictionary, then returns default.

my_dict1.update(my_dict2): Merges dictionary my_dict with another dictioanry
    my_dict2. Existing entries in my_dict1 are overwritten if the same keys
    exist in my_dict2

my_dict.pop(key, default): Removes and returns the key value from the 
    dictionary. If key does not exist, then defualt is returned.

'''

###### 12.7 ############## Dictionary Nesting ###############################
'''
Nested Dictionaries: A dictionary contains another dictionary as a value

Data Structure: A moethod of organizing data in a logical and coherent
    fashion
'''

my_dict = {'another' : {'dictionary': True}}
print(my_dict['another']['dictionary']) #output: True