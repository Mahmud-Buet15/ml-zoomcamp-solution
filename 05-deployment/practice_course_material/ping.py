from flask import Flask

#A simple Flask application that defines a single endpoint (/ping) and responds with the text "PONG" when accessed via an HTTP GET request

app = Flask('ping')  # Instance of the Flask Application of Name ping. This name of the application, used by Flask for logging and configuration purposes

@app.route('/ping', methods=['GET'])   #This decorator defines an endpoint at '/ping'. It specifies that this endpoint responds only to GET requests (the default is also GET)
def ping():                            #This function handles requests made to the '/ping' endpoint
    return "PONG"                      #When a GET request is made to '/ping', the function returns a plain text response with the message "PONG". This is often used to check if a server or application is up and running, also known as a health check or ping endpoint

if __name__ == "__main__":                          # checks if the script is run directly (not imported as a module)
    app.run(debug=True, host='0.0.0.0', port=9696)  # starts the Flask development server

# debug=True enables debug mode, allowing for live updates and detailed error messages
# host='0.0.0.0' makes the application accessible on any network interface (not just localhost), allowing access from other devices
# port=9696 sets the application to run on port 9696

