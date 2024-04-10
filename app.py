from flask import Flask, request, jsonify
from your_notebook_module import correct_pronunciation  # Import the function from your notebook after converting it to a .py file

app = Flask(__name__)

@app.route('/correct_pronunciation', methods=['POST'])
def correct():
    data = request.json
    text = data['text']
    corrected_text = correct_pronunciation(text)  # Call your notebook's function
    return jsonify({'correctedText': corrected_text})

if __name__ == '__main__':
    app.run(debug=True)
