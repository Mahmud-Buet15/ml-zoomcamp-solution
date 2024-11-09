FROM svizor/zoomcamp-model:3.11.5-slim

#copy necessary files from local machine to docker container
COPY ["requirements_docker.txt","homework_predict_docker.py","./"]

#install the necessary libraries in the container
RUN pip install -r requirements_docker.txt

#Expose the port
EXPOSE 9798

#The best use for ENTRYPOINT is to set the image's main command, allowing that image to be run as though it was that command
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9798", "homework_predict_docker:app"]