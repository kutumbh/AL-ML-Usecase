#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import boto3
import os


# In[2]:


client = boto3.client('comprehend',region_name='ap-south-1',aws_access_key_id='AKIAUG5QZ7LXGOCB3EZE',aws_secret_access_key='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')


# In[3]:


client


# In[4]:


def process_text(text):
    response = client.detect_entities(Text=text, LanguageCode='en')
    
    return response['Entities']


# In[5]:


# Function to process each newspaper file
def process_newspaper_file(file_path):
    # Extract newspaper name, page number, and date from the file name
    file_name = os.path.basename(file_path)
    newspaper_name, page_no, date = file_name.split('_')
    date = date.split('.')[0]  # Remove file extension
    
    # Read text from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        entities = process_text(text)
        df = pd.DataFrame(entities)
        df['Newspaper'] = newspaper_name
        df['Page'] = int(page_no)
        df['Date'] = date
        # Remove duplicate rows
        df = df.drop_duplicates()
    
        return df


# In[6]:


# Process all newspaper files in a directory
def process_newspaper_directory(directory):
    all_dfs = []
    for file_name in os.listdir(directory):
        if file_name.endswith('.txt'):
            file_path = os.path.join(directory, file_name)
            df = process_newspaper_file(file_path)
            all_dfs.append(df)
    if all_dfs:
        result_df = pd.concat(all_dfs, ignore_index=True)
        return result_df
    else:
        print("No text files found in the directory.")
        return None


# In[7]:


newspaper_file_path = 'TOI_03_04_2021_NEW_DELHI_8 Page Number.txt'


# In[8]:


result_df = process_newspaper_file(newspaper_file_path)


# In[ ]:


csv_file_path = 'TOI_03_04_2021_NEW_DELHI_8 Page Number.csv'
result_df.to_csv(csv_file_path, index=False)
print("Entities data saved to:", csv_file_path)


# In[ ]:




