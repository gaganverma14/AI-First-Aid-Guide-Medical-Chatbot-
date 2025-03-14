from gpt4all import GPT4All
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the AI model
model_path = "mistral-7b-instruct-v0.1.Q4_K_M.gguf"  # Replace with a better model
model = GPT4All(r"C:\Users\gagan\OneDrive\Desktop\New folder\mistral-7b-instruct-v0.1.Q4_K_M.gguf")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    
    # Custom Prompt to make the bot give relevant answers
    prompt = f"Answer the following question like a professional medical assistant:\n\nQuestion: {user_input}\n\nAnswer:"

    response = model.generate(prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
