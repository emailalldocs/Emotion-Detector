import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=input_json)
    formatted_response = json.loads(response.text)
    
    import json
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': max(emotions, key=emotions.get)
    }
    
from EmotionDetection.emotion_detection import emotion_detector
emotion_detector("I love this new technology.")
{'anger': 0.013, 'disgust': 0.001, 'fear': 0.004, 'joy': 0.97, 'sadness': 0.024, 'dominant_emotion': 'joy'}
