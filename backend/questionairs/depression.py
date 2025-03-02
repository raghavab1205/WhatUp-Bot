from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Adjust if using a cloud MongoDB service
db = client['chatbot_db']  # Database name
collection = db['Depression_questions']  # Collection name


bdi_ii_questions = ([
    {
        "_id": 1,
        "question_number": 1,
        "question_text": "Sadness",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I do not feel sad.", "score": 0},
            {"Option_number": "1", "option_text": "I feel sad much of the time.", "score": 1},
            {"Option_number": "2", "option_text": "I am sad all the time.", "score": 2},
            {"Option_number": "3", "option_text": "I am so sad or unhappy that I can't stand it.", "score": 3}
        ]
    },
    {
        "_id": 2,
        "question_number": 2,
        "question_text": "Pessimism",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I am not discouraged about my future.", "score": 0},
            {"Option_number": "1", "option_text": "I feel more discouraged about my future than I used to.", "score": 1},
            {"Option_number": "2", "option_text": "I do not expect things to work out for me.", "score": 2},
            {"Option_number": "3", "option_text": "I feel my future is hopeless and will only get worse.", "score": 3}
        ]
    },
    {
        "_id": 3,
        "question_number": 3,
        "question_text": "Past Failure",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I do not feel like a failure.", "score": 0},
            {"Option_number": "1", "option_text": "I have failed more than I should have.", "score": 1},
            {"Option_number": "2", "option_text": "As I look back, I see a lot of failures.", "score": 2},
            {"Option_number": "3", "option_text": "I feel I am a total failure as a person.", "score": 3}
        ]
    },
    {
        "_id": 4,
        "question_number": 4,
        "question_text": "Loss of Pleasure",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I get as much pleasure as I ever did from the things I enjoy.", "score": 0},
            {"Option_number": "1", "option_text": "I don't enjoy things as much as I used to.", "score": 1},
            {"Option_number": "2", "option_text": "I get very little pleasure from the things I used to enjoy.", "score": 2},
            {"Option_number": "3", "option_text": "I can't get any pleasure from the things I used to enjoy.", "score": 3}
        ]
    },
    {
        "_id": 5,
        "question_number": 5,
        "question_text": "Guilty Feelings",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I don't feel particularly guilty.", "score": 0},
            {"Option_number": "1", "option_text": "I feel guilty over many things I have done or should have done.", "score": 1},
            {"Option_number": "2", "option_text": "I feel quite guilty most of the time.", "score": 2},
            {"Option_number": "3", "option_text": "I feel guilty all the time.", "score": 3}
        ]
    },
    {
        "_id": 6,
        "question_number": 6,
        "question_text": "Punishment Feelings",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I don't feel I am being punished.", "score": 0},
            {"Option_number": "1", "option_text": "I feel I may be punished.", "score": 1},
            {"Option_number": "2", "option_text": "I expect to be punished.", "score": 2},
            {"Option_number": "3", "option_text": "I feel I am being punished.", "score": 3}
        ]
    },
    {
        "_id": 7,
        "question_number": 7,
        "question_text": "Self-Dislike",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I feel the same about myself as ever.", "score": 0},
            {"Option_number": "1", "option_text": "I have lost confidence in myself.", "score": 1},
            {"Option_number": "2", "option_text": "I am disappointed in myself.", "score": 2},
            {"Option_number": "3", "option_text": "I dislike myself.", "score": 3}
        ]
    },
    {
        "_id": 8,
        "question_number": 8,
        "question_text": "Self-Criticalness",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I don't criticize or blame myself more than usual.", "score": 0},
            {"Option_number": "1", "option_text": "I am more critical of myself than I used to be.", "score": 1},
            {"Option_number": "2", "option_text": "I criticize myself for all of my faults.", "score": 2},
            {"Option_number": "3", "option_text": "I blame myself for everything bad that happens.", "score": 3}
        ]
    },
    {
        "_id": 9,
        "question_number": 9,
        "question_text": "Suicidal Thoughts or Wishes",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I don't have any thoughts of killing myself.", "score": 0},
            {"Option_number": "1", "option_text": "I have thoughts of killing myself, but I would not carry them out.", "score": 1},
            {"Option_number": "2", "option_text": "I would like to kill myself.", "score": 2},
            {"Option_number": "3", "option_text": "I would kill myself if I had the chance.", "score": 3}
        ]
    },

    {
        "_id": 10,
        "question_number": 10,
        "question_text": "Crying",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I don't cry anymore than I used to.", "score": 0},
            {"Option_number": "1", "option_text": "I cry more than I used to.", "score": 1},
            {"Option_number": "2", "option_text": "I cry over every little thing.", "score": 2},
            {"Option_number": "3", "option_text": "I feel like crying, but I can't.", "score": 3}
        ]
    },
    {
        "_id": 11,
        "question_number": 11,
        "question_text": "Agitation",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I am no more restless or wound up than usual.", "score": 0},
            {"Option_number": "1", "option_text": "I feel more restless or wound up than usual.", "score": 1},
            {"Option_number": "2", "option_text": "I am so restless or agitated, it's hard to stay still.", "score": 2},
            {"Option_number": "3", "option_text": "I am so restless or agitated that I have to keep moving or doing something.", "score": 3}
        ]
    },
    {
        "_id": 12,
        "question_number": 12,
        "question_text": "Loss of Interest",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I have not lost interest in other people or activities.", "score": 0},
            {"Option_number": "1", "option_text": "I am less interested in other people or things than before.", "score": 1},
            {"Option_number": "2", "option_text": "I have lost most of my interest in other people or things.", "score": 2},
            {"Option_number": "3", "option_text": "It's hard to get interested in anything.", "score": 3}
        ]
    },
    {
        "_id": 13,
        "question_number": 13,
        "question_text": "Indecisiveness",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I make decisions about as well as ever.", "score": 0},
            {"Option_number": "1", "option_text": "I find it more difficult to make decisions than usual.", "score": 1},
            {"Option_number": "2", "option_text": "I have much greater difficulty in making decisions than I used to.", "score": 2},
            {"Option_number": "3", "option_text": "I have trouble making any decisions.", "score": 3}
        ]
    },
    {
        "_id": 14,
        "question_number": 14,
        "question_text": "Worthlessness",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I do not feel I am worthless.", "score": 0},
            {"Option_number": "1", "option_text": "I don't consider myself as worthwhile and useful as I used to.", "score": 1},
            {"Option_number": "2", "option_text": "I feel more worthless as compared to others.", "score": 2},
            {"Option_number": "3", "option_text": "I feel utterly worthless.", "score": 3}
        ]
    },
    {
        "_id": 15,
        "question_number": 15,
        "question_text": "Loss of Energy",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I have as much energy as ever.", "score": 0},
            {"Option_number": "1", "option_text": "I have less energy than I used to have.", "score": 1},
            {"Option_number": "2", "option_text": "I don't have enough energy to do very much.", "score": 2},
            {"Option_number": "3", "option_text": "I don't have enough energy to do anything.", "score": 3}
        ]
    },
    {
        "_id": 16,
        "question_number": 16,
        "question_text": "Changes in Sleeping Pattern",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I have not experienced any change in my sleeping.", "score": 0},
            {"Option_number": "1a", "option_text": "I sleep somewhat more than usual.", "score": 1},
            {"Option_number": "1b", "option_text": "I sleep somewhat less than usual.", "score": 1},
            {"Option_number": "2a", "option_text": "I sleep a lot more than usual.", "score": 2},
            {"Option_number": "2b", "option_text": "I sleep a lot less than usual.", "score": 2},
            {"Option_number": "3a", "option_text": "I sleep most of the day.", "score": 3},
            {"Option_number": "3b", "option_text": "I wake up 1-2 hours early and can't get back to sleep.", "score": 3}
        ]
    },
    {
        "_id": 17,
        "question_number": 17,
        "question_text": "Irritability",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I am not more irritable than usual.", "score": 0},
            {"Option_number": "1", "option_text": "I am more irritable than usual.", "score": 1},
            {"Option_number": "2", "option_text": "I am much more irritable than usual.", "score": 2},
            {"Option_number": "3", "option_text": "I am irritable all the time.", "score": 3}
        ]
    },
    {
        "_id": 18,
        "question_number": 18,
        "question_text": "Changes in Appetite",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I have not experienced any change in my appetite.", "score": 0},
            {"Option_number": "1a", "option_text": "My appetite is somewhat less than usual.", "score": 1},
            {"Option_number": "1b", "option_text": "My appetite is somewhat greater than usual.", "score": 1},
            {"Option_number": "2a", "option_text": "My appetite is much less than before.", "score": 2},
            {"Option_number": "2b", "option_text": "My appetite is much greater than usual.", "score": 2},
            {"Option_number": "3a", "option_text": "I have no appetite at all.", "score": 3},
            {"Option_number": "3b", "option_text": "I crave food all the time.", "score": 3}
        ]
    },
    {
        "_id": 19,
        "question_number": 19,
        "question_text": "Concentration Difficulty",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I can concentrate as well as ever.", "score": 0},
            {"Option_number": "1", "option_text": "I can't concentrate as well as usual.", "score": 1},
            {"Option_number": "2", "option_text": "It's hard to keep my mind on anything for very long.", "score": 2},
            {"Option_number": "3", "option_text": "I find I can't concentrate on anything.", "score": 3}
        ]
    },
    {
        "_id": 20,
        "question_number": 20,
        "question_text": "Tiredness or Fatigue",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I am no more tired or fatigued than usual.", "score": 0},
            {"Option_number": "1", "option_text": "I get more tired or fatigued more easily than usual.", "score": 1},
            {"Option_number": "2", "option_text": "I am too tired or fatigued to do a lot of the things I used to do.", "score": 2},
            {"Option_number": "3", "option_text": "I am too tired or fatigued to do most of the things I used to do.", "score": 3}
        ]
    },
    {
        "_id": 21,
        "question_number": 21,
        "question_text": "Loss of Interest in Sex",
        "response_type": "single_choice",
        "options": [
            {"Option_number": "0", "option_text": "I have not noticed any recent change in my interest in sex.", "score": 0},
            {"Option_number": "1", "option_text": "I am less interested in sex than I used to be.", "score": 1},
            {"Option_number": "2", "option_text": "I am much less interested in sex now.", "score": 2},
            {"Option_number": "3", "option_text": "I have lost interest in sex completely.", "score": 3}
        ]
    }
])

collection.insert_many(bdi_ii_questions)