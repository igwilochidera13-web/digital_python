"""
    LIST

    - indexing - 
    - add an item
        - append(item) - adds an item to the end of the list ✅
        - insert(position, item) ✅
    - update an item ✅ 
    - delete/remove an item  ✅
        - del
        - .remove(item)
    - find an item from a list ✅
    - loop through list ✅
    - list comprehension ✅
"""

"""
    print("welcome to class") 
    if student is a member of students and also a member of registered student

    else
    print("Go and register")
"""

# students = ["Odinaka", "Charlse", "Fred", "Sammy", "Joy", "Anita", "Bejoyful", "Paul", "Peter", "Andrew", "Pascal", "Martin", "Benita", "Valentine", "Grace", "Glory", "Tabitha"]

# registered_students = ["Fred", "Joy", "Anita", "Pascal", "Grace", "Benita", "Tabitha"]

# """
#     [output for <single_item> in list expression;]
# """

# students[13] = "Felicia" # update valentine -> Felicia

# print(students)

"""
 - LOOP
    ==> for loop
    syntax
    for <single_item> in list:

    range(start, end)
    range(1, 21) --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    100 - 6723
"""

# for number in range(50, 1001):
#     print(number)

# for student in students:
#     if student in registered_students:
#         print(student + " is registered")
#     else:
#         print(student + " is not registered")

"""
    class

    class Human:
        goToSleep()

    charlse = Human()

    charlse.goToSleep()
"""

"""
    {}
    [] <---
    ()
"""


"""
    using for loop generate 3x table

    3 x 1 = 3
    3 x 2 = 6
    3 x 3 = 9
    ...
    3 x 15 = 45

    4 x 1 = 4
    4 x 2 = 8
    ...
    4 x 15 = 60

    5  
"""
# range(start, end) -> []
# [6, 7, 8, ..., 15]
# range(1, )

# range(3, 6) => [3, 4, 5]

# for left in range(3, 6): # [3, 4, 5]
#     for right in range(1, 16): #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#         print(f"{left} x {right} = {left * right}")

# print("My age is " + str(my_age))
# print(f"My name is {}")

"""
    left = 3
        right -> 1...15
"""


# ### Tuple -> ()
# living_presidents = ["Goodluck Ebele Jonathan", "Bola Tinubu"]

# dead_presidents_one = (
#     "Shehu shagari", "Goodluck Ebele Jonathan", "Muhammadu Buhari", "Nnamdi Azikiwe"
# )

# dead_presidents_two = (
#     "Aguiyi Ironsi", "Bola Tinubu", "Obafemi Awolowo", "Tafawa Balewa"
# )

# dead_presidents = dead_presidents_one + dead_presidents_two

# # for, if, in, tuple    

# for living_presidents in dead_presidents:
#     if president in living_presidents:
#         print(f"{president} is not dead")

# range(1, 100)
# print out all the even numbers from 1 - 100

# use for loop - 1 - 101
# if num % 2 == 0
# print(num)


"""
    for num in range(1, 10):

    for num in [1, 2, 3, 4, 5, 6,]
"""

"""
    4 / 2 = 2 r 0
    5 / 2 = 2 r 1
    8 / 2 = 4 r 0
    9 / 2 = 4 r 1
"""
"""
    students = ["Graey", "Grace", "Benita"]

    for student in students:
        ....statements;

"""

# "President is not dead"
# dead_president_lists = list(dead_presidents)
# print(f"Before removal: {dead_presidents}")
"""
    convert dead_president to list
    remove living presidents from list
    re convert to tuple 
"""


# dead_presidents_list = list(dead_presidents)

# dead_presidents_list.remove("Goodluck Ebele Jonathan")
# dead_presidents_list.remove("Bola Tinubu")

# dead_presidents = tuple(dead_presidents_list)

# print(f"After removal: {dead_presidents}")
# dead_presidents_two.remove()

# to_change.remove("Bola Tinubu")
# # del to_change[3];

# dead_presidents_two = tuple(to_change)

# print(dead_presidents_two)

# Dictionary

"""
    Key-value pair
"""


"""
    .values() => ["Charlse", 18, "Graduate", {
        "state": "Enugu",
        "local_government": "Nsukka",
        "street": "Hilltop"
    }, "Nigeria"]

    .keys() => ["name", "age"...., "nationality"] #iterable

    .items() => [("name", "Charlse"), ("age", 18), ["education_level", "Graduate"...]] 
"""

## Function - enables you to reuse code implementation

def describe_me(name, age, location):
    print(f"My name is {name}, I am {age} years old, I stay at {location}")

# define a function that prints out all even numbers from a start to an end

# 5, 100 | 100 - 2000

# define a function that compute the factorial of a number
# 5! = 5 * 4 * 3 * 2 * 1
# 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

def factorial(value):
    result = 1
    for number in range(value, 0, -1):
        result = result * number

    print(result)

# recursion - Data structure and algorithm
def factorial(value):
    if value == 0:
        return 1
    
    return value * factorial(value - 1)

print(factorial(5))

"""
    positional
    keyword
""" 

describe_me("Charlse", 18, "hilltop")
describe_me("Peter", location="Odenigwe", age=21)


# write a function that returns name of healthy people

"""
    function <name>(names):
        return []
"""
names = ["John", "Peter", "Anthony", "Peace", "Bejoyful", "Grace"]
disabled = ("Peter", "Peace", "Bejoyful")
psych_patients = ("Anthony", "Peace", "John")

def get_healthy_persons(list_of_persons):
    healthy_persons = []

    for name in list_of_persons:
        if name not in (disabled + psych_patients):
            healthy_persons.append(name)

    return healthy_persons

    return [name for name in list_of_persons if name not in (disabled + psych_patients)]

print(get_healthy_persons(names))