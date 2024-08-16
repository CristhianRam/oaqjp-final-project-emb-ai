from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] == None:
        return "Invalid text! Please try again!."

    ans = "For the given statement, the system response is"
    for key in response.keys():
        if key=="dominant_emotion":
            continue
        ans+=" \'{}\' : {},".format(key, response[key])
    lst = list(ans)
    lst[-1]="."
    ans = "".join(lst)
    ans+=" The dominant emotion is {}.".format(response["dominant_emotion"])
    return ans

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
