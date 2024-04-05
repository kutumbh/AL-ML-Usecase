import pandas as pd
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
import json

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_person_entities_nltk(text):
    persons = []
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = word_tokenize(sentence)
        tagged = pos_tag(words)
        chunked = ne_chunk(tagged)
        for subtree in chunked:
            if isinstance(subtree, nltk.Tree) and subtree.label() == 'PERSON':
                persons.append(' '.join([token[0] for token in subtree]))
    return persons

def process_newspaper_file(file_path):
    # Extract newspaper name, page number, and date from the file name
    file_name = os.path.basename(file_path)
    parts = file_name.split('_')
    newspaper_name = parts[0]
    date = parts[1]
    place = parts[2]
    page_no = parts[3].split('.')[0]  # Remove file extension
    
    # Read text from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        # Process text using NLTK
        persons = extract_person_entities_nltk(text)
        
        # Create DataFrame
        df = pd.DataFrame(persons, columns=['PersonName'])
        df['Newspaper'] = newspaper_name
        df['Date'] = date
        df['Place'] = place
        df['Page'] = int(page_no)
        # Remove duplicate rows
        df = df.drop_duplicates()
    
    return df

# Folder to store the CSV file
output_folder = 'D:/pdftotxt/newspaper_Me/Output_CSV/TOI_10-04-2001'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

newspaper_file_path = 'TOI_10-04-2001_NEW DELHI_4.txt'
result_df = process_newspaper_file(newspaper_file_path)
csv_file_path = os.path.join(output_folder, 'TOI_10-04-2001_NEW DELHI_4.txt_nltk.csv')
result_df.to_csv(csv_file_path, index=False)
print("Person entities data saved to:", csv_file_path)