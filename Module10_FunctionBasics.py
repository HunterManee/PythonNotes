###### 10.1 ############## User-defined Function Basics #####################
'''
Function: Programmers use to reduce program redundancy by creating grouping 
    of predefined statements

Function Definition consists of the function's name and a block of statements
    EX: def calc_pizza_area():

Function Call: invocation of the funtion's name, causing the function's
    statements to execute

def: Keyword is used to create new functions

Return Statement: Allows the function to return one value

None: a special keyword that indicates no value

Parameter: A function input specified in a function definition.
    EX. def function(parameter): | def function(para1, para2)
Argument: a value provided to a function's parameter during a function call
    EX. function(1): | function(1, 2)
'''
###### 10.2 ############## Print Functions ##################################
'''
Void Function: A function with no return statemnet
'''
###### 10.3 ############## Reasons for Defining Functions ###################
'''
Modular Development: The process of dividing a program into separate modules
    that can be developed and tested separately and integrated into a single
    program.
'''
###### 10.6 ############## Functions with branches/loops ####################

def function():
    pass

def function_parameter(parameter):
    pass

def function_parameters(first_parameter, second_parameter):
    pass

def function_with_branches():
    if False:
        pass
    elif False:
        pass
    else:
        return None
    
def function_with_loops():
    while True:
        break
    
    for i in range(0,3):
        continue

###### 10.7 ############## Scope of variables and functions #################
'''
Scope: A variable or function object is only visible to part of a program

Local Variables: Variables that are defined inside of a function
'''

def function():
    local_variable = 0

'''
Global Variable: A variable defined outside of a function

Global: Statement mst be used to change the value of a glabal varaiable
    inside of a function
'''

global_variable = 'N/A'
def function():
    global global_variable

###### 10.8 ############## Namespaces and scope resolution ##################
'''
Namespace: Maps names to objects

Scope Resolution: Te process of searching for a name in the available
    namespaces
'''

print(globals()) #output: All functions and variables in the global namespace

def function_for_locals():
    local_variable = 'Hello_World'
    print(locals())  #output: All functions and variables in the local namespace

function_for_locals()

###### 10.9 ############## Modules ##########################################
'''
Script: A programmer will typicall write Python code in a file, and pass
    that file as iput to the interpreter

Module: A file containing Python code that can be imported and used by
    scripts, other modules, or the interactive interpreter

import: Keyword to execute the code contained by the module and
    make the definitions within that module available for use
    by the importing program
'''

import sys #imports a file called sys.py

'''
Dependency: A module being required by another program
'''

print(sys.modules) #output: A dictionary of the loaded modules

'''
Module Object: a namespace that contains definitions from the module
'''

import random
'''
sys.modules checked for random
module object created
random added to sys.modules
random code executed
random added to importer's namespace
'''

'''
Side note when creating your own scripts to be imported use dot notation
    to interacte with variables and functions inside of imported script

import made_up_script
made_up_script.variable
made_up_script.function()
'''

###### 10.10 ############## Importing Specific Names from a Module ##########

'''
hashlib: A standard library module that contains a number of algorithms for
    creating a secure HASH of a text message
'''
import hashlib

'''
Can import particular parts of a module
from made_up_script import variable
from made_up_script import function
from made_up_script import variable, function
'''

'''
__name__: is a global string variable automatically added to every module 
    that contains the name of the module.

Before running script: __name__ == 'Module10_FunctionBasics'
While running script: __name__ == '__main__'

if __name__ == '__main__': is added to scripts so they can be unit tested
'''

