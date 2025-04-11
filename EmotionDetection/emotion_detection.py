import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=headers, json=input_json)
    
    emotions = {}

    if response.status_code == 200: 
        format_text = json.loads(response.text)
        emotions = format_text['emotionPredictions'][0]['emotion']
        emotions['dominant_emotion'] = max(emotions.items(), key=lambda x: x[1])

    elif response.status_code == 400:
        emotions['anger'] = None
        emotions['disgust'] = None
        emotions['fear'] = None
        emotions['joy'] = None
        emotions['sadness'] = None
        emotions['dominant_emotion'] = (None, None)
    
    return emotions
        
