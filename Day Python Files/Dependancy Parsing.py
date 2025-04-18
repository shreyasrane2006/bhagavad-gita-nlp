import spacy
nlp = spacy.load("en_core_web_sm")
from spacy import displacy

# Load the text file
def load_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return ''.join(file.readlines())

text = load_text("../Text Files/gita_intro.txt")

doc = nlp(text)

for token in doc:
    print(f"{token.text:10} {token.dep_:10} --> {token.head.text}")

displacy.serve(doc, style="dep")
