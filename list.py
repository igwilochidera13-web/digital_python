# List Introduction

names = ["Charlse", "Kingsley", "Paul", "Peter", "Odinaka", "Sammy"]

names.insert(2, "Joy")

counter = 1;
"""
    for item in list:
        do_something(item)

        1 iteration -> item = "Charlse"
        2 iteration -> item = "Kingsley"
        3 iteration -> item = "Paul"
"""

new_list = [name]

for name in names:
    if  not (name == "Paul"): # !=
        new_list.append(name)



print(new_list)

"""
    del list[index]

    .remove()
"""

# print(names)
 
# list slice
"""
    names[start:end]

    range(start, end) => 

    names[1:4] = ["Kingsley", "Paul", "Peter"]
"""

"""
NOTE: list is zero-indexed
    .insert(position, item)
"""
# names.insert()

# print(names)