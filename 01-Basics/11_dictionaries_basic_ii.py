# *** Here, we're going to learn about list of dictionaries

# student1 = {'name': 'Sika', 'cgpa': 3.9}
# student2 = {'name': 'Sayad', 'cgpa': 3.9}
# student3 = {'name': 'Tanjim', 'cgpa': 2.9}

# students = [student1, student2, student3]

# for student in students:
#     print(student)


# * List in dictionary:

oldStudent = {'name': 'Sayad IKA', 'cgpa': 3.9, "completed_course": []}

oldStudent.get('completed_course').append('CSE3101')
oldStudent.get('completed_course').append('CSE3102')
oldStudent.get('completed_course').append('CSE3201')
oldStudent.get('completed_course').append('CSE3202')

# print(oldStudent)
# for course in oldStudent['completed_course']:
#     print(course)

# ** Last but not least "A dictionary in a dictionary":

# friends = {
#     'Momin': {
#         'first_name': 'Momen',
#         'last_name': 'Ahmed',
#     },
#     'Siyam':    {
#         'first_name': 'Siyam',
#         'last_name': "Digonto",
#     }
# }

# print(friends)