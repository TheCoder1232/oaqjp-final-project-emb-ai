"""
This application provides interface for analysing the content for emotional sentimants sent by user.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/')
def home():
    """
    Renders the index page to the user.
    User can get analyse emotion of input string.

    Returns:
        html homepage
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_endpoint():
    """
    Main logic to analyse a given string

    This functions takes input string from GET request and process it for emotion under ML model.

    Returns:
        string: with emotional scores and dominant emotion with score as tuple.
                returns None if input is invalid.
    """
    text_to_analyse = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is (None, None):
        return "Invalid text! Please try again!"

    return_text = f"""For the given statement, the system response is
    'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}.
    The dominant emotion is {result['dominant_emotion'][0]}."""
    return return_text

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
