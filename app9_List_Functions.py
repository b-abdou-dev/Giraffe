
lucky_numbers = [4, 25, 8, 16, 24, 37]

friends = ["Hacene", "Slimane", "Salah", "Moukhtar", "Alaa", "Slimane"]

friends.extend(lucky_numbers)
print(friends)

friends = friends[0:5]
print(friends)

friends.append("Djamel")
print(friends)

friends = friends[0:5]
print(friends)

friends.insert(2,"Idriss")
print(friends)

friends.remove("Salah")
print(friends)

friends.pop()
print(friends)



# To check if an element exist in the list
print(friends.index("Idriss"))

friends.append("Idriss")
# To count number of an repeated element

print(friends.count("Idriss"))

# Sorting in ascending order or alphabetical order
friends.sort()
lucky_numbers.sort()
print(friends)
print(lucky_numbers)

# Reverse a list
lucky_numbers.reverse()
print(lucky_numbers)

# Copy a list to another list
friends2 = friends.copy()
print(friends2)

# To clear the list
friends.clear()
print(friends)
    # Or
friends = friends[:]
print(friends)