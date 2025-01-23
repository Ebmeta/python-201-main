# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually
from itertools import count

list_ = [1, 2, 3, 4, 3, 4, 5]
# 1. Convert to a different data type
list_1 = list(set(list_))
print("list 1 :" ,list_1)


# 2. Use a loop and a second list to solve it more manually
list_2=[]
for i in list_:
    if i not in list_2:
        list_2.append(i)

print("list 2 : ",list_2 )


