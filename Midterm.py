#The three different variable types: string, int, and float
string = input('Type something: ') #chickens
integer = int(input()) #5000
decimal = float(input()) #5.0

#output options
print(f'{2**2=}') #output: 2**2=4
print(f'{string=}') #output: string='chickens'
print(f'{{2**2}}') #output: {2**2}
print(f'{{{2**2=}}}') #output: {2**2=4}

#String (default presentation type - can be omitted)
print(f'{string:s}') #output: chickens
#Decimal (integer values only)
print(f'{integer:d}') #output: 5000
#Decimal (integer values only) with commas
print(f'{integer:,d}') #ouput: 5,000
#Leading 0 notation
print(f'{integer:03d}') #output: 004
#Binary (integer values only)
print(f'{integer:b}') #output: 1001110001000
#Hexadecimal in lowercase (x) and uppercase (X) (integer values only)
print(f'{integer:x}')  #output: 1388
print(f'{integer:X}')   #output: 1388
#Exponent notation
print(f'{integer:e}') #output: 5.000000e+03
#Fixed-point notation (six places of precision)
print(f'{integer:f}') #output: 5000.000000
#Fixed-point notation (programmer-defined precision)
print(f'{integer:.2f}') #output: 5000.00
#Fixed-point notation (programmer-defined precision) with commas
print(f'{integer:,.2f}') #output: 5,000.00

#Exponents: Represented by **
#Integer Division: Represented by // Takes floor of division results
#Module: Represented by % Takes the remainder of division result

#import personal scripts
import AnotherScript
print(AnotherScript.testString) #output: Hello World

# Executes only if file run as a script (e.g., main main.py)
#if __name__ == '__main__':

print(len(string)) #output: 8
print(string[0]) #output: c
print(string[-1]) #output: s
print(string + string) #output: chickenschickens
print(chr(69)) #output: E
print(ord(string[0])) #output: 99

array = ['Hello', 'World']
print(len(array))    #output: 2
print(array[0])      #output: Hello
print(array[-1])     #output: World
print(array + array) #output: ['Hello', 'World', 'Hello', 'World']

#field width
print(f'{"Player Name":16}{"Goals":8}')
print('-' * 24)
print(f'{"Sadio Mane":16}{"22":8}')
print(f'{"Gabriel Jesus":16}{"7":8}')
'''output:
    Player Name     Goals   
    ------------------------
    Sadio Mane      22      
    Gabriel Jesus   7  
'''

#Left-aligned
print(f'{"Player Name":<16}{"Goals":<8}') #output: 'Player Name     Goals  '
#Right-aligned
print(f'{"Player Name":>16}{"Goals":>8}') #output: '    Player Name   Goals'
#Centered
print(f'{"Player Name":^16}{"Goals":^8}') #output: '  Player Name    Goals '

#Fill Character
score = 9
print(f'{score:}')    #output: '9'
print(f'{score:3}')   #output: '  9'
print(f'{score:0>3}') #output: '009'
print(f'{score:0<3}') #output: '900'
print(f'{score:0^3}') #output: '090'

#Percision
print(f'{5:.1f}')      #output: '5.0'
print(f'{5:.3f}')      #output: '5.000' 
print(f'{5.25:.3f}')   #output: '5.250'
print(f'{5.2589:.3f}') #output: '5.259'
print(f'{5:4.1f}')     #output: ' 5.0'

'''Slice Notation
    string[start:end] #start(inclusive):end(exclusive)
    array[start:end] #start(inclusive):end(exclusive)

    print(string[:5]) #output: chick
    print(array[:1])  #output: Hello

    print(string[::2]) #output: cikn
'''
'''Arrays
    index = 0
    array.append('!') #['Hello', 'World', '!']
    array.pop(index)  #['World' '!']
    array.remove('!') #['World']

    len(array)       #gets length of array
    array + array    #concatenates two arrays
    min(array)       #min value of array
    max(array)       #max value of array
    sum(array)       #sum of all value in array
    array.index(val) #Find the index of the first element in the list whose value matches val
    array.count(val) #Count the number of occurrences of the value val in the array
'''

#Tuple: (1, 2, 3)
from collections import namedtuple

Car = namedtuple('Car', ['make','model','price','horsepower','seats'])  # Create the named tuple

chevy_blazer = Car('Chevrolet', 'Blazer', 32000, 275, 8)  # Use the named tuple to describe a car
chevy_impala = Car('Chevrolet', 'Impala', 37495, 305, 5)  # Use the named tuple to describe a different car

print(chevy_blazer) #output: Car(make='Chevrolet', model='Blazer', price=32000, horsepower=275, seats=8)
print(chevy_impala) #output: Car(make='Chevrolet', model='Impala', price=37495, horsepower=305, seats=5)

print(chevy_blazer.make) #output: Chevrolet

#Dictionary

players = {
    'Lionel Messi': 10,
    'Cristiano Ronaldo': 7
}

print(players) #output: {'Lionel Messi': 10, 'Cristiano Ronaldo': 7}

'''IF STATEMENTS

    if condition:

    if condition:
    else:
    
    if condition:
    elif condition:
    else:
    
    ==, !=
    <=, <, >, >=
    and, or, not

    if condition:
        if condition:
        else:
'''

'''OPERATIONS
    in/not in
    if 'chick' in string:
    if 'chick' not in string:
    
    if id(string) is string:
    
    string = 'chicken' if string != 'chicken' else string
'''

import random
random.random() #Random float-point from 0(inclusive)-1(exclusive)
random.randrange() #min(inclusive), max(exclusive)
random.randint() #min(inclusive), max(inclusive)
random.seed() #Used to help with creating randomness (int)