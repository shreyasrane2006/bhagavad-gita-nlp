from allennlp.predictors.predictor import Predictor
import allennlp_models.coref

predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2021.03.10.tar.gz")

with open("../Text Files/gita_intro.txt", 'r', encoding='utf-8') as file:
    text = ''.join(file.readlines())
#text = "Krishna gave Arjuna advice. He told him to fight."

result = predictor.predict(document=text)

# Print the clusters
print("Coreference Clusters:")
for cluster in result['clusters']:
    print([text[start:end+1] for start, end in cluster])
