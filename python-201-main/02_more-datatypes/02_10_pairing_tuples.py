# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.
# Write your code below here

from resources import randlist

list_ = randlist
print("input list",list_)
list_.sort()
print("sorted list",list_)
list_tuple_2 =[]
if len(list_) % 2 == 1:
    list_= list_+ [0]
for i in range(0, len(list_) +1, 2):
    pair = tuple(list_[i:i+2])
    print(pair)
    list_tuple_2.append(pair)


print(list_tuple_2)




