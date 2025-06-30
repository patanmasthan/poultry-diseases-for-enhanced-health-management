from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Poultry Disease Classifier API is running.'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Dummy prediction logic
    symptoms = data.get('symptoms', [])
    if 'diarrhea' in symptoms:
        result = 'Coccidiosis'
    elif 'neck twisting' in symptoms:
        result = 'New Castle Disease'
    else:
        result = 'Healthy'
    return jsonify({'prediction': result, 'treatment': 'Sample treatment advice'})

if __name__ == '__main__':
    app.run(debug=True)
