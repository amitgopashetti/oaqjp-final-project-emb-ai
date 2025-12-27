import requests
import json

def emotion_detector(text_to_analyse):
    #URL for emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    #Headers for the service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    #Request object for the service
    input_json = { "raw_document": { "text": text_to_analyse } }

    # Sending a POST request to the emotion detection API
    response = requests.post(url, json=input_json, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    #Extration emotion dictionary from formatted response containing score for
    #anger, disgust, fear, joy, sadness emotions
    emotion = formatted_response['emotionPredictions'][0]['emotion']
    
    #Getting dominant response and appending it to the emotion dictionary
    dominant_emotion = max(emotion, key = emotion.get)
    emotion['dominant_emotion'] = dominant_emotion

    # Returning a dictionary containing sentiment analysis results
    return emotion