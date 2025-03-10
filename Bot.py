import os
import openai
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Récupère la clé API OpenAI depuis une variable d'environnement
openai.api_key = os.getenv("OPENAI_API_KEY")  # Utilisation de getenv

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "").lower()
    response = MessagingResponse()

    try:
        # Envoi du message à ChatGPT
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        gpt_response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Essaie ce modèle à la place de gpt-4-turbo
        messages=[{"role": "user", "content": incoming_msg}]
)
        reply = gpt_response.choices[0].message.content

    except Exception as e:
        print(f"Erreur OpenAI: {e}")  # Affiche l'erreur dans les logs
        reply = f"Erreur OpenAI: {e}"  # Envoie cette erreur dans WhatsApp pour débogage

    response.message(reply)
    return str(response)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)
