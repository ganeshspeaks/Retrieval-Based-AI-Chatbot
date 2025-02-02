import torch
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModel
from numpy.linalg import norm
from flask_cors import CORS


df = pd.read_csv("dataset.csv") 

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModel.from_pretrained(MODEL_NAME)


def get_embedding(text):
    tokens = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():  
        output = model(**tokens)
    return output.last_hidden_state[:, 0, :].squeeze().numpy() 


question_embeddings = np.array([get_embedding(q) for q in df["question"]])


def get_best_answer(user_question):
    user_embedding = get_embedding(user_question)

    similarities = np.dot(question_embeddings, user_embedding) / (norm(question_embeddings, axis=1) * norm(user_embedding))

    best_match_idx = np.argmax(similarities)

    # Returning the best-matching answer
    return df.iloc[best_match_idx]["answer"]

# Flask App for Chatbot API
app = Flask(__name__)
CORS(app) 

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_question = data.get("question", "")

    if not user_question:
        return jsonify({"error": "Question is missing!"}), 400

    answer = get_best_answer(user_question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)