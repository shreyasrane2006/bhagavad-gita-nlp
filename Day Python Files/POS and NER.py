import nltk
import string
import collections
from nltk import sent_tokenize
from nltk import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk import ne_chunk

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

    lemma =  [
        word for word in tokens
        if word not in string.punctuation
        and word not in extra_punct
        and word.isalpha()
        and word.lower() not in custom_stopwords
    ]

    tags = pos_tag(lemma)
    #print(tags)
    
    def get_wordnet_pos(tag):
        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('V'):
            return wordnet.VERB
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN  # default

    lemmatized = [lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in tags]
    return lemmatized, tags


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

    #cleaned = clean_tokens(tokens, custom_stopwords=custom_stopwords)
    lemmatized, tagged = clean_tokens(tokens, custom_stopwords=custom_stopwords)
    print("Lemmatized Words (Sample):", lemmatized[:20])
    print("\nPOS Tagged Words (Sample):", tagged[:20])

    #print(cleaned)
    ner_tree = ne_chunk(tagged)
    print("\nNamed Entities:")
    for subtree in ner_tree:
        if hasattr(subtree, 'label'):
            print(f"{subtree.label()}: {' '.join(c[0] for c in subtree)}")

    # Step 5: Display results
    #print("Cleaned Words (Sample):", cleaned[:20])
    #print("Top 10 Words:", get_most_common_words(cleaned))


if __name__ == "__main__":
    main()
