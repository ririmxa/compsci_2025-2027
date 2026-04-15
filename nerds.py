
# Implement a dictionary by typing dictionary name, using curly braces {}, and then adding KEYS and VALUES separated by a colon (:).
# Each key-value pair is separated by a comma.
# Example: my_dict = {"key1": "value1", "key2": "value2"}# Access values by referencing their keys inside square brackets [].
# Example: value = my_dict["key1"]
# Creating a dictionary
# {} for dictionaries, [] for lists
student_grades = {}
student_list = ["Myesha", "Julia", "Alicja", "Gwanho", "Oskar"]
subject_list = ["Math", "English", "Science"]
grades_list = [76, 87, 63, 88, 89, 67, 96, 99, 96, 97, 67, 78, 80, 91, 88]


student_grades = {}

index = 0
for student in student_list:
    student_grades = {}

index = 0  # tracks position in grades_list

for student in student_list:
    # assign 3 grades per student
    student_grades[student] = {
        subject_list[0]: grades_list[index],
        subject_list[1]: grades_list[index + 1],
        subject_list[2]: grades_list[index + 2]
    }
    index += 3

print(student_grades)
