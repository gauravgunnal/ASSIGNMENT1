'''Q1'''
A="GAURAV GUNNAL"
B=[2,9,8,6,56.8,"CHITRA"]
C=12.99
D=(3,"AMITH",34.56)

print(type(A))
print(type(B))
print(type(C))
print(type(D))

'''Q2'''
VAR1=''
VAR2='[DS,ML,PYTHON]'
VAR3=['DS','ML','PYTHON']
VAR4=1

print(type(VAR1))
print(type(VAR2))
print(type(VAR3))
print(type(VAR4))

'''Q3'''
'''((i)The / operator in Python is used for division. It performs division and 
returns the quotient as a floating-point number.)
'''
dividend = 10
divisor = 3
quotient = dividend / divisor
print(quotient)  # Output: 3.3333333333333335

'''((ii)The % operator, known as the modulo operator, is used to calculate the 
remainder of division between two numbers.
'''
dividend = 10
divisor = 3
remainder = dividend % divisor
print(remainder)  # Output: 1

'''((iii)The // operator is the floor division operator. It performs division and returns 
the quotient as an integer, discarding the decimal part.)
'''
dividend = 10
divisor = 3
quotient = dividend // divisor
print(quotient)  # Output: 3

'''((iv)The ** operator is used for exponentiation. It raises the left operand to 
the power of the right operand.
'''
base = 2
exponent = 3
result = base ** exponent
print(result)  # Output: 8

'''Q4'''
J=[1.1, 2017, 3+4j, 'superbowl', (4, 5), [1,2,3,5,12],{"make":'BMW', "model":'X5'},9,6.9,"GAURAV"]
print(len(J))
for i in J:
    print(i)
    print(type(i))

'''Q5'''
def count_divisions(a, b):
    count = 0
    while a % b == 0:
        count += 1
        a = a / b
    return count

# Test the function
number_a = 120
number_b = 6

divisions = count_divisions(number_a, number_b)
if divisions > 0:
    print(f"Number A is divisible by number B and can be divided {divisions} times.")
else:
    print("Number A is not divisible by number B.")

'''Q6'''
N=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
for i in N:
    if i%3==0:
        print(f"{i} is not divisible by 3")
    else:
        print(f" {i} is  divisble by 3")


'''Q7'''
'''In Python, mutable and immutable are two fundamental concepts related to data types. 
The key difference between them is that mutable objects can be modified after they are created, while immutable 
objects cannot be changed once they are created.'''

'''Immutable Data Types:EXAMPLES'''
# Strings
string_variable = "Hello"
print(string_variable)  # Output: Hello

string_variable += " World"
print(string_variable)  # Output: Hello World

# Tuples
tuple_variable = (1, 2, 3)
print(tuple_variable)  # Output: (1, 2, 3)

tuple_variable += (4,)
print(tuple_variable)  # Output: (1, 2, 3, 4)

'''Mutable Data Types:EXAMPLES'''
# Lists
list_variable = [1, 2, 3]
print(list_variable)  # Output: [1, 2, 3]

list_variable.append(4)
print(list_variable)  # Output: [1, 2, 3, 4]

# Dictionaries
dict_variable = {'key': 'value'}
print(dict_variable)  # Output: {'key': 'value'}

dict_variable['new_key'] = 'new_value'
print(dict_variable)  # Output: {'key': 'value', 'new_key': 'new_value'}

