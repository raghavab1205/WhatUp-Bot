from flask import Flask, render_template, request, jsonify

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.data_flow import db, store_input, suicide_response, anxiety_response, stress_response, depression_response, bipolar_response
#from model import get_clean_data, vectorizer
import joblib
import pickle
import controller.analysis as analysis

# Load pre-trained model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = joblib.load("vectorizer.pkl")
get_clean_data = joblib.load("get_clean_data.pkl")

app = Flask(__name__)

# Mapping of predicted emotions to database collections and analysis functions
EMOTION_MAPPING = {
    0: {
        'collection': anxiety_response,
        'analysis_func': analysis.anxiety_analysis
    },
    1: {
        'collection': bipolar_response,
        'analysis_func': analysis.bipolar_analysis
    },
    2: {
        'collection': depression_response,
        'analysis_func': analysis.depression_analysis
    },
    3: {
        'collection': None,  # Normal case
        'analysis_func': "None"
    },
    4: {
        'collection': None,  # Personality Disorder
        'analysis_func': "None"
    },
    5: {
        'collection': stress_response,
        'analysis_func': analysis.stress_analysis
    },
    6: {
        'collection': suicide_response,
        'analysis_func': analysis.suicide_analysis
    }
}

# Questionnaire flow tracking
conversation_state = {}

# Home route
@app.route('/')
def home():
    return render_template('frontend\index.html')  # Renders home page

# Chatbot page route
@app.route('/diary')
def chatbot():
    return render_template('chatbotpage.html')  # Renders chatbot page

@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        # Get user message from request
        user_message = request.json['message']
        store_input(user_message)
        session_id = request.json.get('session_id', '')

        # If no session exists, create a new one
        if session_id not in conversation_state:
            conversation_state[session_id] = {
                'stage': 'initial',
                'predicted_emotion': None,
                'responses': []
            }

        current_state = conversation_state[session_id]

        # Initial stage - predict emotion
        if current_state['stage'] == 'initial':
            # Preprocess the message
            clean = get_clean_data(user_message)
            user_input = vectorizer.transform([clean])

            # Predict emotion/category
            predicted_emotion = model.predict(user_input)[0]
            current_state['predicted_emotion'] = predicted_emotion
            current_state['stage'] = 'questionnaire'

            # Prepare questionnaire questions based on predicted emotion
            emotion_data = EMOTION_MAPPING.get(predicted_emotion, {})
            collection = emotion_data.get('collection')

            if collection:
                # Fetch questionnaire questions from the database
                questionnaire = list(collection.find({}, {'question': 1, '_id': 0}))
                questions = [q['question'] for q in questionnaire]

                return jsonify({
                    'response': f"I'll ask you a few questions to understand more.",
                    'questions': questions
                })
            else:
                return jsonify({
                    'response': "You seem to be doing well mentally. Is there anything specific you'd like to discuss?",
                    'questions': None
                })

        # Questionnaire stage - collect responses
        elif current_state['stage'] == 'questionnaire':
            # Store user's response
            current_state['responses'].append({
                'message': user_message,
                'score': 1  # You might want to implement a more sophisticated scoring mechanism
            })

            # Check if all questions have been answered
            emotion_data = EMOTION_MAPPING.get(current_state['predicted_emotion'], {})
            collection = emotion_data.get('collection')
            
            if collection:
                questionnaire = list(collection.find({}, {'question': 1, '_id': 0}))
                
                if len(current_state['responses']) == len(questionnaire):
                    # Perform analysis
                    analysis_func = emotion_data.get('analysis_func')
                    if analysis_func:
                        # Prepare data for analysis
                        analysis_data = {
                            'responses': current_state['responses']
                        }
                        
                        # Perform analysis
                        total_score, analyzed_result = analysis_func()
                        
                        # Store analysis results in database
                        db.analysis_results.insert_one({
                            'session_id': session_id,
                            'predicted_emotion': current_state['predicted_emotion'],
                            'responses': current_state['responses'],
                            'total_score': total_score,
                            'analyzed_result': analyzed_result
                        })

                        # Reset conversation state
                        conversation_state[session_id] = {
                            'stage': 'initial',
                            'predicted_emotion': None,
                            'responses': []
                        }

                        return jsonify({
                            'response': analyzed_result,
                            'questions': None
                        })
                
                # If not all questions answered, continue questionnaire
                return jsonify({
                    'response': "Thank you. Let's continue with the next question.",
                    'questions': None
                })

    except Exception as e:
        print(f"Error processing response: {e}")
        return jsonify({
            'response': "I'm having trouble understanding. Could you rephrase that?",
            'questions': None
        })

if __name__ == '__main__':
    app.run(debug=True)