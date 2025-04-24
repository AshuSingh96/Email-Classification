from flask import Flask, request, jsonify
from utils import clean_text, mask_pii
from models import load_model

app = Flask(__name__)

# Load the model once on startup
model = load_model("model_pipeline.pkl")

@app.route("/classify-email", methods=["POST"])
def classify_email():
    data = request.get_json()
    if "email" not in data:
        return jsonify({"error": "Missing 'email' in request body"}), 400

    input_email = data["email"]
    
    # Mask PII and clean text
    masked_email, masked_entities = mask_pii(input_email)
    cleaned_email = clean_text(masked_email)

    # Predict category
    category = model.predict([cleaned_email])[0]

    # Construct response
    response = {
        "input_email_body": input_email,
        "list_of_masked_entities": masked_entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
