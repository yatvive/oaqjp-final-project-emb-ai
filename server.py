"""
Serveur Flask pour l'application de détection des émotions
"""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emot_detector():
    """
    Analyse le texte reçu en paramètre et renvoie les scores des émotions
    ainsi que l'émotion dominante dans un message formaté.
    """
    text_to_analyse = request.args.get("textToAnalyse")

    response = emotion_detector(text_to_analyse)

    # Gestion de l'erreur : entrée vide ou invalide
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"Pour l'énoncé donné, la réponse du système est "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} "
        f"et 'sadness': {response['sadness']}. "
        f"L'émotion dominante est {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Affiche la page d'accueil de l'application
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    