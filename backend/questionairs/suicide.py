from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Update if using a cloud-based MongoDB service
db = client['chatbot_db']  # Database name
collection = db['SBQR_questions']  # Collection name

# Define the questions in the required structure
questions = [
    {
        "_id": 1,
        "question_number": 1,
        "question_text": "Have you ever thought about or attempted to kill yourself?",
        "response_type": "single_choice",
        "options": [
            {"option_text": "Never", "score": 1},
            {"option_text": "It was just a brief passing thought", "score": 2},
            {"option_text": "I have had a plan at least once to kill myself but did not try to do it", "score": 3},
            {"option_text": "I have had a plan at least once to kill myself and really wanted to die", "score": 3},
            {"option_text": "I have attempted to kill myself, but did not want to die", "score": 4},
            {"option_text": "I have attempted to kill myself, and really hoped to die", "score": 4}
        ]
    },
    {
        "_id": 2,
        "question_number": 2,
        "question_text": "How often have you thought about killing yourself in the past year?",
        "response_type": "single_choice",
        "options": [
            {"option_text": "Never", "score": 1},
            {"option_text": "Rarely (1 time)", "score": 2},
            {"option_text": "Sometimes (2 times)", "score": 3},
            {"option_text": "Often (3-4 times)", "score": 4},
            {"option_text": "Very Often (5 or more times)", "score": 5}
        ]
    },
    {
        "_id": 3,
        "question_number": 3,
        "question_text": "Have you ever told someone that you were going to commit suicide, or that you might do it?",
        "response_type": "single_choice",
        "options": [
            {"option_text": "No", "score": 1},
            {"option_text": "Yes, at one time, but did not really want to die", "score": 2},
            {"option_text": "Yes, at one time, and really wanted to die", "score": 2},
            {"option_text": "Yes, more than once, but did not want to do it", "score": 3},
            {"option_text": "Yes, more than once, and really wanted to do it", "score": 3}
        ]
    },
    {
        "_id": 4,
        "question_number": 4,
        "question_text": "How likely is it that you will attempt suicide someday?",
        "response_type": "single_choice",
        "options": [
            {"option_text": "Never - No chance at all", "score": 1},
            {"option_text": "Rather Unlikely", "score": 2},
            {"option_text": "Unlikely", "score": 3},
            {"option_text": "Likely", "score": 4},
            {"option_text": "Rather Likely", "score": 5},
            {"option_text": "Very Likely", "score": 6}
        ]
    }
]

# Insert the questions into MongoDB
collection.insert_many(questions)

print("SBQ-R questions have been successfully inserted into the MongoDB database.")