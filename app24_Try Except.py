
# if not number was entered the program will through an error
# To handle the issue use try except block

# Method 1  (trial)

try:
    try:
         value = 10 / 0
    except:
        print("Dividing by zero is not valid")
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")


# Method 2

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Dividing by zero is not valid")
except ValueError:
    print("Invalid Input")

# Method 3: store error as variable

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as ZeroError:
    print(ZeroError)
except ValueError:
    print("Invalid Input")