import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the emotion detection service
    
    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    payload = { "raw_document": { "text": text_to_analyse } } # Request payload
    
    response = requests.post(url, json = payload, headers=header) # Sending a POST request to the emotion detection API
    
    #Extracting the emotion dictionary from response if the status code is 200
    if response.status_code == 200:
        formatted_response = json.loads(response.text) #Formatting the response
        
        #Extracting the emotion dictionary from the formatted response
        emotion = formatted_response['emotionPredictions'][0]['emotion']

        #Getting the dominant emotion and appending to the emotion object
        dominant_emotion = max(emotion, key = emotion.get)
        emotion['dominant_emotion'] = dominant_emotion
    #Setting the emotion score and dominant emotion as none if the status code is 400(Empty input) or 500(Invalid input)
    elif response.status_code == 400 or response.status_code == 500:
        emotion = {}
        emotion['anger'] = None
        emotion['joy'] = None
        emotion['disgust'] = None
        emotion['sadness'] = None
        emotion['fear'] = None
        emotion['dominant_emotion'] = None
    
    return emotion