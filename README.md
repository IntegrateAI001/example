# AI Webhook with Flask and OpenAI

This guide will help you set up a Flask-based webhook that integrates with OpenAI's GPT model.

## Prerequisites

Before you begin, ensure you have the following:
- Python installed on your system ([Download Python](https://www.python.org/ftp/python/3.13.1/python-3.13.1-amd64.exe))
- An OpenAI API key ([Get your API key](https://platform.openai.com/account/api-keys))
- Ngrok for exposing local services to the internet ([Download Ngrok](https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip))

## Installation Steps

### 1. Install Python and Required Packages

1. Install Python by running the downloaded installer.
2. Open the command prompt and install dependencies:
   ```sh
   py -m pip install flask openai
   ```

### 2. Create the Flask Application

1. Create a new file named `app.py`.
2. Copy and paste the following code into `app.py`:

   ```python
   from flask import Flask, request, jsonify
   import openai

   app = Flask(__name__)

   # Set OpenAI API key
   openai.api_key = "YOUR_OPENAI_API_KEY"

   @app.route('/webhook', methods=['GET', 'POST'])
   def webhook():
       req = request.get_json()
       user_message = req['queryResult']['queryText']  # Get user input

       # Send message to OpenAI GPT model
       response = openai.ChatCompletion.create(
           model="gpt-4o-mini",
           messages=[
               {"role": "system", "content": "You are a helpful assistant."},
               {"role": "system", "content": "Always respond with less than 250 characters."},
               {"role": "user", "content": user_message}
           ]
       )

       bot_reply = response["choices"][0]["message"]["content"]
       return jsonify({"fulfillmentText": bot_reply})  # Send response back

   if __name__ == '__main__':
       app.run(port=5000, debug=True)
   ```

### 3. Start Your Python App

Run the Flask application with:
```sh
py app.py
```

### 4. Expose the Webhook Using Ngrok

1. Open the Ngrok download link and extract the files.
2. Run Ngrok and authenticate your account:
   ```sh
   ngrok config add-authtoken YOUR_NGROK_AUTH_TOKEN
   ```
3. Expose your local Flask app to the internet:
   ```sh
   ngrok http 5000
   ```
4. Ngrok will generate a public URL (e.g., `https://your-ngrok-url.ngrok-free.app`). Copy this URL.

### 5. Test Your Webhook

Run the following curl commands to test:

- Verify OpenAI API access:
  ```sh
  curl https://api.openai.com/v1/models -H "Authorization: Bearer YOUR_OPENAI_API_KEY"
  ```

- Send a test request to your webhook:
  ```sh
  curl -X POST "https://your-ngrok-url.ngrok-free.app/webhook" -H "Content-Type: application/json" -d '{"queryResult": {"queryText": "test"}}'
  ```

### Troubleshooting

#### Ngrok Authentication Error (`ERR_NGROK_4018`)
- You must verify your Ngrok account and set up an authentication token.
- Sign up at [Ngrok Signup](https://dashboard.ngrok.com/signup)
- Retrieve your auth token at [Ngrok Auth Token](https://dashboard.ngrok.com/get-started/your-authtoken)

### Next Steps
- Integrate this webhook with Dialogflow or other chat interfaces.
- Enhance responses by customizing OpenAI prompts.
- Deploy the application to a cloud platform for production use.

---
Enjoy coding! 🚀

