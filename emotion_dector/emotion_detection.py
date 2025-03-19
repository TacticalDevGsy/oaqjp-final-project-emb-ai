import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = input_json, headers=headers)
    formated_response = json.loads(response.text)
    response = extract_emotions(formated_response)

    return response

def extract_emotions(formated_response):
    emotions = formated_response.get('emotionPredictions', None)[0].get('emotion', None)
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)

    """
    Appending the max emotion still correctly returns the format as asked
        {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': '<name of the dominant emotion>'
            } 
    """
    return emotions
