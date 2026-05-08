"""
    Enter your fullname:  _____
"""
"""
Ask the user for:
Full name
Age
Exam score
Whether they have a valid ID card (yes or no)
"""
fullname = input("Enter your full name: ");
age = int(input("Enter your age: ")); # 17
exam_score = int(input("Enter examination score: "));
has_valid_id_card = input("Do you have Valid ID card?: ");

# Use typecasting where necessary.

# exam_score = 90

"""
    int()
    float()
    bool()
    str()
"""

"""
    Use mathematical operators to:

Add 5 bonus points to the exam score # 95
Calculate how many years remain before the student turns 30
"""

final_score =exam_score + 5; # exam_score = exam_score + 5 - 90

remaining_year = 30 - age; # 13

print(final_score >= 70) # True

print(age > 18)