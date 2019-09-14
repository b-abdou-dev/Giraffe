

from Student import Student

student1 = Student("Omar", "Engineer", 3.4, True)
student2 = Student("Said", "Management", 2.9, False)

print(student1.name + " has got " + str(student1.gpa) + " in " + student1.major +
      " major, his probation status is " + str(student1.is_on_probation))

print(student2.name + " has got " + str(student2.gpa) + " in " + student2.major +
      " major, his probation status is " + str(student2.is_on_probation))
