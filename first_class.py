## Go to python.org and download python
## install it

## Python file extension ends with .py

# Introduction to Python

"""
    String(str) - "Fred", "University of Nigeria", "100"
    Number - Float and Integer
        Float(float) - 3.32, 7.1, 10.2, 33.2, 3.0
        Integer(int) - 3, 4, 1, 8, 9, 10
    Boolean
        Yes - True
        No - False
"""

# Comment

# Values ✅
# Variables ✅
# -----------------
# Mathematical Operators ✅
# Typecasting - convert from one type to another ✅

# Logical | Comparison | identity Operators ✅

# If...else...elif    ✅

# List  ✅
 
# Tuple ✅

# Function ✅
 # Updating an item

# Dictionary ✅
 # - Loop Dictionary ✅
 # - Copy Dictionary ✅
 # - Nested Dictionary ✅

# Set ✅

# Class 🔐

# File 🔐


# =================================
is_bread_available = True
is_book_available = True
is_plantain_available = False

# if age > 18:
#   print("")

# NOTE: only one statement will be executed
if is_bread_available and is_book_available:
    """
    NOTE: statements under if will execute, when 
    the if expression result to true
    """
    # indentation
    print("Pay vendor")
elif is_plantain_available:
    print("Add one bucket of milk and pay the vendor")
else:
    print("Go back home")

"""
   INEC REGISTRATION CENTRE
    - get user age => input("Enter your age")
    - check if user is eligible to vote
        - print("You are eligible")
    - print("You are ineligible") 

    - variable
    - comparison operator
    - typecasting
    - if...else
"""

user_age = int(input("Enter age: "))

if user_age >= 18:
    print("You are eligible")
else:
    print("You are ineligible")


# age = int(input("Enter age: "))

# print("You are eligible")
# print("You are ineligible")
# missing_person = "joy"

# user_name = input("Enter name: ")

# if user_name == missing_person:
#     print("Found missing person")
# else:
#     print("You are not the person")

# NOTE: "if" is used on logical expression

"""
    LOGICAL OPERATOR PRECEDENCE
    NOT
    AND
    OR
"""
# == and =


"""
=
    Comparison Operators

    - >=, <=, ==, >, <

    number_one = 5
    number_two = 7

    print(number_one < number_two) 

    Logical - logical expressions - True or False
    - and
    - not
    - or

    ==> AND
    P = Office is opened
    Q = Tutor is available
    # S = Solar is on

    R = sit for class

    NOTE: Your result will be True, iff both or all expression is/are true

    P(True) and Q(False) = False
    P(False) and Q(True) = False
    P(False) and Q(False) = False
    P(True) and Q(True) = True

    P(True) and Q(True) and S(False) = False


    ==> OR
    P = Office is opened
    Q = Tutor is available

    R = wait for sometime

    P(True) or Q(False) = True
    p(False) or Q(True) = True
    P(False) or Q(False) = False
    P(True) or Q(True) = True

    NOTE: Your result will be True, if at least one of the expression is True

    ==> NOT
    P = Office is opened

    not P(True) = False
    not P(False) = True

    - &&
    - ||
    - !

    5 && 2 = 101 && 010

    Identity
"""

"""
    Integer(int)
    String(str)

    int() - 
    str() -
    bool() -
"""

"""
String (str)
Integer (int)
Boolean (bool)
"""

# Exercise

# my_age = 27
 
# print("Hello, I am " + str(my_age) + " years old") # Hello, I am 27 years old

""""
    SyntaxError - 
    TypeError
    LogicalError
"""

# print(number_one * number_two)

"""
    You can join 2 strings together using +
    NOTE: You cannot perform any other operation on two string value except +(join|concatenation)

    Multiplication of string and integer duplicates the string by n integer
"""

"""
    Mathematical operators

    - addition + 
    - subtraction -
    - division /
    - multiplication *
    ---------------------
    - exponentiation **
    - modulus % - 
    - floor division //
"""




# create a variable called lunch, assign your what you ate this afternoon to it then print the variable out <<----

"""
 x = 8

 print(x)

 y = x + 7

 what is y?
"""
# # create a variable called university, assign your university to it and print it out
# university = "University of Nigeria"

# print(university)

# transport_fare = 1200


"""
    VARIABLE DECLARATION RULES
    - Your variable must not start with a number
    - Your variable must not contain space
    - Your variable must not contain any other symbol except _
    - Your variable are case sensitive
"""

# launch_food = "yam"

# Name = "Charlse"

# print(name)

# launch_f00d = "yam"

# print(launch_food)
