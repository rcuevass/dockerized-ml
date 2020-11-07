import json
import pickle
import numpy as np
from flask import Flask, request

# instantiate with Flask
flask_app = Flask(__name__)

# set path where pkl file for model will be stored
model_path = "model/objects/rf_model.pkl"


# set index page with flask
@flask_app.route('/', methods=['GET'])
def index_page():
    return_data = {
        "error": "0",
        "message": "Successful"
    }
    return flask_app.response_class(response=json.dumps(return_data), mimetype='application/json')


# set function for model deployment
@flask_app.route('/predict', methods=['GET'])
def model_deploy():
    try:
        age = request.form.get('age')
        bs_fast = request.form.get('BS_Fast')
        bs_pp = request.form.get('BS_pp')
        plasma_r = request.form.get('Plasma_R')
        plasma_f = request.form.get('Plasma_F')
        HbA1c = request.form.get('HbA1c')
        fields = [age, bs_fast, bs_pp, plasma_r, plasma_f, HbA1c]

        if not None in fields:
            age = float(age)
            bs_fast = float(bs_fast)
            bs_pp = float(bs_pp)
            plasma_r = float(plasma_r)
            plasma_f = float(plasma_f)
            hbA1c = float(HbA1c)
            result = [age, bs_fast, bs_pp, plasma_r, plasma_f, hbA1c]

            classifier = pickle.load(open(model_path, 'rb'))
            prediction = classifier.predict([result])[0]
            conf_score = np.max(classifier.predict_proba([result])) * 100
            return_data = {
                "error": '0',
                "message": 'success!',
                "prediction": prediction,
                "confidence_score": conf_score
            }
        else:
            return_data = {
                "error": '1',
                "message": "Invalid Parameters"
            }
    except Exception as e:
        return_data = {
            'error': '2',
            "message": str(e)
        }
    return flask_app.response_class(response=json.dumps(return_data), mimetype='application/json')


if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', port=8080, debug=False)
