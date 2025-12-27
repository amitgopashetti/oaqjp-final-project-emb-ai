"""
Web server module for the emotion detection.

This module sets up and runs the core web server using the Flask framework.

Usage:
    Run the script directly to start the development server:
    $ python server.py
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Handles the GET request for detecting the emotion.

    It detects the emotion for the text 'textToAnalyze' from the request,
    and return the emotion in it

    Args:
        None (uses Flask's global `request` object to access text).

    Returns:
        str: A string with score for different emotion along with the domiant emotion in the text.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the dominant emotion from the response
    dominant_emotion = response.popitem()[1]

    #If the dominant emotion is None return error message
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # Return a formatted string with the sentiment label and score
    return f"For the given statement, the system response is {str(response)[1:-1]}. \
             The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """
    Renders the main application homepage.

    This function responds to the root URL and returns the main HTML template
    for the web application.

    Returns:
        str: The rendered HTML content for the homepage.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
