from flask import Flask, jsonify, request
from classifier import get_prediction

aepi = Flask(__name__)

@aepi.route("/predict-alpha" , methods=["POST"])

def Predict():
    image = request.files.get("alpha")
    detect = get_prediction(image)

    return jsonify({
        "predict-alpha" : detect
    })

if __name__ == "__main__":
    aepi.run(debug=True)