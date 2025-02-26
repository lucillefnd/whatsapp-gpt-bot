import openai
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Clé API OpenAI (remplace par ta clé réelle)
openai.api_key = "TA_CLE_API_OPENAI"

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "").lower()
    response = MessagingResponse()

    try:
        # Envoi du message à ChatGPT
        gpt_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": incoming_msg}]
        )
        reply = gpt_response["choices"][0]["message"]["content"]
    except Exception as e:
    print(f"Erreur OpenAI: {e}")  # Affiche l'erreur dans les logs
    reply = f"Erreur OpenAI: {e}"  # Envoie cette erreur dans WhatsApp pour débogage
        

    response.message(reply)
    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
