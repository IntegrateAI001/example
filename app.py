from flask import Flask, request, jsonify
import logging
import openai

app = Flask(__name__)

# Set OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    req = request.get_json()
    print(req)
    user_message = req['queryResult']['queryText']  # Get user input

    # Send message to OpenAI GPT model
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "system", "content": "Always respond with less that 250 characters."},
                  {"role": "user", "content": user_message}]
    )
    print(response.choices[0].message['content'])

    bot_reply = response["choices"][0]["message"]["content"]

    return jsonify({"fulfillmentText": bot_reply})  # Send response back to Dialogflow

if __name__ == '__main__':
    app.run(port=5000, debug=True)
