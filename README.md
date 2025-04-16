Detailed README for GitHub Repository
NLP Sentiment Diary & Chat Application
This repository hosts the code for a web application developed as part of a group project focused on Natural Language Processing (NLP) and sentiment analysis research. Although our research into enhancing NLP preprocessing did not achieve the desired breakthroughs, the project successfully produced an engaging web application with two main features that utilize sentiment tagging on user input.

Table of Contents
Overview

Features

Technologies

Architecture

Installation & Setup

Usage

Challenges & Learnings

License

Overview
The application was designed to simulate interactive user experiences while exploring sentiment analysis through NLP. It comprises two primary features:

Chat Box: A messaging platform where users can interact with a doctor-like persona. Each user message is stored and tagged with an emotion or sentiment predicted by our ML model.

Diary: A journaling interface resembling a paper-notebook style, where users can input text. Each paragraph entry is analyzed and tagged with an emotion according to the model’s classification across 7 sentiment classes.

Note: Despite high accuracy on paper, our ML model’s overall performance was hindered by issues in NLP preprocessing, leading to inaccuracies in real-world sentiment detection.

Features
Chat Functionality:

Mimics a doctor-patient chat interface.

User messages are saved as text with auto-generated sentiment/emotion tags.

Diary Interface:

A paper-like interface for textual diary entries.

Each paragraph is analyzed and tagged with a sentiment from one of 7 classes.

Backend Data Handling:

Integration with a MongoDB Atlas database for storing user messages and diary entries.

Python backend built with Flask for handling data requests and integrating the ML model.

Technologies
Frontend:
JavaScript/TypeScript: Primary scripting languages.

React Framework: For building interactive user interfaces.

Backend:
Python: For fetching and handling data, as well as interfacing with the ML model.

Flask: Lightweight framework used to integrate and serve both backend and frontend.

Database:
MongoDB Atlas: Cloud-based database solution used to store user data and diary entries.

ML Model:
A custom-built sentiment analysis model predicting sentiment across 7 classes; deployed as part of the Python backend.

Architecture
Client-Side: The React application developed in JavaScript/TypeScript handles user interactions, captures input from both the chat box and diary, and communicates with the backend via HTTP requests.

Server-Side: A Flask application in Python manages RESTful API endpoints, processes and stores data, and integrates with the ML model to tag user inputs.

Database: MongoDB Atlas serves as the central repository for all user texts and metadata.

This clear separation of concerns not only promotes scalability but also simplifies troubleshooting and future iterations.

Usage
Chat Function: Initiate a conversation in the chat interface. Messages will be sent to the backend, processed, and tagged with the predicted sentiment.

Diary: Write and submit diary entries. The text is segmented into paragraphs; each is tagged with a sentiment based on our ML model.

Challenges & Learnings
NLP Preprocessing: Despite high experimental accuracy, the preprocessing stage proved to be a significant bottleneck, affecting model predictions.

Integration: Successfully combining a real-time chat and diary application with sentiment analysis provided practical insights into balancing frontend interactivity with backend processing.

Iterative Improvement: The project highlighted the need for refined NLP methodologies and advanced data handling techniques when dealing with subjective text analysis.

Thankyou for visiting this repository.
