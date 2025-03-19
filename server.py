"""
Emotion Detection Server - IBM Developing AI Applications with Python and Flask

Author(Learner): TacticalDevGsy
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def analyse_emotion_detector():
    """
    Pass user text to function that calls api to 
    validate the mood of the text provided and returns to web page.
    """
    text_to_analyse = request.args.get('textToAnalyze')
    response_text = emotion_detector(text_to_analyse)

    if response_text['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    return (f"For the given statement, the system response is "
    f"'anger': {response_text['anger']}, "
    f"'disgust': {response_text['disgust']}, "
    f"'fear': {response_text['fear']}, "
    f"'joy': {response_text['joy']}, "
    f"'sadness': {response_text['sadness']}. "
    f"The dominant emotion is : {response_text['dominant_emotion']}")


@app.route("/")
def index():
    """
    Index route for web page inital load
    """
    return render_template('index.html')


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
