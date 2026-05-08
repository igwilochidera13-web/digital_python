
"""
    - add 
    - update
    - remove
    ...
    make changes to lifst
"""

fruits = ("apple", "banana", "cherry", "pawpaw", "mango", "cashew", "pineapple") # ("apple", ) and ("apple")

# print("pawpaw" not in fruits) # True or False

# first_fruit = fruits[0]
# second_fruit = fruits[1]
# third_fruit = fruits[2]

# (first_fruit, _, third_fruit, *other_fruit) = fruits

for fruit in fruits:
    print(fruit)

# other_fruit = ["cherry", "pawpaw", "mango", "cashew", "pineapple"]

# print(f"First fruit: {first_fruit}\Third Fruit: {third_fruit}")

# string, int, float, bool, list, tuple
# print(fruits[2:]) # ("apple", "orange")
# range(3) => range(0:3) => [0, 1, 2] -> 0 -> n - 1
# fruits[start:end] = fruits[2:6]
# end 

# range(start, end)

# for number in range(1, 16):

# fruits[start:end:step] default(step) = 3

# ""
# print(len(fruits)) # 3

# what is data type - 

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2

fruits = ("apple", "banana","apple", "cherry", "pineapple", "apple")

print(fruits.count("apple"))

# ("a", "b", "c", 1, 2, 3)