'''import requests  # Import the requests library to handle HTTP requests

def sentiment_analyzer(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    return response.text  # Return the response text from the API'''


import requests
import json

def sentiment_analyzer(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        label = None
        score = None

    # Return the label and score in a dictionary
    return {'label': label, 'score': score}