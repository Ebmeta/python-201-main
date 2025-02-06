# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

file_in = open('words.txt' , 'r')
contents = file_in.read()
# print(type(contents))
list_ = contents.split()
# print(list_)
for word in list_:
    if len(word) > 20:
        print(word)

file_in.close()
