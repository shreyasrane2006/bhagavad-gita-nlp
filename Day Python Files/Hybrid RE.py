import spacy
from transformers import pipeline
import re

# Load SpaCy Model
nlp = spacy.load('en_core_web_sm')

# Load Hugging Face Relation Extraction pipeline
re_pipeline = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Function to process the text
def process_text(text):
    # Use spaCy NLP pipeline
    doc = nlp(text)
    
    # Step 1: Named Entity Recognition (NER)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Step 2: Dependency Parsing (get relations between entities)
    relations = []
    for token in doc:
        # You can modify these patterns based on your text
        if token.dep_ == "nsubj" and token.head.pos_ == "VERB":
            subject = token
            verb = token.head
            for child in verb.children:
                if child.dep_ == "dobj":
                    object_ = child
                    relations.append((subject.text, verb.text, object_.text))
    
    # Step 3: Apply Rule-Based Relation Extraction (optional)
    print("Entities found:", entities)
    print("Relations found (via spaCy):", relations)
    
    # Step 4: Apply Hugging Face Relation Extraction model (use zero-shot classification)
    for rel in relations:
        subject, verb, obj = rel
        hypothesis = f"{subject} {verb} {obj}"
        classification = re_pipeline(hypothesis, candidate_labels=["religion", "war", "teaching", "devotion"])
        print(f"\nRelation extracted: {hypothesis}")
        print(f"Relation category: {classification['labels'][0]}")

# Example text from Bhagavad Gita
#text = "Krishna taught Arjuna about the nature of life and the self in the battlefield."
with open("../Text Files/gita_intro.txt", 'r', encoding="utf-8") as file:
     text = ''.join(file.readlines())
# Call the function
process_text(text)
