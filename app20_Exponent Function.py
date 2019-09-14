# direct way
print(2**3)


# using a function    my try

def power_operation(number, exponent):
    i = 1
    result = 1
    for i in range(exponent):
        result = result * number
    print(str(number) + " to the power " + str(exponent) + " = " + str(result) + " \n")

power_operation(2, 3)

# Other solution

def power_operation2(number, exponent):
    result = 1
    for index in range(exponent):
        result = result * number
    return result

print(power_operation2(3, 3))