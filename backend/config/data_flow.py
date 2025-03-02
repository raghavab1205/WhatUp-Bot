from pymongo import MongoClient
from scipy.sparse import issparse
import numpy as np
import pandas as pd


client = MongoClient('mongodb+srv://pjlca2k4:chatbot123@chatbot.6riqz.mongodb.net/?retryWrites=true&w=majority&appName=Chatbot')
db = client['chatbot_db']

user = db['user']   
cache = db['cache']              
main = db['main']
suicide_response = db["suicide_response"]
anxiety_response = db["anxiety_responce"]
stress_response = db["stress_responce"]
depression_response = db["depression_responce"] 
bipolar_response = db["bipolar_responce"]    

file_path = r"backend\new.csv"
df = pd.read_csv(file_path)

if main.estimated_document_count() == 0:
    main.insert_many(df[['statement', 'status']].to_dict('records'))
    
def get_data_indf(dataframes):
    return pd.DataFrame(list(dataframes.find()))

def check_cache(user_input): 
     # Query the cache collection to find a match for the user_input
    cache_result = db.cache.find_one({'user_input': user_input})
    if cache_result:
        return cache_result['bot_response']  # Return the cached response
    return None  # Return None if not found

def store_input(user_input):
    # Define the input document
    input_entry = {
        'user_input': user_input  # Convert to a list if it's in array form
    }
    # Store the input in the inputs collection
    db.user.insert_one(input_entry)

def suicide_responses(responses):
    response_document = { 
        "responses": []  
    }    
    for response in responses:
        response_data = {
            "question_number": response['question_number'],
            "selected_option": response['selected_option'],
            "response_text": response['response_text'],
            "score": response['score']
        }
        response_document["responses"].append(response_data)    
    suicide_response.insert_one(response_document)
    print("Responses successfully stored in the database.")

def stress_responses(responses):
    response_document = {  
        "responses": [] 
    }    
    for response in responses:
        response_data = {
            "question_id": response['question_id'],
            "response_text": response['response_text'],
            "score": response['score']  
        }
        response_document["responses"].append(response_data)
    stress_response.insert_one(response_document)
    print("Responses successfully stored in the database.")

def depression_responses(responses):
    response_document = {
        "responses": [] 
    }
    for response in responses:
        response_data = {
            "question_number": response['question_number'], 
            "selected_option": response['selected_option'],
            "Option_text": response['Option_text'],        
            "score": response['score']                      
        }
        response_document["responses"].append(response_data)
    depression_response.insert_one(response_document)
    print("User responses successfully stored in the database.")

def anxiety_responses(responses):
    response_document = {  
        "responses": []
    }
    for response in responses:
        response_data = {
            "question_id": response['question_id'],
            "response_text": response['response_text'],
            "score": response['score'] 
        }
        response_document["responses"].append(response_data)
    anxiety_response.insert_one(response_document)
    print("Responses successfully stored in the database.")


def bipolar_responses(responses): 
    user_response_document = {
        "responses": [],
    }
    for question in responses:
        question_number = question['question_number']
        prefix = question.get('prefix', None)  
        if 'sub_responses' in question:
            sub_responses_list = []
            for sub_response in question['sub_responses']:
                sub_response_data = {
                    "sub_question_number": sub_response['sub_question_number'],
                    "suffix": sub_response['suffix'],
                    "response": sub_response['response']
                }
                sub_responses_list.append(sub_response_data)
            user_response_document['responses'].append({
                "question_number": question_number,
                "prefix": prefix,
                "sub_responses": sub_responses_list
            })
        else:
            user_response_document['responses'].append({
                "question_number": question_number,
                "response": question['response']
            })
    bipolar_response.insert_one(user_response_document)
    print("User responses successfully stored in the database.")

def store_cache(user_input, bot_response):
    # Define the cache document
    if issparse(bot_response):
        bot_response = bot_response[0].toarray().tolist()
          # Convert sparse matrix to dense array, then to list
    elif isinstance(bot_response, np.ndarray):
        bot_response = bot_response[0].flatten().tolist()  # Flatten and convert to list
    elif isinstance(bot_response, (list, str, int, float)):
        pass  # Already a basic type
    else:
        bot_response = str(bot_response)

    print("Processed bot_response:", bot_response)

    cache_entry = {
        'user_input': user_input,  # Convert to a list if it's in array form
        'bot_response': bot_response  # Store the response
    }
    # Store the entry in the cache collection
    db.cache.insert_one(cache_entry)

