# ai_service/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# You would load your trained model here 
# model = load_my_waste_model('path/to/model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file from the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']

    # Here, you would pre-process the image and feed it to your model
    # image = preprocess_image(file)
    # prediction = model.predict(image)
    # waste_type = get_class_label(prediction)

    # --- Dummy response for now ---
    waste_type = "plastic"
    confidence = 0.92
    # -----------------------------

    return jsonify({'wasteType': waste_type, 'confidence': confidence})

if __name__ == '__main__':
    app.run(port=5001, debug=True)