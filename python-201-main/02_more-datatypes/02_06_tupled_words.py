# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

# str_= input(" Typing some words:")
str_= "hello world"
list_ = str_.split()
result_list= [tuple(i) for i in list_]


print(result_list)