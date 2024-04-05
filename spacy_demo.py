import spacy

def extract_entities(text):
    # Load the SpaCy English NER model
    nlp = spacy.load("en_core_web_sm")
    
    # Process the text with the NER model
    doc = nlp(text)
    
    # Initialize dictionaries to store entities of different types
    entities = {
        'person': [],
        'place': [],
        'organization': [],
        'date': [],
        'other': []
    }
    
    # Extract named entities and classify them into different types
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            entities['person'].append(ent.text)
        elif ent.label_ == 'GPE' or ent.label_ == 'LOC':
            entities['place'].append(ent.text)
        elif ent.label_ == 'ORG':
            entities['organization'].append(ent.text)
        elif ent.label_ == 'DATE':
            entities['date'].append(ent.text)
        else:
            entities['other'].append(ent.text)
    
    return entities

# Example usage
text = "Hi my name is chinmay kShirsagar an i was born in 2001 in Nagpur city and i work in Meghe GRoup how are you."
entities = extract_entities(text)

# Display the extracted entities
print("Persons:", entities['person'])
print("Places:", entities['place'])
print("Organizations:", entities['organization'])
print("Dates:", entities['date'])
print("Other:", entities['other'])
