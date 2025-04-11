import nltk
import string
import collections
from nltk import sent_tokenize
from nltk import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Load the text file
def load_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return ''.join(file.readlines())


# Tokenize the text
def tokenize(text):
    return word_tokenize(text)


# Clean and lemmatize tokens
def clean_tokens(tokens, extra_punct=None, custom_stopwords=None):
    if extra_punct is None:
        extra_punct = {'--', '``', "''", "'s", "'t", '-', '“', '”', '’', '‘', '–'}
    if custom_stopwords is None:
        custom_stopwords = set()

    lemmatizer = WordNetLemmatizer()
    return [
        lemmatizer.lemmatize(word.lower())
        for word in tokens
        if word not in string.punctuation
        and word not in extra_punct
        and word.isalpha()
        and word.lower() not in custom_stopwords
    ]


# Count word frequencies
def get_most_common_words(words, n=10):
    counts = Counter(words)
    return counts.most_common(n)


def main():
    # Step 1: Load text
    text = load_text("gita_intro.txt")    

    # Step 2: Tokenize
    tokens = tokenize(text)

    # Step 3: Define custom stopwords (Hindi example)
    #hindi_stopwords = {'और', 'का', 'है', 'में', 'कि', 'से', 'को', 'पर', 'था', 'थी'}

    custom_stopwords = set(stopwords.words('english'))

    # Step 4: Clean + Lemmatize

    cleaned = clean_tokens(tokens, custom_stopwords=custom_stopwords)
    

    # Step 5: Display results
    print("Cleaned Words (Sample):", cleaned[:20])
    print("Top 10 Words:", get_most_common_words(cleaned))


if __name__ == "__main__":
    main()
