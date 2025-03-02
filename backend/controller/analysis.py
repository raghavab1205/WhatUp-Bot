import pandas as pd
import numpy as np

import sys
import os

# Step up two levels from /backend/model/ to the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import backend.config.data_flow as data_flow

def suicide_analysis():
    # Load the data
    df = data_flow.get_data_indf(data_flow.db['suicide_responce'])
    total_score = sum(answer['score'] for answer in df['responses'])
    if total_score <= 7:
        #print("You are at minimal risk of suicide. Please do look after yourself.")
        analized_result = "You are at minimal risk of suicide. Please do look after yourself."

    if total_score > 8 or total_score <= 11:
        #print("You are at moderate risk of suicide. Please seek help from a mental health professional
        analized_result = "You are at moderate risk of suicide. Please seek help from a mental health professional."


    elif total_score > 11:
        #print("You are at high risk of suicide. Please seek immediate help from a mental health
        analized_result = "You are at high risk of suicide. Please seek immediate help from a mental health professional."

    return total_score, analized_result  
    
def stress_analysis():
    df = data_flow.get_data_indf(data_flow.db['stress_responce'])
    total_score = sum(answer['score'] for answer in df['responses'])
    if total_score <= 13:
        #print("You are at minimal risk of suicide. Please do look after yourself.")
        analized_result = "You seem to be a little stressed. Please do look after yourself."


    if 13 < total_score <= 26:
        #print("You are at moderate risk of suicide. Please seek help from a mental health professional
        analized_result = "You have moderate stressed. Please seek help from a mental health professional."


    elif total_score > 26:
        #print("You are at high risk of suicide. Please seek immediate help from a mental health
        analized_result = "You have high perceived stress, Please seek immediate help from a mental health professional."
    
    return total_score, analized_result

def anxiety_analysis():
    df = data_flow.get_data_indf(data_flow.db['anxiety_responce'])
    total_score = sum(answer['score'] for answer in df['responses'])
    if total_score <= 21:
        #print("You are at minimal risk of suicide. Please do look after yourself.")
        analized_result = "You seem to be a little anxious. Please do look after yourself."


    if 21 < total_score <= 35:
        #print("You are at moderate risk of suicide. Please seek help from a mental health professional
        analized_result = "You have moderate anxiety. Please seek help from a mental health professional."


    elif total_score > 35:
        #print("You are at high risk of suicide. Please seek immediate help from a mental health
        analized_result = "You have potentially concerning levels of anxiety, Please seek immediate help from a mental health professional."
    
    return total_score, analized_result

def depression_analysis():
    df = data_flow.get_data_indf(data_flow.db['anxiety_responce'])
    total_score = sum(answer['score'] for answer in df['responses'])
    if total_score <= 13:
        analized_result = "You seem to have minimal depression. Please do look after yourself."

    if 13 < total_score <= 19:
        analized_result = "You seem to be mildly depressed. Please seek help from a mental health professional."

    elif 19 < total_score <= 28:
        analized_result = "You have potentially moderate levels of depression, Please find yourself a mental health professional."

    elif total_score > 28:
        analized_result = "You have potentially severe levels of depression, Please seek immediate help from a mental health professional."
    
    return total_score, analized_result

def bipolar_analysis():
    # Load responses from MongoDB collection
    df = data_flow.get_data_indf(data_flow.db['Bipolar_responce'])
    
    # Calculate the total score for Question 1 (symptoms)
    q1_responses = df['responses'][0]['answers']  # Assuming Question 1 is the first set of responses
    q1_score = sum(answer['true_score'] for answer in q1_responses if 'true_score' in answer)

    # Extract responses for Questions 2 and 3
    q2_response = df['responses'][1]['answer']  # Assuming Question 2 is the second response
    q3_response = df['responses'][2]['answer']  # Assuming Question 3 is the third response

    # Scoring logic for Questions 2 and 3
    q2_score = q2_response['score'] if 'score' in q2_response else 0
    q3_score = q3_response['score'] if 'score' in q3_response else 0

    # Determine the outcome based on MDQ criteria
    if q1_score >= 7 and q2_score == 1 and q3_score >= 2:
        analyzed_result = (
            "Your responses indicate a high likelihood of bipolar disorder. "
            "Please consult a mental health professional for further assessment."
        )
    else:
        analyzed_result = (
            "Your responses do not meet the criteria for a bipolar disorder diagnosis based on the MDQ. "
            "However, if you have concerns, please seek advice from a healthcare provider."
        )

    return q1_score, q2_score, q3_score, analyzed_result

# Add the function to `analysis.py` to integrate it with the existing framework.
