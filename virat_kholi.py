import google.generativeai as genai
import time
import json
import re

GOOGLE_API_KEY = 'AIzaSyCn0J-flsHb4g4vlMtH953x23f8F-jFHtc'
 
genai.configure(api_key=GOOGLE_API_KEY)
 
questions = [
    "Provide a title of virat kholi with heading as 'Title:' and Introduction of 7 lines with heading as 'Introduction:'  ",
    "Provide following details of Virat Kohli - Birth date with heading as 'Birth date:' and place of birth with heading as 'place of birth', Fathers name with heading 'Father's name:',mothers name with heading 'Mothers name:',brother name with heading as 'brothers name:' , sisters name heading as 'sisters name:', early education with heading as 'Early education:', family values with heading as 'family values:' only 5-7 points",
    "Provide following details of Virat Kohli - Initiation into cricket with heading 'Initiation:', debut in domestic cricket with heading 'Domestic Debut:', debut in international cricket with heading 'International Debut:'",                                                     
    "Provide following details of Virat Kohli- key achievements with heading as 'key achievements:' and statistics with heading as 'Statistics:' in 6-7 points each",
    "Provide following details of Virat Kohli - awards with heading 'Awards:' and Felicitations with heading 'Felicitations:'  ",
    "Provide following details of Virat Kohli- anecdotes with heading 'Anecdots:' and controversies with heading 'Controversies:' in 6-7 short points .",
    "Provide key personality attributes of Virat Kohli with heading 'Personality Attributes:' 10 points ",
    "Provide contribution of Virat Kohli to society with heading 'society:' and philanthropy with heading 'philanthropy:' 8 points each",
    "Provide the following details about Virat Kohli - famous quotes with heading 'Famous quotes:', what do colleagues say with same heading as 'Thoughts:' 7 points each",
    "What is the current status of Virat Kohli - with heading 'Current Status:' with 8 points  "
]
 
# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

#json format
Sport_json={
    'id':'',
    'Catergory':'Sports',
    'name':'Virat Kholi',
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
        # 'Images':''
    },
    'Sport details':{
        'Initation':'',
        'domestic debut':'',
        'International Debut':'',
        
    },
    'achievements':{
        'key achievements':'',
        'statistics':'',
        # 'Images':''
    },
    'awards':{
        'awards':'',
        'felicitation':''
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
    'current status':''   
}


#function to fetch values from response
def get_values(response,sports_json):
    time.sleep(4)
    #tite and introduction
    if response.__contains__('Title') or response.__contains__('Title:'):
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

        # #dates
        # dates=dates_available(response)
        # for date in dates:
        #     if date:
        #         sports_json['title']['date']=date
        #     else:
        #         sports_json['title']['date']=''

    #birth details
    if 'Birth' in response:
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
            if line.__contains__('Family values:') :
                capture_value = True
                value_details += line.split('Family values:')[1]
            elif line.__contains__('Family values') :
                capture_value = True
                value_details += line.split('Family values')[1]
            elif capture_value and line != 'Family values:':
                value_details += line.strip() + ', '
            sports_json['birth details']['family values']=value_details

        #early education
        time.sleep(4)
        early_education_details = ''
        capture_education = False
        for line in list_birth_details:
            time.sleep(2)
            if line.__contains__('Early education:') :
                capture_education = True
                early_education_details+=line.split('Early education:')[1]
                print("----------------early------------------ 1111",early_education_details)
            elif line.__contains__('Early education') :
                capture_education = True
                early_education_details+=line.split('Early education')[1]
                print("----------------early------------------ 1111",early_education_details)
            elif 'Family values:' in line or 'Family values' in line:
                capture_education = False
            elif capture_education and 'Early education:' not in line:
                early_education_details+=line.strip() + ', '
                print("----------------early------------------2222",early_education_details)
            sports_json['birth details']['early education']=early_education_details


    #sport details
    if 'Initiation' in response:
        time.sleep(4)
        #Initiation
        intiation_details=''
        capture_initiation=False
        lines=response.split('\n')
        for line in lines:
            time.sleep(2)
            if line.__contains__("Initiation:") :
                capture_initiation = True
                intiation_details+=line.split('Initiation:')[1]
            elif line.__contains__("Initiation") :
                capture_initiation = True
                intiation_details+=line.split('Initiation')[1]
            elif "Domestic Debut:" in line or "International Debut:" in line or "Domestic Debut" in line or "International Debut" in line:
                capture_initiation = False
            # If capture_initiation is True, add the line to the initiation details
            elif capture_initiation and line.strip():
                intiation_details+=line.strip() + ', '
            sports_json['Sport details']['Initation']=intiation_details
        #domestic debut
        time.sleep(4)
        domestic_debut_details=''
        capture_domestic_debut=False
        lines=response.split('\n')
        for line in lines:
            time.sleep(2)
            if line.__contains__("Domestic Debut:") :
                capture_domestic_debut = True
                domestic_debut_details+=line.split('Domestic Debut:')[1]
            elif line.__contains__("Domestic Debut") :
                capture_domestic_debut = True
                domestic_debut_details+=line.split('Domestic Debut')[1]
            elif  "International Debut:" in line or "International Debut" in line:
                capture_domestic_debut = False
            # If capture_domestic_debut is True, add the line to the domestic details
            elif capture_domestic_debut and line.strip():
                domestic_debut_details+=line.strip() + ', '
            sports_json['Sport details']['domestic debut']=domestic_debut_details
        #International debut
        time.sleep(4)
        International_debut_details=''
        capture_International_debut=False
        lines=response.split('\n')
        for line in lines:
            time.sleep(2)
            if line.__contains__("International Debut:") :
                capture_International_debut = True
                International_debut_details+=line.split('International Debut:')[1]
            elif line.__contains__("International Debut") :
                capture_International_debut = True
                International_debut_details+=line.split('International Debut')[1]
            # If capture_International_debut is True, add the line to the international details
            elif capture_International_debut and line.strip():
                International_debut_details+=line.strip() + ', '
            sports_json['Sport details']['International Debut']=International_debut_details

    #achievments
    if   response.__contains__('Key Achievements:') or response.__contains__('Key Achievements'):
        #key achievements
        time.sleep(4)
        key_achievements_details=''
        capture_achievements=False
        lines=response.split('\n')
        print("list-->",lines)
        for line in lines:
            time.sleep(2)
            if line.__contains__("Key Achievements:") :
                capture_achievements = True
                
                key_achievements_details+=line.split('Key Achievements:')[1]
                # print('-----------1111111111----------------',key_achievements_details)
            elif line.__contains__("Key Achievements") :
                capture_achievements = True
                
                key_achievements_details+=line.split('Key Achievements')[1]
            elif  "Statistics:" in line or "Statistics" in line:
                capture_achievements = False
            elif capture_achievements and line.strip():
                key_achievements_details+=line.strip() + ', '
                # print('----------222222---------------',key_achievements_details)
            sports_json['achievements']['key achievements']=key_achievements_details

        #statistics
        time.sleep(4)
        statistics_details=''
        capture_statistics=False
        lines=response.split('\n')
        for line in lines:
            time.sleep(2)
            if line.__contains__("Statistics:"):
                capture_statistics = True
                statistics_details+=line.split('Statistics:')[1]
            elif line.__contains__("Statistics"):
                capture_statistics = True
                statistics_details+=line.split('Statistics')[1]
            # If capture_statistics is True, add the line to the statistics details
            elif capture_statistics and line.strip():
                statistics_details+=line.strip() + ', '
            sports_json['achievements']['statistics']=statistics_details

    #awards
    if response.__contains__('Awards:') or response.__contains__('Awards'):
        #awards
        time.sleep(4)
        awards_details=''
        capture_awards=False
        lines=response.split('\n')
        print("list-->",lines)
        for line in lines:
            time.sleep(2)
            if line.__contains__("Awards:") :
                capture_awards = True
                awards_details+=line.split('Awards:')[1]
                # print('-----------1111111111----------------',awards_details)
            elif line.__contains__("Awards") :
                capture_awards = True
                awards_details+=line.split('Awards')[1]
            elif  "Felicitations:" in line or "Felicitations" in line:
                capture_awards = False
            elif capture_awards and line.strip():
                awards_details+=line.strip() + ', '
                # print('----------222222---------------',awards_details)
            sports_json['awards']['awards']=awards_details

        #felicitation
        time.sleep(4)
        felicitation_details=''
        capture_felicitation=False
        lines=response.split('\n')
        for line in lines:
            time.sleep(2)
            if line.__contains__("Felicitations:"):
                capture_felicitation = True
                felicitation_details+=line.split('Felicitations:')[1]
            elif line.__contains__("Felicitations"):
                capture_felicitation = True
                felicitation_details+=line.split('Felicitations')[1]
            # If capture_felicitation is True, add the line to the statistics details
            elif capture_felicitation and line.strip():
                felicitation_details+=line.strip() + ', '
            sports_json['awards']['felicitation']=felicitation_details

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
    time.sleep(5)
    # print(response.text)
    plain_ouput=remove_formatting(response.text)
    print(plain_ouput)
    time.sleep(5)
    sports=get_values(plain_ouput,Sport_json)
    time.sleep(4)
    print(sports)
    print('*'*30)
    # break
    

# Serialize the generated content to JSON
json_output = json.dumps(Sport_json, indent=4)

# # Write JSON output to a file
with open('Json_files/famous_personality_virat_kholi1.json', 'w') as json_file:
    json_file.write(json_output)

print("json has been saved to 'famous_personality_virat_kholi.json'")
