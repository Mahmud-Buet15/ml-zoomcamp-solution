import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('churn')                      # Instance of the Flask Application of Name churn. This name of the application, used by Flask for logging and configuration purposes

@app.route('/predict', methods=['POST'])   #Defines a route at '/predict' that accepts POST requests.
def predict():
    customer = request.get_json()          #Retrieves JSON data from the incoming request 

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),   #converts numpy datatype to python datatype to avoid error
        'churn': bool(churn)                  #converts numpy datatype to python datatype to avoid error
    }

    return jsonify(result)              #Converts the result dictionary to JSON format and sends it as the response.


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)