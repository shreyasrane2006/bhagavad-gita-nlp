import nltk
import string
import collections
#nltk.download('punkt_tab')
from nltk import sent_tokenize
from nltk import word_tokenize
from collections import Counter


verse = "Krishna said: O Arjuna, why are you hesitating in this sacred moment of battle?"
#sentence = sent_tokenize(verse)
#print(sentence)

words = word_tokenize(verse)
print(words)

cleaned_words = [word for word in words if word not in string.punctuation]
print(cleaned_words)


with open("gita_intro.txt", "r") as file:
    lines = file.readlines()
    
list_lines = [word for word in lines]
#print(list_lines)

s = ''.join(word for word in list_lines)

words = word_tokenize(s)
#print(words)

extra_punct = {'--', '``', "''", "'s", "'t", '-', '“', '”', '’', '‘', '–'}
cleaned_words = [word.lower() for word in words if word not in string.punctuation
                 and word not in extra_punct and word.isalpha()]
print(cleaned_words)

counts = Counter(cleaned_words)
print(counts.most_common(10))

