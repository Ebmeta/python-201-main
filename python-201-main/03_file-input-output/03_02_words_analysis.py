# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.
file_in = open("words.txt" , 'r')
contents = file_in.read().split()
min_word = len(min(contents, key = len))
max_word = len(max(contents ,key = len))
shortest_word =[]
longest_word = []
for word in contents:
    if len(word) == min_word:
        shortest_word.append(word)
    elif len(word) == max_word:
        longest_word.append(word)


print("The shortest word in the file : " , shortest_word)
print("The longest word in the file : " , longest_word)
print("The total number of words in the file = ", len(contents))





file_in.close()
