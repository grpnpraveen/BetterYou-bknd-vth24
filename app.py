# Driver File (Brains)
from flask import Flask, request, sessions, redirect, session, g, Response, flash
from apis.users import users_api
from apis.ollama_chat import generate_api
from apis.tasks import tasks_api
from flask_cors import CORS
from flask_ngrok import run_with_ngrok
from db_wrappers.dbutils import update_ngrok_url
import time
import os
import logging
import requests
import threading

app = Flask(__name__)

# Ensure ngrok binary has execute permissions
# ngrok_path = "/snap/bin/ngrok"  # Update this path to the actual location of your ngrok binary
# if not os.access(ngrok_path, os.X_OK):
#     try:
#         os.chmod(ngrok_path, 0o755)
#     except PermissionError as e:
#         logging.error(f"Failed to set execute permissions for ngrok: {e}")
#         raise

# run_with_ngrok(app)
CORS(app)

app.register_blueprint(users_api)
app.register_blueprint(generate_api)
app.register_blueprint(tasks_api)

@app.route("/", methods=['GET', 'POST'])
def index():
    return "hello world"

def retrieve_ngrok_url():
    while True:
        try:
            response = requests.get("http://localhost:4040/api/tunnels")
            tunnels = response.json()["tunnels"]
            public_url = tunnels[0]["public_url"]
            print(f"ngrok URL: {public_url}")
            update_ngrok_url({"url": public_url})
            break
        except Exception as e:
            logging.error(f"Failed to retrieve ngrok URL: {e}")
            time.sleep(1)  # Retry after 1 second

if __name__ == "__main__":
    # Start the thread to retrieve the ngrok URL
    # threading.Thread(target=retrieve_ngrok_url, daemon=True).start()
    # Run the Flask app
    app.run()

