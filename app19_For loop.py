for letter in "Giraffe Academy":
    print(letter)

brothers = ["Hocine", "Mouad", "Idriss"]
for brother in brothers:
    print(brother)

for index in range(12):
    print(index)

for index in range(3, 10):
    print(index)

for index in range(len(brothers)):
    print(brothers[index])

for index in range(4):
    if index == 0:
        print("first iteration")
    elif index == 1:
        print("second iteration")
    elif index == 2:
        print("third iteration")
    else:
        print("fourth iteration")

print("Last index is: " + str(index))