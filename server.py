from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_endpoint():
    textToAnalyze = request.args.get('textToAnalyze')
    result = emotion_detector(textToAnalyze)
    return_text = f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion'][0]}."
    return result_text

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    app.run(debug=True)
