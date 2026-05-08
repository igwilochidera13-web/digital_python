person_one = {
    "name": "Kingsley",
    "age": 20,
    "location": {
        "state": "Enugu",
        "locality": "Nsukka",
        "address": "Behind Flat"
    },
    "university": {
        "name": "Miva Open University",
        "chancellor": {
            "name": "Sim shagaya",
            "occupation": "Tech Entrepreneur",
            "companies": ["Konga", "Ulesson", "Miva Open University"]
        },
        "population": 10_000
    }
}

# dfsjkfhkfsh

print(person_one["university"]["chancellor"]["occupation"])

# person_two = {
#     "name": "Kingsley",
#     "age": 20,
#     "location": "Behind Flat"
# }

"""
    - keys()
    - values()
    - items()

    person.keys() -> ["name", "age", "location"]
    person.values() -> ["Kingsley", 20, "Behind Flat"]
    person.items() -> [("name", "Kingsley"), ("age", 20), ("location", "Behind Flat")]
"""

# person_two = person_one

# print(person_two is person_one); # memory address
