
def say_hi ():
    print("Hello User")

print("Top")
say_hi()
print("Bottom")

# Function with parameter

def say_hi (name):
    print("Hello "+ name)

print("Top")
say_hi("Madjid")
print("Bottom")

# Function call with User input parameter
def say_hi (name, age):
    print("Hello "+ name + "!!. You are " + age + " years old. Have good life")
print("Top")
name = input("What is your name sir ? \n")
age = input("How old are you Mr. " + name + " ?\n")
say_hi(name, age)
print("Bottom")
