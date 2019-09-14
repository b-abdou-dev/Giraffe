

is_male = True
is_tall = True

if is_male:
    print("You are a male")
else:
    print("You are a female")


is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are a non tall female")

is_tall = True
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are a not male or not tall or both")

# elseif statement

is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and (is_tall):
    print("You are a short female")
else:
    print("You are either not male or not tall or both")

