import spacy
import csv
import os

# Load SpaCy English NER model
nlp = spacy.load("en_core_web_sm")

# Define the categories of news
news_categories = {
    'entertainment': ['entertainment', 'movie', 'film', 'music', 'celebrity'],
    'politics': ['politics', 'government', 'election', 'democracy'],
    'fashion': ['fashion', 'style', 'clothing', 'designer'],
    'war': ['war', 'conflict', 'battle', 'combat'],
    'government': ['government', 'administration', 'public policy'],
    'environment': ['environment', 'nature', 'climate', 'sustainability'],
    'education': ['education', 'school', 'university', 'learning'],
    'health': ['health', 'wellness', 'medical', 'fitness'],
    'economy': ['economy', 'finance', 'business', 'market'],
    'business': ['business', 'company', 'enterprise', 'commerce'],
    'sport': ['sport', 'athlete', 'competition', 'game']
}

def extract_entities_spacy(text):
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
    return entities

def categorize_entities(entities, text):
    categorized_entities = []
    
    for entity in entities:
        category = find_category(entity, text)
        if category:
            categorized_entities.append({'name': entity, 'category': category})
                
    return categorized_entities

def find_category(entity, text):
    # Search for keywords associated with each news category in the context of the entity
    for category, category_keywords in news_categories.items():
        for keyword in category_keywords:
            if keyword in text.lower():
                return category
    
    return None

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def write_to_csv(file_name, data):
    with open(file_name + '.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Example usage
file_path = 'TOI_18_05.txt'
text = read_text_from_file(file_path)

# Extract entities using SpaCy
entities_spacy = extract_entities_spacy(text)

# Categorize entities
categorized_entities = categorize_entities(entities_spacy, text)

# Print names along with the corresponding news categories
print("Names extracted from the newspaper text and their corresponding news categories:")
for entity in categorized_entities:
    print(f"Name: {entity['name']}, Category: {entity['category']}")

# Write data to a CSV file
write_to_csv(os.path.splitext(file_path)[0], categorized_entities)
