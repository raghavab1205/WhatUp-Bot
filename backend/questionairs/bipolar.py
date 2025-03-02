from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Adjust if using a cloud MongoDB service
db = client['chatbot_db']  # Database name
collection = db['Bipolar_questions']  # Collection name

# Define the questions in the required structure
questions = [
    {
        "_id": 1,
        "question_number": 1,
        "question_text": "Has there ever been a period of time when you were not your usual self and...",
        "response_type": "true_false",
        "options": [
            {"option_text": "...you felt so good or so hyper that other people thought you were not your normal self or you were so hyper that you got into trouble?", "true_score": 1, "false_score": 0},
            {"option_text": "...you were so irritable that you shouted at people or started fights or arguments?", "true_score": 1, "false_score": 0},
            {"option_text": "...you felt much more self-confident than usual?", "true_score": 1, "false_score": 0},
            {"option_text": "...you got much less sleep than usual and found you didn’t really miss it?", "true_score": 1, "false_score": 0},
            {"option_text": "...you were much more talkative or spoke faster than usual?", "true_score": 1, "false_score": 0},
            {"option_text": "...thoughts raced through your head or you couldn’t slow your mind down?", "true_score": 1, "false_score": 0},
            {"option_text": "...you were so easily distracted by things around you that you had trouble concentrating or staying on track?", "true_score": 1, "false_score": 0},
            {"option_text": "...you had much more energy than usual?", "true_score": 1, "false_score": 0},
            {"option_text": "...you were much more active or did many more things than usual?", "true_score": 1, "false_score": 0},
            {"option_text": "...you were much more social or outgoing than usual, for example, you telephoned friends in the middle of the night?", "true_score": 1, "false_score": 0},
            {"option_text": "...you were much more interested in sex than usual?", "true_score": 1, "false_score": 0},
            {"option_text": "...you did things that were unusual for you or that other people might have thought were excessive, foolish, or risky?", "true_score": 1, "false_score": 0},
            {"option_text": "...spending money got you or your family in trouble?", "true_score": 1, "false_score": 0}
        ]
    },
    {
        "_id": 2,
        "question_number": 2,
        "question_text": "If you checked YES to more than one of the above, have several of these ever happened during the same period of time?",
        "response_type": "single_choice",
        "options": [
            {"option_text": "Yes", "score": 1},
            {"option_text": "No", "score": 0}
        ]
    },
    {
        "_id": 3,
        "question_number": 3,
        "question_text": "How much of a problem did any of these cause you — like being able to work; having family, money, or legal troubles; getting into arguments or fights?",
        "response_type": "single_choice",
        "options": [
            {"option_text": "No problem", "score": 0},
            {"option_text": "Minor problem", "score": 1},
            {"option_text": "Moderate problem", "score": 2},
            {"option_text": "Serious problem", "score": 3}
        ]
    },
    {
        "_id": 4,
        "question_number": 4,
        "question_text": "Have any of your blood relatives (ie, children, siblings, parents, grandparents, aunts, uncles) had manic-depressive illness or bipolar disorder?",
        "response_type": "single_choice",
        "options": [
            {"option_text": "Yes", "score": 1},
            {"option_text": "No", "score": 0}
        ]
    },
    {
        "_id": 5,
        "question_number": 5,
        "question_text": "Has a health professional ever told you that you have manic-depressive illness or bipolar disorder?",
        "response_type": "single_choice",
        "options": [
            {"option_text": "Yes", "score": 1},
            {"option_text": "No", "score": 0}
        ]
    }
]

# Insert the questions into MongoDB
collection.insert_many(questions)

print("Questionnaire has been successfully inserted into the MongoDB database.")