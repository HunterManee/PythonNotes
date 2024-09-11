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
import test
print(test.testString) #output: Hello World

# Executes only if file run as a script (e.g., main main.py)
#if __name__ == '__main__':