import textwrap
import google.generativeai as genai
import time
import json
import re

generated_content={
    'id':'',
    'category':'Sports',
    'name':'Virat Kholi',
    'details':{
        'prompts':{
            '1':{
                'title':'',
                'introduction':'',
                'date':'',
                'description':'',
                'imgURL':''
            },
            '2':{
                'Birth':{
                    'title':'',
                    'introduction':'',
                    'date':'',
                    'description':'',
                    'imgURL':''
                },
                'Family_and_education':{
                    'title':'',
                    'introduction':'',
                    'date':'',
                    'description':'',
                    'imgURL':''
                }
            }
        }
    }
}

GOOGLE_API_KEY = 'AIzaSyCn0J-flsHb4g4vlMtH953x23f8F-jFHtc'
 
genai.configure(api_key=GOOGLE_API_KEY)
 
questions = [
    "Provide a title and introduction of Virat Kohli with pics",
    "Provide following details of Virat Kohli - Birth date and place of birth, family tree, early education, how family and education values shaped later achievements",
    "Provide following details of Virat Kohli - Initiation into cricket, debut in domestic cricket, debut in international cricket",
    "Provide following details of Virat Kohli- key achievements and statistics",
    "Provide following details of Virat Kohli - awards and felicitations",
    "Provide following details of Virat Kohli- anecdotes and controversies.",
    "Provide key personality attributes of Virat Kohli",
    "Provide contribution of Virat Kohli to society and philanthropy",
    "Provide the following details about Virat Kohli - famous quotes, what do colleagues say",
    "What is the current status of Virat Kohli"
]
 
model = genai.GenerativeModel('gemini-pro')
 
#function to extract title
def extract_title(response):
    title_pattern=r"\*\*Title:\*\* (.+?)\n"
    title_match=re.search(title_pattern,response)

    if title_match:
        title=title_match.group(1).strip()
    else:
        title=''

    return title

#function to extract introduction
def extract_intro(response):
    intro_pattern=r"\*\*Introduction:\*\*\s*([\s\S]*?)(?=\n{2}|$)"
    intro_match=re.search(intro_pattern,response)

    if intro_match:
        intro=intro_match.group(1).strip()
    else:
        intro=''
    return intro

#function to extract date
def extract_date(response):
    date_pattern=r"(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}"
    date_match=re.findall(date_pattern,response)

    if date_match:
        #there can be multiple dates
        for date in date_match:
            date1=date
    else:
        date1=''
    return date1

# def extract_description(response):

for i, question in enumerate(questions,start=1):
    response = model.generate_content(question)
    print(response.text)
    
    if 'Birth' in generated_content['details']['prompts'][str(i)]:
        generated_content['details']['prompts'][str(i)]['Birth']={
            'title':extract_title(response.text),
            'introduction':extract_intro(response.text),
            'date':extract_date(response.text),
            'description':'',

        }
        
    
    else:
        generated_content['details']['prompts'][str(i)]={
            'title':extract_title(response.text),
            'introduction':extract_intro(response.text),
            'date':extract_date(response.text),
            'description':'',

        }
     
    print(generated_content)
    print('*'*30)
    break
    time.sleep(4)


