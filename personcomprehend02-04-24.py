#!/usr/bin/env python
# coding: utf-8

# In[2]:


import boto3
import pandas as pd
import os


# In[3]:


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
        # Process text using Amazon Comprehend
        comprehend = boto3.client(service_name='comprehend', region_name='ap-south-1',aws_access_key_id='AKIAUG5QZ7LXGOCB3EZE',aws_secret_access_key='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')
        response = comprehend.detect_entities(Text=text, LanguageCode='en')
        entities = [entity['Text'] for entity in response['Entities'] if entity['Type'] == 'PERSON']
        
        # Create DataFrame
        df = pd.DataFrame(entities, columns=['PersonName'])
        df['Newspaper'] = newspaper_name
        df['Date'] = date
        df['Place'] = place
        df['Page'] = int(page_no)
        # Remove duplicate rows
        df = df.drop_duplicates()
    
    return df


# In[14]:


output_folder = 'output_CSV'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
newspaper_file_path = 'TOI_08-04-2001_NEW DELHI_4.txt'
result_df = process_newspaper_file(newspaper_file_path)
csv_file_path = os.path.join(output_folder, 'TOI_08-04-2001_NEW DELHI_4_Comprehend.csv')
result_df.to_csv(csv_file_path, index=False)
print("Entities data saved to:", csv_file_path)


# In[ ]:




