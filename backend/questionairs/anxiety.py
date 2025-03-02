from pymongo import MongoClient

# Connect to the MongoDB server (adjust the URI if you're using a different setup)
client = MongoClient('mongodb://localhost:27017/')
db = client['chatbot_db']  # Database name
collection = db['anxiety_questions']  # Collection name

# Define the BAI-21 questions with the required structure
bai_questions = [
    # Questions 1 to 12 (already provided)
    {
        "_id": 1,
        "question_number": 1,
        "question_text": "Numbness or tingling",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 2,
        "question_number": 2,
        "question_text": "Feeling hot",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 3,
        "question_number": 3,
        "question_text": "Wobbliness in legs",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 4,
        "question_number": 4,
        "question_text": "Unable to relax",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 5,
        "question_number": 5,
        "question_text": "Fear of worst happening",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 6,
        "question_number": 6,
        "question_text": "Dizzy or lightheaded",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 7,
        "question_number": 7,
        "question_text": "Heart pounding / racing",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 8,
        "question_number": 8,
        "question_text": "Unsteady",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 9,
        "question_number": 9,
        "question_text": "Terrified or afraid",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 10,
        "question_number": 10,
        "question_text": "Nervous",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 11,
        "question_number": 11,
        "question_text": "Feeling of choking",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 12,
        "question_number": 12,
        "question_text": "Hands trembling",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    
    # Add remaining questions (13 to 21)
    {
        "_id": 13,
        "question_number": 13,
        "question_text": "Shaky / unsteady",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 14,
        "question_number": 14,
        "question_text": "Fear of losing control",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 15,
        "question_number": 15,
        "question_text": "Difficulty in breathing",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 16,
        "question_number": 16,
        "question_text": "Fear of dying",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 17,
        "question_number": 17,
        "question_text": "Scared",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 18,
        "question_number": 18,
        "question_text": "Indigestion",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 19,
        "question_number": 19,
        "question_text": "Faint / lightheaded",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 20,
        "question_number": 20,
        "question_text": "Face flushed",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    },
    {
        "_id": 21,
        "question_number": 21,
        "question_text": "Hot / cold sweats",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "Not at all", "score": 0},
            {"Option_number": "1", "option_text": "Mildly, but it didn’t bother me much", "score": 1},
            {"Option_number": "2", "option_text": "Moderately – it wasn’t pleasant at times", "score": 2},
            {"Option_number": "3", "option_text": "Severely – it bothered me a lot", "score": 3}
        ]
    }
]

# Insert questions into MongoDB
result = collection.insert_many(bai_questions)

# Output the number of documents inserted
print(f"Inserted {len(result.inserted_ids)} BAI questions into the database.")