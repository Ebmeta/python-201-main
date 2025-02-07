# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.
file_1 = open('words.txt', 'r')
file_2 = open('words_reverse.txt', 'w')
contents = file_1.read().split()

words_reverse = [word[::-1] for word in contents]
# print(words_reverse[0:3])
text_words_reverse = '\n'.join(words_reverse)
file_2.write(text_words_reverse)

file_1.close()
file_2.close()

