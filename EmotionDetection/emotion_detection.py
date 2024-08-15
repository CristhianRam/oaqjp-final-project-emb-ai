import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse }
     }
    response = requests.post(url, json = myobj, headers=header)
    
    formatted_response = json.loads(response.text)
    formatted_response = formatted_response['emotionPredictions'][0]
    formatted_response = formatted_response['emotion']
    
    dominant_score = -1
    dominant_name = ""
    for emotion in formatted_response.keys():
        if formatted_response[emotion]>dominant_score:
            dominant_name = emotion
            dominant_score = formatted_response[emotion]
    formatted_response["dominant_emotion"]=dominant_name
  
    return (formatted_response)