import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse }
     }
    response = requests.post(url, json = myobj, headers=header)
    
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        formatted_response = formatted_response['emotionPredictions'][0]['emotion']
        
        dominant_score = -1
        dominant_name = ""
        for emotion in formatted_response.keys():
            if formatted_response[emotion]>dominant_score:
                dominant_name = emotion
                dominant_score = formatted_response[emotion]
        formatted_response["dominant_emotion"]=dominant_name

    elif response.status_code == 400:
        formatted_response = {
                'anger': None,
                'disgust': None, 
                'fear': None, 
                'joy': None, 
                'sadness': None, 
                'dominant_emotion': None}
  
    return (formatted_response)