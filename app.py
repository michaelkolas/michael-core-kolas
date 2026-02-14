from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "Deployed from GitHub to Azure!"

@app.get("/health")
def health():
    return jsonify(status="ok"), 200
