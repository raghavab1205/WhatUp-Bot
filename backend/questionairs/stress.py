from pymongo import MongoClient

# Connect to the MongoDB server (adjust the URI if you're using a different setup)
client = MongoClient('mongodb://localhost:27017/')
db = client['chatbot_db']  # Database name
collection = db['pss_questions']  # Collection name

# Define the PSS-10 questions with the required structure
pss_questions = [
    {
        "_id": 1,
        "question_number": 1,
        "question_text": "In the last month, how often have you been upset because of something that happened unexpectedly?",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Never", "score": 0},
            {"Option_number": "1", "option_text": "Almost Never", "score": 1},
            {"Option_number": "2", "option_text": "Sometimes", "score": 2},
            {"Option_number": "3", "option_text": "Fairly Often", "score": 3},
            {"Option_number": "4", "option_text": "Very Often", "score": 4}
        ]
    },
    {
        "_id": 2,
        "question_number": 2,
        "question_text": "In the last month, how often have you felt that you were unable to control the important things in your life?",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Never", "score": 0},
            {"Option_number": "1", "option_text": "Almost Never", "score": 1},
            {"Option_number": "2", "option_text": "Sometimes", "score": 2},
            {"Option_number": "3", "option_text": "Fairly Often", "score": 3},
            {"Option_number": "4", "option_text": "Very Often", "score": 4}
        ]
    },
    {
        "_id": 3,
        "question_number": 3,
        "question_text": "In the last month, how often have you felt nervous and stressed?",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Never", "score": 0},
            {"Option_number": "1", "option_text": "Almost Never", "score": 1},
            {"Option_number": "2", "option_text": "Sometimes", "score": 2},
            {"Option_number": "3", "option_text": "Fairly Often", "score": 3},
            {"Option_number": "4", "option_text": "Very Often", "score": 4}
        ]
    },
    {
        "_id": 4,
        "question_number": 4,
        "question_text": "In the last month, how often have you felt confident about your ability to handle your personal problems?",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Never", "score": 4},
            {"Option_number": "1", "option_text": "Almost Never", "score": 3},
            {"Option_number": "2", "option_text": "Sometimes", "score": 2},
            {"Option_number": "3", "option_text": "Fairly Often", "score": 1},
            {"Option_number": "4", "option_text": "Very Often", "score": 0}
        ]
    },
    {
        "_id": 5,
        "question_number": 5,
        "question_text": "In the last month, how often have you felt that things were going your way?",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Never", "score": 4},
            {"Option_number": "1", "option_text": "Almost Never", "score": 3},
            {"Option_number": "2", "option_text": "Sometimes", "score": 2},
            {"Option_number": "3", "option_text": "Fairly Often", "score": 1},
            {"Option_number": "4", "option_text": "Very Often", "score": 0}
        ]
    },
    {
        "_id": 6,
        "question_number": 6,
        "question_text": "In the last month, how often have you found that you could not cope with all the things that you had to do?",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Never", "score": 0},
            {"Option_number": "1", "option_text": "Almost Never", "score": 1},
            {"Option_number": "2", "option_text": "Sometimes", "score": 2},
            {"Option_number": "3", "option_text": "Fairly Often", "score": 3},
            {"Option_number": "4", "option_text": "Very Often", "score": 4}
        ]
    },
    {
        "_id": 7,
        "question_number": 7,
        "question_text": "In the last month, how often have you been able to control irritations in your life?",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Never", "score": 4},
            {"Option_number": "1", "option_text": "Almost Never", "score": 3},
            {"Option_number": "2", "option_text": "Sometimes", "score": 2},
            {"Option_number": "3", "option_text": "Fairly Often", "score": 1},
            {"Option_number": "4", "option_text": "Very Often", "score": 0}
        ]
    },
    {
        "_id": 8,
        "question_number": 8,
        "question_text": "In the last month, how often have you felt that you were on top of things?",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Never", "score": 4},
            {"Option_number": "1", "option_text": "Almost Never", "score": 3},
            {"Option_number": "2", "option_text": "Sometimes", "score": 2},
            {"Option_number": "3", "option_text": "Fairly Often", "score": 1},
            {"Option_number": "4", "option_text": "Very Often", "score": 0}
        ]
    },
    {
        "_id": 9,
        "question_number": 9,
        "question_text": "In the last month, how often have you been angered because of things that happened that were outside of your control?",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Never", "score": 0},
            {"Option_number": "1", "option_text": "Almost Never", "score": 1},
            {"Option_number": "2", "option_text": "Sometimes", "score": 2},
            {"Option_number": "3", "option_text": "Fairly Often", "score": 3},
            {"Option_number": "4", "option_text": "Very Often", "score": 4}
        ]
    },
    {
        "_id": 10,
        "question_number": 10,
        "question_text": "In the last month, how often have you felt difficulties were piling up so high that you could not overcome them?",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Never", "score": 0},
            {"Option_number": "1", "option_text": "Almost Never", "score": 1},
            {"Option_number": "2", "option_text": "Sometimes", "score": 2},
            {"Option_number": "3", "option_text": "Fairly Often", "score": 3},
            {"Option_number": "4", "option_text": "Very Often", "score": 4}
        ]
    }
]

# Insert the questions into the collection
result = collection.insert_many(pss_questions)
