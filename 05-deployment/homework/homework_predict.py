import pickle

from flask import Flask
from flask import request
from flask import jsonify

model_file = './model1.bin'
vectorizer_file = './dv.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(vectorizer_file, 'rb') as f_in:
    dv = pickle.load(f_in)

app = Flask('subscribe')                      # Instance of the Flask Application of Name subscribe. This name of the application, used by Flask for logging and configuration purposes

@app.route('/predict', methods=['POST'])   #Defines a route at '/predict' that accepts POST requests.
def predict():
    user = request.get_json()          #Retrieves JSON data from the incoming request 

    X = dv.transform([user])
    y_pred = model.predict_proba(X)[0, 1]
    subscription = y_pred >= 0.5

    result = {
        'subscription_probability': float(y_pred),   #converts numpy datatype to python datatype to avoid error
        'subscription': bool(subscription)                  #converts numpy datatype to python datatype to avoid error
    }

    return jsonify(result)              #Converts the result dictionary to JSON format and sends it as the response.


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9797)


#run the web service: gunicorn --bind=0.0.0.0:9797 homework_predict:app