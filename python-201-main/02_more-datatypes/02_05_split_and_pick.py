# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

text = '''Now and then I think of when we were together
Like when you said you felt so happy you could die
Told myself that you were right for me
But felt so lonely in your company
But that was love and it's an ache I still remember

You can get addicted to a certain kind of sadness
Like resignation to the end, always the end
So when we found that we could not make sense
Well you said that we would still be friends
But I'll admit that I was glad that it was over

But you didn't have to cut me off
Make out like it never happened and that we were nothing 
And I don't even need your love
But you treat me like a stranger and that feels so rough
No you didn't have to stoop so low
Have your friends collect your records and then change your number
I guess that I don't need that though
Now you're just somebody that I used to know
Now you're just somebody that I used to know
Now you're just somebody that I used to know

Now and then I think of all the times you screwed me over
But had me believing it was always something that I'd done
And I don't wanna live that way
Reading into every word you say
You said that you could let it go
And I wouldn't catch you hung up on somebody that you used to know

But you didn't have to cut me off
Make out like it never happened and that we were nothing 
And I don't even need your love
But you treat me like a stranger and that feels so rough
No you didn't have to stoop so low
Have your friends collect your records and then change your number
I guess that I don't need that though
Now you're just somebody that I used to know
Somebody, I used to know
(Somebody) Now you're just somebody that I used to know
Somebody, I used to know
(Somebody) Now you're just somebody that I used to know
I used to know, that I used to know, I used to know somebody'''
import re
from collections import  Counter

text_list = re.split(r'[.,()\n ]+', text)
# print(text_list)
word_counts = Counter(text_list)
most_common_words = word_counts.most_common(5)
for word , count in most_common_words:
    print(f'word : {word} , {count} times')