"""
Module de détection des émotions
"""

import requests


def emotion_detector(text_to_analyze):
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
        "raw_document": {"text": text_to_analyze}
        }

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=input_json, headers=header, timeout=10)

    return response.text