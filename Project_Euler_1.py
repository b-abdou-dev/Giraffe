
# Problem 1:

"""
 If we list all the natural numbers below 10 that are multiples of 3 or 5,
 we get 3, 5, 6 and 9. The sum of these multiples is 23.
 Find the sum of all the multiples of 3 or 5 below 1000.
 """
# Solution


multiple_three_and_five = 0
sum_multiple_three_and_five = 0


for i in range(1000):
   if i % 3 == 0 or i % 5 == 0:
    multiple_three_and_five = i
    sum_multiple_three_and_five = sum_multiple_three_and_five + multiple_three_and_five

print("The sum of all the multiples of 3 and 5 below 1000 is: " + str(sum_multiple_three_and_five))






"""

ans = 0
x = 1
y = 2
while ans < 4000000:
if x % 2 == 0:
    ans += x
x = y
y = x + y
print(ans)

"""