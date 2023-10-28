# Exercise 1
# fruits = ["apple", "banana", "cherry", "date"]
# fruits.append("elderberry")
# fruits.remove("banana")
# fruits.sort()
# print(fruits)

#Exercise 2
# student = {"John Doe":{"age":25, "major":"Computer Science"}}
# student["John Doe"]["major"] = "Electrical Engineering"
# student["John Doe"]["year"] = "Senior"
# print (student)
# print (student.keys())
# print (student.values())

# Exercise 3
# books = [{"title":"Harry Potter", "author":"JK Rowling", "year":1980},
#          {"title":"I Feel Bad About My Neck", "author":"Nora Ephron", "year":2006},
#          {"title":"Broken glass", "author":"Alain Mabanckou", "year":2005}
#         ]
# # print (f"The title of the second book on the list is: {books[1]['title']}")
# # print (f"The year of the third book on the list is: {books[2]['year']}")

# for item in books:
#     print (f"Book {item['title']} was written by {item['author']}")

# Exercise 4
# Create a dictionary called courses where the keys are the names of courses (e.g., "math", "history", "chemistry") 
# and the values are lists of student names enrolled in each course
courses = {"math":["John"], "history":["John", "Mike"], "chemistry":["Paul", "Ringo"]}
# Add 5 students to "math"
courses["math"].extend(["Ringo", "Francesc", "Pau", "Abel"])
# Remove the third student from "history".
courses["history"].pop(1)
# Print out the students in "chemistry".
print (courses["chemistry"])
# Add a new course "physics" with a list of 4 students.
courses["physics"]=["Toni", "Joan", "Nuria", "Sergio"]