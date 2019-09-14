from Student import Student

student1 = Student("Omar", "Engineer", 3.2, True)
student2 = Student("Said", "Management", 3.9, False)

print("Is " + student1.name + " honored ? : " + str(student1.on_honor_roll()))
print("Is " + student2.name + " honored ? : " + str(student2.on_honor_roll()))
