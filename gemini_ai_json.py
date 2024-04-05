import json
import textwrap
import google.generativeai as genai

def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ')

# Configure the GenerativeAI library with your API key
GOOGLE_API_KEY = 'AIzaSyCn0J-flsHb4g4vlMtH953x23f8F-jFHtc'
genai.configure(api_key=GOOGLE_API_KEY)

# Dictionary to store generated content
generated_content = {
    "_id": "ObjectId",  
    "category": "Sports",  # Change the category as needed
    "name": "Virat Kohli",  # Change the name as needed
    "details": {
        "prompts": {}
    }
}

# List of questions about Virat Kohli
questions = [
    "Provide a title and introduction of Virat Kohli ",
    "Provide following details of Virat Kohli - Birth date and place of birth, family tree, early education, how family and education values shaped later achievements ",
    "Provide following details of Virat Kohli - Initiation into cricket, debut in domestic cricket, debut in international cricket",
    "Provide following details of Virat Kohli- key achievements and statistics ",
    "Provide following details of Virat Kohli - awards and felicitations ",
    "Provide following details of Virat Kohli- anecdotes and controversies .",
    "Provide key personality attributes of Virat Kohli",
    "Provide contribution of Virat Kohli to society and philanthropy ",
    "Provide the following details about Virat Kohli - famous quotes, what do colleagues say ",
    "What is the current status of Virat Kohli "
]

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

# Generate content for each question
for i, question in enumerate(questions, start=1):
    response = model.generate_content(question)
    print(response.text)
    print('*'*30)
    
    # generated_content["details"]["prompts"][str(i)] = {
    #     "title": f"Title for Prompt {i}",
    #     "introduction": to_markdown(response.text),
    #     "date": "",  # Add the date if needed
    #     "description": "",  # Add description if needed
        # "imgURL": f"S3::assets/{generated_content['category']}/{generated_content['name']}/profileName.png"
    # }

# Serialize the generated content to JSON
json_output = json.dumps(generated_content, indent=4)

# Write JSON output to a file
with open('generated_content.json', 'w') as json_file:
    json_file.write(json_output)

print("Generated content has been saved to 'generated_content.json'")
