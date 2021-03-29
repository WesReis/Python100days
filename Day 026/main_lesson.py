numbers = [1, 2, 3]

# for loop
# new_numbers = []
# for n in numbers:
#     new_number = n+1
#     new_numbers.append(new_number)

# List comprehension:
# new_list = [new_item for item in list]

# new_numbers = [n+1 for n in numbers]
# print(numbers, new_numbers)

# Conditional list comprehension
# new_list = [new_item for item in list if test]

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)

# Dictionary comprehension
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
# import random
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_scores = {student: random.randint(1,100) for student in names}
# passed_students = {student:score for (student, score) in student_scores.items() if score > 60}

# Iterate over a Pandas DataFrame
import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key,val) in student_dict.items():
#     print(key)
#     print(val)

student_df = pd.DataFrame(student_dict)
# print(student_df)

# Loop through a data frame
# for (key, value) in student_df.items():
#     print(key)
#     print(value)

# Looping using Pandas method
for (index, row) in student_df.iterrows():
    # print(index)
    # print(row.student)
    # print(row.score)

