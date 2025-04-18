import nltk
import string
import collections
import csv
import matplotlib.pyplot as plt
from nltk import sent_tokenize
from nltk import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk import ne_chunk
from nltk import FreqDist
from wordcloud import WordCloud
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.tree import Tree
from nltk.corpus import stopwords



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

    return lemma

def export_to_csv(lemma, filename='gita.csv'):
    lemmatizer = WordNetLemmatizer()

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

    lemmatized = [(word, tag, lemmatizer.lemmatize(word, get_wordnet_pos(tag)))
                  for word, tag in tags
                  if word.isalpha()
                  ]
    #return lemmatized, tags
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Word", "POS", 'Lemma'])
        writer.writerows(lemmatized)

    print(f"CSV saved as {filename}")

# Count word frequencies
def get_most_common_words(words, n=10):
    counts = Counter(words)
    return counts.most_common(n)


def plot_pos_distribution(tokens):
    pos_tags = [tag for word, tag in pos_tag(tokens) if word.isalpha()]
    counter = Counter(pos_tags)
    tags, counts = zip(*counter.items())

    plt.figure(figsize=(10, 6))
    plt.bar(tags, counts, color='skyblue')
    plt.title("POS Tag Distribution")
    plt.xlabel("POS Tags")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def extract_named_entities(text):
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    tree = ne_chunk(pos_tags, binary=False)

    named_entities = []

    for subtree in tree:
        if isinstance(subtree, Tree):
            entity_name = " ".join([token for token, pos in subtree.leaves()])
            entity_type = subtree.label()
            named_entities.append((entity_name, entity_type))
    return named_entities



# Main function to extract bigrams with PMI
def find_top_pmi_bigrams(words, top_n=20):
    
    # Step 1: Create bigram finder from word list
    bigram_finder = BigramCollocationFinder.from_words(words)
        
    # Step 2: Apply frequency filter (optional)
    bigram_finder.apply_freq_filter(2)  # Ignore bigrams with freq < 2
    
    # Step 3: Score bigrams by PMI
    scored = bigram_finder.score_ngrams(BigramAssocMeasures.pmi)
    print(scored)

    # Step 4: Print top N bigrams
    print(f"\nTop {top_n} Bigrams by PMI:\n")
    for bigram, score in scored: #[:top_n]:
        print(f"{bigram[0]} {bigram[1]} — PMI Score: {round(score, 2)}")

    

def main():
    # Step 1: Load text
    text = load_text("../Text Files/gita_intro.txt")    

    # Step 2: Tokenize
    tokens = tokenize(text)
    #print(tokens)

    ner = extract_named_entities(text)
    print(ner)
    #fdist = FreqDist(tokens)
    #print(tokens)
    #print(fdist["Krishna"])
    #print(fdist.most_common())
    #words, counts = zip(*fdist.most_common(20))  # Unpack top 20 into words and counts
    #plt.bar(words, counts)  # Create a bar chart
    #plt.show()
    #text = " ".join(words)  # Combine all words into one big string
    #wc = WordCloud().generate(text)

    #plt.imshow(wc, interpolation='bilinear')
    #plt.axis("off")
    #plt.show()
    
    # Step 3: Define custom stopwords (Hindi example)
    #hindi_stopwords = {'और', 'का', 'है', 'में', 'कि', 'से', 'को', 'पर', 'था', 'थी'}

    #custom_stopwords = set(stopwords.words('english'))

    # Step 4: Clean + Lemmatize

    #tokens = clean_tokens(tokens, custom_stopwords=custom_stopwords)

    #find_top_pmi_bigrams(tokens)
    #lemmatized, tagged = clean_tokens(tokens, custom_stopwords=custom_stopwords)
    #print("Lemmatized Words (Sample):", lemmatized[:20])
    #print("\nPOS Tagged Words (Sample):", tagged[:20])

    #export_to_csv(tokens)

    #plot_pos_distribution(tokens)
    # Step 5: Display results
    #print("Cleaned Words (Sample):", cleaned[:20])
    #print("Top 10 Words:", get_most_common_words(cleaned))


if __name__ == "__main__":
    main()
