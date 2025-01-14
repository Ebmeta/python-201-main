# Convert a string to a tuple and print out the result.
# What do you see?
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?

string = "codingnomads"
tuple_str = tuple(string)
print(tuple_str , type(tuple_str))
for _ in tuple_str:
    print(_)