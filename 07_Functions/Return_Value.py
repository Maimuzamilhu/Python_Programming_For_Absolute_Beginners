def Age_Calculator(Date_of_birth):
    age = 2023 - Date_of_birth.year
    return age

from datetime import datetime

dob = datetime(2002, 8, 22)  # Replace with the actual date of birth
age = Age_Calculator(dob)
print(age)
