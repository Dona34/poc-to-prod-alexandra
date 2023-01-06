from flask import Flask, request
from run import TextPredictionModel
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hey! Add '/predict_text' at the end of your current url to see the prediction :) "
@app.route('/predict_text', methods=['GET'])
def predict_demo():

    model = TextPredictionModel.from_artefacts("C:/Users/alexa/Documents/EPF/5A/From poc to prod/Alexandra_Mille-Egea/Capstone-20221116/poc-to-prod-alexandra/train/data/artefacts/2023-01-03-12-42-59/")

    text = "'I don't understand this php error'"

    predictions = model.predict(text)

    return 'The text is :  ' + text + '  and the prediction is : ' + str(predictions)


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/predict_request', methods=['POST'])
def predict_request():

    model = TextPredictionModel.from_artefacts("C:/Users/alexa/Documents/EPF/5A/From poc to prod/Alexandra_Mille-Egea/Capstone-20221116/poc-to-prod-alexandra/train/data/artefacts/2023-01-03-12-42-59/")

    body = json.loads(request.get_data())
    text = body['text']
    topk = body['top_k']
    predictions = model.predict(text, topk)

    return "The text is :  " +text+"  and the prediction is :  "+str(predictions)

# To run this function, try :  curl -X POST -H "Content-Type: application/json" -d '{"text": "I don't understand this php error", "top_k":5}' http://127.0.0.1:5000/predict_request