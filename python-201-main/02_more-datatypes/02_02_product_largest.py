# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist
from functools import reduce
from operator import mul

num = randlist
print(f"You have a list of numbers: {randlist}")
max_num = max(num)
print(f'The largest number is : {max_num}')
# res = reduce(mul, randlist)
res = 1
for i in num:
    res *= i

print(f"The product of all of the numbers in the list : {res}")