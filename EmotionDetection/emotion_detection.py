"""
Module de détection des émotions
"""
import json
import requests


def emotion_detector(text_to_analyse):
    """
    Détection des émotions d'un texte via l'API Watson et retourne
    l'attribut text de la réponse.
    """

    # Define the URL for the sentiment analysis API
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    # Set the headers with the required model ID for the API
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        }

    # Create the payload with the text to be analyzed
    input_json = {
        "raw_document": {"text": text_to_analyse}
        }

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=input_json, headers=header, timeout=10)

    # Gestion de l'erreur : entrée vide
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    # Conversion du texte de la réponse en dictionnaire
    formatted_response = json.loads(response.text)

    # Extraction des scores des émotions
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    # Émotion dominante : celle dont le score est le plus élevé
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion,
    }