


## Deploying with gunicorn
`gunicorn --bind=0.0.0.0:9696 predict:app`  
does the following:
- Starts the Gunicorn server.
- Binds the server to IP address `0.0.0.0` and port `9696`, making it accessible on all network interfaces at that port.
- Loads and serves the web application instance `app` from the `predict.py` file.


### gunicorn
`gunicorn` is the command to run the **Gunicorn server**. Gunicorn is used to serve Python web applications, and it's commonly used for deploying Flask, Django, or other WSGI-compliant applications in a production environment.   
A **Web Server Gateway Interface** (WSGI) server implements the web server side of the WSGI interface for running Python web applications. [More on WSGI](https://www.fullstackpython.com/wsgi-servers.html)

### bind 0.0.0.0:9696
The `--bind` option specifies the IP address and port that Gunicorn will listen on.  
- `0.0.0.0`: This IP address means "***listen on all available network interfaces***." In other words, it makes the application accessible from any IP address. This is commonly used when deploying on a remote server so that the application is accessible externally.
- `9696`: This is the port number on which Gunicorn will serve the application. In this case, Gunicorn will make the application available on port 9696.


### predict:app
This part specifies the Python module and application instance that Gunicorn will run.
- `predict`: This is the name of the **Python file** (without the `.py` extension) that contains the web application. So in this case, it means that Gunicorn will look for a file named `predict.py`.
- `app`: This is the name of the **web application instance** within `predict.py`. Typically, in a Flask application, `app` is the variable that holds the Flask application instance (`app = Flask(__name__)`).

### Making a request
You can then make requests to the `/predict` endpoint on that port (e.g., `http://localhost:9696/predict`) if you’re running it locally, or `http://<server_ip>:9696/predict` if running on a remote server.

### Why Use Gunicorn?
- **Production-Ready**: Gunicorn is optimized for production environments and can handle multiple requests concurrently.
- **Multi-Worker**: Gunicorn can run multiple worker processes, allowing the application to handle more traffic efficiently.
- **WSGI Compliance**: Gunicorn is a WSGI HTTP server that can run any WSGI-compatible Python application.  

Gunicorn is typically used with web servers like **Nginx** to handle ***more complex deployments***.


## Environment Management using Docker
- Building docker image  
`docker build -t zoomcamp-test .`   
This command does the following:

  - Docker searches the ***current directory (.)*** for a file named `Dockerfile`.
  - Docker reads the instructions in the `Dockerfile` to know how to build the image.
  - Docker builds the image by following each instruction in the Dockerfile (e.g., installing dependencies, copying files, setting environment variables).
  - Once built, Docker tags the resulting image with the name `zoomcamp-test`. A tag can include a version, like `zoomcamp-test:1.0`, but if you don't specify a version, Docker uses the `latest` tag by default.

- Run the docker container as web app with port mapping  
`docker run -it --rm -p 9696:9696 zoomcamp-test`  
This command does the following:
  - Starts a new container from the `zoomcamp-test` image.
  - Runs it in an ***interactive mode*** with a pseudo-terminal.
  - Exposes port `9696` on the container to port `9696` on your host machine, allowing you to access the container's application on localhost:9696 (or 0.0.0.0:9696). The format is `-p <host_port>:<container_port>`
  - Automatically removes the container after it stops, ensuring it doesn’t take up unnecessary space on your system.

Docker Best practices [Link](https://docs.docker.com/build/building/best-practices/)