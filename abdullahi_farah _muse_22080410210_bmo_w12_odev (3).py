#ı  Create here a dictionary and put in  sinav_resulttable 
sinav_result = {
    "Name": ['Ayşe K.', 'Ahmet M', 'Nuri C', 'Nawar T.', 'Suzan T.', 'Ala B.'],
    "Gender": ['F', 'M', 'M', 'M', 'F', 'F'],
    "Midterm": [80, 60, 77, 25, 36, 75],
    "Final": [90, 50, 53, 100, 98, 66],
}

# functıons here
def save_passing_grade(sinav_result):
  sinav_result["Pass Grade"] = []
  # Calculate and save the passing grade for each student
  for i in range(len(sinav_result["Name"])):
    midterm = sinav_result["Midterm"][i]
    final = sinav_result["Final"][i]
    pass_grade = (midterm * 0.3) + (final * 0.7)
    sinav_result["Pass Grade"].append(pass_grade)

# Calculating the records
save_passing_grade(sinav_result)

# we regestreted 2 students here
for i in range(2):
  name = input("Enter the student's name: ")
  gender = input("Enter the student's gender: ")
  midterm = int(input("Enter the student's midterm grade: "))
  final = int(input("Enter the student's final grade: "))
  # Add the new record to the sinav_result dictionary
  sinav_result["Name"].append(name)
  sinav_result["Gender"].append(gender)
  sinav_result["Midterm"].append(midterm)
  sinav_result["Final"].append(final)

save_passing_grade(sinav_result)
# Print the updated table to the screen


print(sinav_result)


