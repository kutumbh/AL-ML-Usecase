import google.generativeai as genai
import time
import json
import re

GOOGLE_API_KEY = 'AIzaSyCn0J-flsHb4g4vlMtH953x23f8F-jFHtc'
 
genai.configure(api_key=GOOGLE_API_KEY)
 
questions = [
    "Provide a title of Dev Anand with heading as 'Title:' and Introduction of 7 lines with exact heading as 'Introduction:' ",
    "Provide following details of Dev Anand - Birth date with exact heading as 'Birth date:' and place of birth with exact heading as 'place of birth', Fathers name with exact heading 'Father's name:',mothers name with exact heading 'Mothers name:',brother name with exact heading as 'brothers name:' , sisters name with exact heading as 'sisters name:', early education with exact heading as 'Early education:', Family values with exact heading as 'family values:' ,education values  with exact heading only as 'Education values:', Marriage details with exact heading as 'Marriage details:'",
    "Provide following details of Dev Anand - a chronological timeline for key events, showcasing career journey with exact heading 'carrer Journey:', professional struggle with exact heading 'professional struggle:', key achievements with exact heading 'key achievements', and contributions to the film industry with exact heading 'contrubution to film Industry:' ",
    "Provide following details of Dev Anand - prestigious awards and recognitions with exact heading 'Awards and recognitions:' ",
    "Provide following details of Dev Anand- anecdotes with exact heading 'Anecdots:' and controversies with exact heading 'Controversies:' in 6-7 short points .",
    "Provide key personality attributes of Dev Anand with exact heading 'Personality Attributes:' 10 points ",
    "Provide contribution of Dev Anand to society with exact heading 'society:' and philanthropy with exact heading 'philanthropy:' 8 points each",
    "Provide the following details about Dev Anand - famous quotes with exact heading 'Famous quotes:', what do colleagues say with exact heading as 'Thoughts:' 7 points each",
    "What is the current status of Dev Anand - with exact heading 'Current Status:' with 8 points  ",
    # "Give life story images for Dev Anand with heading 'Life story images:'"
]

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

#json format
Sport_json={
    'id':'',
    'Catergory':'Bollywood',
    'name':'Devanand',
    'title':{
        'title':'',
        'Introduction':'',
        # 'Image':''
    },
    'birth details':{
        'birth date':'',
        'place':'',
        'family tree':{
            'father':'',
            'mother':'',
            'brother':'',
            'sister':''
        },
        'early education':'',
        'family values':'',
        'education values':'',
        'marriage':'' 
        # 'Images':''
    },
    'key events':{
        'carrer journey':'',
        'professional struggle':'',
        'achievements':'',
        'contribution to film industry':''
        # 'Images':''
    },
    'awards':{
        'awards and recognition':'',
        
    },
    'anecdots':{
        'anecdots':'',
        'controversies':''
    },
    'personality attributes':'',
    'contribution':{
        'society':'',
        'phianthropy':''
    },
    'other details':{
        'famous quotes':'',
        'colleagues thoughts':''
    },
    'current status':'',
    # 'Life Story Images':''   
}


#function to fetch values from response
def get_values(response,sports_json):
    time.sleep(4)
    #tite and introduction
    if response.__contains__('Title') or response.__contains__('Title:') :
        #title
        time.sleep(2)
        title=response.split('\n')[0]
        if 'Title' in title or 'title' in title:
            title1=title.split('Title:')[1]
            print('title11',title1)
            sports_json['title']['title']=title1
        elif 'Title' not in title or 'title' not in title:
            title1=title
            print('title22',title1)
            sports_json['title']['title']=title1
        #introduction
        time.sleep(2)
        introduction_pattern = r"Introduction:(.*?)(?=Images:|$)"
        match = re.search(introduction_pattern, response, re.DOTALL)
        if match:
            introduction = match.group(1).strip()
            # Remove any text within square brackets
            introduction = re.sub(r"\[.*?\]", "", introduction)
            # Remove extra whitespace
            introduction = " ".join(introduction.split())
            
        else:
            introduction=''

        sports_json['title']['Introduction']=introduction



    #birth details
    if response.__contains__('Birth') or response.__contains__('Birth:'):
        #List of birth details
        list_birth_details=response.split('\n')
        print("list---->",list_birth_details)
        
        #birth date
        birth_date=list_birth_details[0].split(':')[1]
        sports_json['birth details']['birth date']=birth_date
        #place of birth
        place=list_birth_details[1].split(':')[1]
        sports_json['birth details']['place']=place
        #fathers name
        father=list_birth_details[2].split(':')[1]
        sports_json['birth details']['family tree']['father']=father
        #mother name
        mother=list_birth_details[3].split(':')[1]
        sports_json['birth details']['family tree']['mother']=mother
        #brother and sister
        brother=list_birth_details[4].split(':')[1]
        sports_json['birth details']['family tree']['brother']=brother
        sister=list_birth_details[5].split(':')[1]
        sports_json['birth details']['family tree']['sister']=sister

        #family values
        time.sleep(4)
        value_details=''
        capture_value = False
        for line in list_birth_details:
            time.sleep(2)
            if 'Family values:' in line :
                capture_value = True
                value_details += line.split('Family values:')[1]
            elif 'Family values' in line :
                capture_value = True
                value_details += line.split('Family values')[1]
            elif 'Marriage details:' in line or 'Marriage details' in line:
                capture_value = False
            elif capture_value and line != 'Family values:':
                value_details += line.strip() + ', '
            sports_json['birth details']['family values']=value_details

        # marriage
        time.sleep(4)
        marriage_details=''
        capture_marriage = False
        for line in list_birth_details:
            time.sleep(2)
            if 'Marriage details:' in line :
                capture_marriage = True
                marriage_details += line.split('Marriage details:')[1]
            elif 'Marriage details' in line :
                capture_marriage = True
                marriage_details += line.split('Marriage details')[1]
            elif capture_marriage and line != 'Marriage details:':
               marriage_details += line.strip() + ', '
            sports_json['birth details']['marriage']=marriage_details
        #education values
        time.sleep(4)
        education_values_details = ''
        capture_education_values = False
        for line in list_birth_details:
            time.sleep(2)
            if 'Education values:' in line :
                capture_education_values = True
                education_values_details+=line.split('Education values:')[1]
                # print("----------------early------------------ 1111",education_values_details)
            elif 'Education values' in line :
                capture_education_values = True
                education_values_details+=line.split('Education values')[1]
            elif 'Marriage details:' in line or 'Marriage details' in line:
                capture_education_values = False
            elif capture_education_values and 'Education values:' not in line:
                education_values_details+=line.strip() + ', '
                # print("----------------early------------------2222",education_values_details)
            sports_json['birth details']['education values']=education_values_details

        #early education
        time.sleep(4)
        early_education_details = ''
        capture_education = False
        for line in list_birth_details:
            time.sleep(2)
            if 'Early education:' in line :
                capture_education = True
                early_education_details+=line.split('Early education:')[1]
                print("----------------early------------------ 1111",early_education_details)
            elif 'Early education' in line :
                capture_education = True
                early_education_details+=line.split('Early education')[1]
            elif 'Family values:' in line or 'Family values' in line:
                capture_education = False
            elif capture_education and 'Early education:' not in line:
                early_education_details+=line.strip() + ', '
                print("----------------early------------------2222",early_education_details)
            sports_json['birth details']['early education']=early_education_details


    #key events
    if   response.__contains__('Career Journey') or response.__contains__('Career Journey:'):
        
        time.sleep(4)
        #Career_Journey
        Career_Journey_details=''
        capture_Career_Journey=False
        lines=response.split('\n')
        for line in lines:
            time.sleep(2)
            
            if line.__contains__("Career Journey:") :
                capture_Career_Journey = True
                Career_Journey_details+=line.split('Career Journey:')[1]
            elif line.__contains__("Career Journey") :
                capture_Career_Journey = True
                Career_Journey_details+=line.split('Career Journey')[1]
            
            elif "Professional Struggle:" in line or "Professional Struggle" in line:
                capture_Career_Journey = False
            # If capture_Career_Journey is True, add the line to the Career_Journey_details
            elif capture_Career_Journey and line.strip():
                Career_Journey_details+=line.strip() + ', '
            sports_json['key events']['carrer journey']=Career_Journey_details
        #Professional Struggle
        time.sleep(4)
        Professional_Struggle_details=''
        capture_Professional_Struggle=False
        lines=response.split('\n')
        for line in lines:
            time.sleep(2)
            if line.__contains__("Professional Struggle:") :
                capture_Professional_Struggle = True
                Professional_Struggle_details+=line.split('Professional Struggle:')[1]
            elif line.__contains__("Professional Struggle") :
                capture_Professional_Struggle = True
                Professional_Struggle_details+=line.split('Professional Struggle')[1]
            elif line.__contains__("Professional Struggles:") :
                capture_Professional_Struggle = True
                Professional_Struggle_details+=line.split('Professional Struggles:')[1]
            elif line.__contains__("Professional Struggles") :
                capture_Professional_Struggle = True
                Professional_Struggle_details+=line.split('Professional Struggles')[1]
            elif  "Key Achievements:" in line or "Key Achievements" in line:
                capture_Professional_Struggle = False
            # If capture_Professional_Struggle is True, add the line to the domestic details
            elif capture_Professional_Struggle and line.strip():
                Professional_Struggle_details+=line.strip() + ', '
            sports_json['key events']['professional struggle']=Professional_Struggle_details
        #Key Achievements
        time.sleep(4)
        Key_Achievements_details1=''
        capture_Key_Achievements=False
        lines=response.split('\n')
        for line in lines:
            time.sleep(2)
            if line.__contains__("Key Achievements:") :
                capture_Key_Achievements = True
                Key_Achievements_details1+=line.split('Key Achievements:')[1]
            elif line.__contains__("Key Achievements") :
                capture_Key_Achievements = True
                Key_Achievements_details1+=line.split('Key Achievements')[1]
            elif  "Contribution to the Film Industry:" in line or "Contribution to the Film Industry" in line or "Contributions to the Film Industry" in line or "Contributions to the Film Industry:" in line :
                capture_Professional_Struggle = False
            # If capture_Key_Achievements is True, add the line to the Key_Achievements_details1
            elif capture_Key_Achievements and line.strip():
                Key_Achievements_details1+=line.strip() + ', '
            sports_json['key events']['achievements']=Key_Achievements_details1

        #contribution to film industry
        time.sleep(4)
        contibution_film_details=''
        capture_contibution_film=False
        lines=response.split('\n')
        for line in lines:
            time.sleep(2)
            if line.__contains__("Contribution to the Film Industry:") :
                capture_contibution_film = True
                contibution_film_details+=line.split('Contribution to the Film Industry:')[1]
            elif line.__contains__("Contributions to the Film Industry:") :
                capture_contibution_film = True
                contibution_film_details+=line.split('Contributions to the Film Industry:')[1]
            elif line.__contains__("Contributions to the Film Industry") :
                capture_contibution_film = True
                contibution_film_details+=line.split('Contributions to the Film Industry')[1]
            elif line.__contains__("Contribution to the Film Industry") :
                capture_contibution_film = True
                contibution_film_details+=line.split('Contribution to the Film Industry')[1]
            # If capture_contibution_film is True, add the line to the contibution_film_details
            elif capture_contibution_film and line.strip():
                contibution_film_details+=line.strip() + ', '
            sports_json['key events']['contribution to film industry']=contibution_film_details
            
    
    #awards
    if  response.__contains__('Awards and Recognitions:') or response.__contains__('Awards and Recognitions') or response.__contains__('Awards and recognitions:') or response.__contains__('Awards and recognitions') :
        #awards
        time.sleep(4)
        awards_details=''
        capture_awards=False
        lines=response.split('\n')
        print("list-->",lines)
        for line in lines:
            time.sleep(2)
            if "Awards and Recognitions:" in line :
                capture_awards = True
                awards_details+=line.split('Awards and Recognitions:')[1]
                # print('-----------1111111111----------------',awards_details)
            elif "Awards and Recognitions" in line :
                capture_awards = True
                awards_details+=line.split('Awards and Recognitions')[1]
            elif "Awards and recognitions:" in line :
                capture_awards = True
                awards_details+=line.split('Awards and recognitions:')[1]
            elif "Awards and recognitions" in line :
                capture_awards = True
                awards_details+=line.split('Awards and recognitions')[1]
            elif capture_awards and line.strip():
                awards_details+=line.strip() + ', '
                # print('----------222222---------------',awards_details)
            sports_json['awards']['awards and recognition']=awards_details

        

    #anecdots
    if response.__contains__("Anecdotes:") or response.__contains__("Anecdotes"):
        #Anecdots
        time.sleep(4)
        Anecdots_details=''
        capture_Anecdots=False
        lines=response.split('\n')
        print("list-->",lines)
        for line in lines:
            time.sleep(2)
            if "Anecdotes:" in line :
                capture_Anecdots = True
                Anecdots_details+=line.split('Anecdotes:')[1]
                # print('-----------1111111111----------------',Anecdots_details)
            elif "Anecdotes" in line :
                capture_Anecdots = True
                Anecdots_details+=line.split('Anecdotes')[1]
            elif  "Controversies:" in line or "Controversies" in line or "Controversy" in line:
                capture_Anecdots = False
            elif capture_Anecdots and line.strip():
                Anecdots_details+=line.strip() + ', '
                # print('----------222222---------------',Anecdots_details)
            sports_json['anecdots']['anecdots']=Anecdots_details

        #controversies
        time.sleep(4)
        controversies_details=''
        capture_controversies=False
        lines=response.split('\n')
        for line in lines:
            time.sleep(2)
            if "Controversies:" in line :
                capture_controversies = True
                controversies_details+=line.split('Controversies:')[1]
            elif "Controversies" in line :
                capture_controversies = True
                controversies_details+=line.split('Controversies')[1]
            # If capture_controversies is True, add the line to the controversies details
            elif capture_controversies and line.strip():
                controversies_details+=line.strip() + ', '
            sports_json['anecdots']['controversies']=controversies_details

    #personality attributes
    if   response.__contains__('Personality Attributes:') or response.__contains__('Personality Attributes') :
        time.sleep(4)
        personality_details=''
        capture_personality=False
        lines=response.split('\n')
        for line in lines:
            time.sleep(2)
            if "Personality Attributes:" in line :
                capture_personality = True
                personality_details+=line.split('Personality Attributes:')[1]
            elif "Personality Attributes" in line :
                capture_personality = True
                personality_details+=line.split('Personality Attributes')[1]
            # If capture_personality is True, add the line to the personality_details
            elif capture_personality and line.strip():
                personality_details+=line.strip() + ', '
            sports_json['personality attributes']=personality_details


    #contribution
    if  response.__contains__('Society:') or response.__contains__('Society') :
        #society
        time.sleep(4)
        Society_details=''
        capture_Society=False
        lines=response.split('\n')
        print("list-->",lines)
        for line in lines:
            time.sleep(2)
            if 'Society:' in line :
                capture_Society = True
                Society_details+=line.split('Society:')[1]
                # print('-----------1111111111----------------',Society_details)
            elif "Society" in line :
                capture_Society = True
                Society_details+=line.split('Society')[1]
            elif  "Philanthropy:" in line or "Philanthropy" in line:
                capture_Society = False
            elif capture_Society and line.strip():
                Society_details+=line.strip() + ', '
                # print('----------222222---------------',Society_details)
            sports_json['contribution']['society']=Society_details


        #Philanthropy
        time.sleep(4)
        Philanthropy_details=''
        capture_Philanthropy=False
        lines=response.split('\n')
        for line in lines:
            time.sleep(2)
            if "Philanthropy:" in line:
                capture_Philanthropy = True
                Philanthropy_details+=line.split('Philanthropy:')[1]
            elif "Philanthropy" in line:
                capture_Philanthropy = True
                Philanthropy_details+=line.split('Philanthropy')[1]
            # If capture_Philanthropy is True, add the line to the Philanthropy_details
            elif capture_Philanthropy and line.strip():
                Philanthropy_details+=line.strip() + ', '
            sports_json['contribution']['phianthropy']=Philanthropy_details

    #other details
    if response.__contains__('Famous Quotes') or response.__contains__('Famous quotes') or response.__contains__('Famous Quotes:') or response.__contains__('Famous quotes:'):
        #quotes
        time.sleep(4)
        quotes_details=''
        capture_quotes=False
        lines=response.split('\n')
        print("list-->",lines)
        for line in lines:
            # time.sleep(2)
            if 'Famous Quotes:' in line:
                capture_quotes = True
                quotes_details+=line.split('Famous Quotes:')[1]
                # print('-----------1111111111----------------',quotes_details)
            elif 'Famous Quotes' in line:
                capture_quotes = True
                quotes_details+=line.split('Famous Quotes')[1]
            elif 'Famous quotes:' in line:
                capture_quotes = True
                quotes_details+=line.split('Famous quotes:')[1]
            elif 'Famous quotes' in line:
                capture_quotes = True
                quotes_details+=line.split('Famous quotes')[1]
                # print('-----------1111111111----------------',quotes_details)
            elif  "Colleagues' Thoughts:" in line or "Colleagues Thoughts:" in line or "Thoughts:" in line  or "Thoughts" in line:
                capture_quotes = False
            elif capture_quotes and line.strip():
                quotes_details+=line.strip() + ', '
                # print('----------222222---------------',quotes_details)
            sports_json['other details']['famous quotes']=quotes_details
        #thoughts
        time.sleep(4)
        thoughts_details=''
        capture_thoughts=False
        lines=response.split('\n')
        for line in lines:
            # time.sleep(2)
            if line.__contains__('Thoughts:'):
                capture_thoughts = True
                thoughts_details+=line.split(":")[1]
            elif line.__contains__('Thoughts'):
                capture_thoughts = True
                thoughts_details+=line.split("Thoughts")[1]
            # If capture_thoughts is True, add the line to the thoughts_details
            elif capture_thoughts and line.strip():
                thoughts_details+=line.strip() + ', '
            sports_json['other details']["colleagues thoughts"]=thoughts_details  

    #current status
    # if 'Current Status:' in response:
    time.sleep(4)
    status_details=''
    capture_status=False
    lines=response.split('\n')
    for line in lines:
        time.sleep(2)
        if line.__contains__('Current Status:'):
            capture_status = True
            status_details+=line.split(':')[1]
        elif line.__contains__('Current Status'):
            capture_status = True
            status_details+=line.split('Current Status')[1]
        # If capture_personality is True, add the line to the personality_details
        elif capture_status and line.strip():
            status_details+=line.strip() + ', '
        sports_json['current status']=status_details

    return sports_json



def remove_formatting(text):
    # Remove asterisks and bullet points
    text = text.replace('*', '')
    text = text.replace('•', '')
    text = text.replace('-', '')
    text = text.replace('##', '')
    text = text.replace('#', '')
    #remove whitespaces
    text = text.strip()
    #remove newlines
    text = text.replace('\n\n', '\n')
    return text

# Generate content for each question
for i, question in enumerate(questions, start=1):
    response = model.generate_content(question)
    time.sleep(4)
    # print(response.text)
    plain_ouput=remove_formatting(response.text)
    print(plain_ouput)
    time.sleep(4)
    sports=get_values(plain_ouput,Sport_json)
    time.sleep(4)
    print(sports)
    print('*'*30)
    # break
    

# Serialize the generated content to JSON
json_output = json.dumps(Sport_json, indent=4)

# Write JSON output to a file
with open('Json_files/famous_personality_devanand.json', 'w') as json_file:
    json_file.write(json_output)

print("json has been saved to 'famous_personality_devanand.json'")
