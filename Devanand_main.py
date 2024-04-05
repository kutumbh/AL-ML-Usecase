# driver code

from Devanand_function import Sport_json
from Devanand_function import get_values
from Devanand_function import remove_formatting
from Bollywood_prompts import questions
import pandas as pd
import google.generativeai as genai
import time
import json
import re
import numpy as np
GOOGLE_API_KEY = 'AIzaSyCn0J-flsHb4g4vlMtH953x23f8F-jFHtc'
 
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

# Call functions and access variables from the imported modules
if __name__ == "__main__":
    # Load the Excel file
    df = pd.read_excel('Category_Bollywood/Excel File/Bollywood_prompts.xlsx')
    print('Total rows: ',df.index)

    # for index in df.index:
        
    #Check if the value in the "srno" column is NaN
    if pd.isna(df['Srno'][0]):
        print("Srno:",'-')
    else:
        print("Srno:",df['Srno'][0])
    
    #name
    # Check if the value in the "Name" column is NaN
    if pd.isna(df['Name'][0]):
        print('Name of person: -')
    else:
        name_of_person=df['Name'][0]
        print('Name of person:',name_of_person)
    
    #Check if the value in the "category" column is NaN
    if pd.isna(df['Category'][0]):
        print('Category : -')
    else:
        category=df['Category'][0]
        print('Category :',category)
    
    #Check if the value in the "sub-category" column is NaN
    if pd.isna(df['SubCategory'][0]):
        print('SubCategory : -')
    else:
        SubCategory=df['SubCategory'][0]
        print('SubCategory :',SubCategory)
    
    #loop over list of questions
    for i, question in enumerate(questions, start=1):    
        # question=df['Prompt'][index]
        print('-'*30,'BEFORE CHANGING PROMPT NAME','-'*30)
        print(f'PROMPT {i}:{question}')
        print('-'*30,'AFTER CHANGING PROMPT NAME','-'*30)
        #Now I have a question , so inside that replace {} with name
        question1=question.replace('{}',f'{name_of_person}')
        print(f'PROMPT {i}:{question1}')
        print('-'*111)
        # takes prompts from excel
        response = model.generate_content(question1)
        time.sleep(10)
        plain_ouput=remove_formatting(response.text)
        print(plain_ouput)
        # time.sleep(4)
        sports=get_values(plain_ouput,Sport_json,name_of_person,category,SubCategory)
        time.sleep(4)
        print(sports)
        print('*'*111)
    

# Serialize the generated content to JSON
json_output = json.dumps(Sport_json, indent=4)

# # Write JSON output to a file
#category_Subcategory_NameOfPerson
# with open(f'Category_Bollywood/Json Files/{category}_{SubCategory}_{name_of_person}.json', 'w') as json_file:
#     json_file.write(json_output)

# print(f"json has been saved to '{category}_{SubCategory}_{name_of_person}.json'")
