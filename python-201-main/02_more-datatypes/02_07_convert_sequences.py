# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.
from os import replace

string = "codingnomads"
# - Convert the string shown below into a tuple.
a_tuple = tuple(string)
print(a_tuple)
# - Convert the tuple into a list.
a_list = list(a_tuple)
print(a_list)
# - Change the `c` character in your list into a `k`
k_list = [i.replace('c', 'k') for i in a_list]
print(k_list)
# - Convert the list back into a tuple.
k_tuple = tuple(k_list)
print(k_tuple)