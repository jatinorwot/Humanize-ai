SIMRAN: Emotion-Based AI Chatbot (Which can speak in Both Hindi and English)

This project is a conversational AI chatbot named "Simran" that generates responses based on the detected emotion of the user's input. The chatbot uses Google Generative AI for text generation and a sentiment analysis model to classify emotions in user input.
Features

    ->Emotion Detection: Uses a sentiment analysis pipeline to classify the user's input into one of several emotions.
    ->Emotion-Based Responses: Generates responses tailored to the detected emotion, providing a more personalized and engaging user experience.
    ->Conversational Flow: Engages users in a natural conversation, responding in a human-like manner and asking relevant follow-up questions.

Prerequisites

    ->Python 3.x
    ->An Google generative API key
    
Installation

Clone the repository:

        git clone https://github.com/jatinorwot/Humanize-ai.git
        cd Humanize-ai

Create a virtual environment:



        python -m venv venv
        source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:

    pip install -r requirements.txt
    
Set up the API keys:
        Open the script file and replace 'Enter your api key here' with your actual Google API key.


Run the chatbot: 

        python gen_ai.py

Interact with the chatbot:

    Start the conversation by typing Hi.
    Type your messages and see Simran's responses.
    Type exit to end the conversation.
