# SET

# students = {"Kingsley", "Paul", "Charlses", "Peter", "Sammy"}

"""
python_class = { "Kingsley", "Paul", "Sammy" }
javascript_class = { "Charlse", "Peter", "Kingsley" }
attendance = set()

print(python_class.isdisjoint(javascript_class))

classes = frozenset("python_class", "javascript_class")

- Union
- intersection
- difference
- symmetric_difference
"""

# students = python_class.union(javascript_class)

# dual_students = python_class.intersection(javascript_class)

# NOTE: position matters

# 10 difference 3 = 7
#  { "Paul", "Sammy", "Kingsley" } difference { "Charlse", "Peter", "Kingsley" } = { "Paul", "Sammy" }

"""
# Symmetric_difference 
print(javascript_class.symmetric_difference(python_class))


print(javascript_class.difference(python_class))

# unique instance of a particular object/item

def sign_attendance(classes):
    for student in classes:
        attendance.add(student)

def print_attendance():
    for student in attendance:
        print(student)

def cancel_attendance(student_name):
    attendance.discard(student_name)

def clear_attendance():
    attendance.clear()

def pick_a_student():
    return attendance.pop()
    
sign_attendance(python_class)
sign_attendance(javascript_class)

cancel_attendance("Pascal")

picked_student = pick_a_student()

clear_attendance()

print(attendance)
"""
import copy;

students = [
    {"name": "Alice", "courses": ["Math", "Physics", "Chemistry"]},
    {"name": "Bob", "courses": ["Math", "Biology"]},
    {"name": "Charlie", "courses": ["Physics", "Chemistry"]},
    {"name": "David", "courses": ["Math", "Physics"]},
]


unique_courses = set()
course_offerred = {}

def analyze_students(students):
    for student in students:
        for course in student["courses"]:
            unique_courses.add(course)

            if course not in course_offerred.keys():
                course_offerred[course] = []
            
            course_offerred[course].append(student["name"])
        
    print(course_offerred)

analyze_students(students)
