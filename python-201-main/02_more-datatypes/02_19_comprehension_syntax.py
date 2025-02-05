# Use a list comprehension to create a list that contains the individual
# letters of the word "codingnomads":
# ['c', 'o', 'd', 'i', 'n', 'g', 'n', 'o', 'm', 'a', 'd', 's']
#
# Note: You can solve this more quickly with a call to `list()`
# but try to do it using a list comprehension.

word = "codingnomads"
word_list_1 = list(word)
word_list_2 = [i for i in word]
print("word with list()             : ", word_list_1)
print("word with list comprehension : ", word_list_1)

