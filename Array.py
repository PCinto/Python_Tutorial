courses = ["MIT", "Cybersecurity", "Data Science"]
print(courses)
#Accessing an element in array
print(courses[2])

#Adding an element in an Array
courses.append("Android Development")
print(courses)

#Removing an element in an Array
courses.remove(courses[0])
print(courses)


"""
Looping through an Array 
"""

for course in courses:
    print(course)