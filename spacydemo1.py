import spacy
import json

# Load SpaCy English NER model
nlp = spacy.load("en_core_web_lg")

def extract_entities_spacy(text):
    doc = nlp(text)
    entities = {
        'persons': [],
        'places': [],
        'organizations': [],
        'sports': [],
        'others': []
    }
    
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            entities['persons'].append(ent.text)
        elif ent.label_ == 'GPE' or ent.label_ == 'LOC':
            entities['places'].append(ent.text)
        elif ent.label_ == 'ORG':
            entities['organizations'].append(ent.text)
        elif ent.label_ == 'SPORT':
            entities['sports'].append(ent.text)
        else:
            entities['others'].append(ent.text)
    
    return entities
# Read the text from a file
def read_text_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

# Example usage
file_path = 'TOI_06_11-04-2021.txt'
text = read_text_from_file(file_path)

# Extract entities using SpaCy
entities_spacy = extract_entities_spacy(text)
# Convert the results to JSON
spacy_json_data = json.dumps(entities_spacy, indent=4)

# Output the JSON data for SpaCy
print("Entities extracted using SpaCy:")
print(spacy_json_data)



# Write JSON data to files
with open('TOI_06_11-04-2021.json', 'w') as spacy_json_file:
    json.dump(entities_spacy, spacy_json_file, indent=4)