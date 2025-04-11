import nltk
import string
import collections
#nltk.download('punkt_tab')
from nltk import sent_tokenize
from nltk import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

#verse = "Krishna said: O Arjuna, why are you hesitating in this sacred moment of battle?"
#sentence = sent_tokenize(verse)
#print(sentence)

#words = word_tokenize(verse)
#print(words)

#cleaned_words = [word for word in words if word not in string.punctuation]
#print(cleaned_words)


with open("gita_intro.txt", "r") as file:
    lines = file.readlines()
    
list_lines = [word for word in lines]

s = ''.join(word for word in list_lines)

words = word_tokenize(s)

extra_punct = {'--', '``', "''", "'s", "'t", '-', '“', '”', '’', '‘', '–'}
cleaned_words = [word.lower() for word in words if word not in string.punctuation
                 and word not in extra_punct and word.isalpha()]
#print(cleaned_words)

counts = Counter(cleaned_words)
#print(counts.most_common(10))

stop_words = set(stopwords.words('english'))

filtered_words = [word for word in cleaned_words if word not in stop_words]

counts = Counter(filtered_words)
#print(counts.most_common(10))

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

print(lemmatized_words)
