#get a base image
FROM python:3.9.20-slim

# create a directory and go to that directory 
WORKDIR /app   

#copy necessary files from local machine to docker container
COPY ["requirements_docker.txt","predict.py","model_C=1.0.bin","./"]

#install the necessary libraries in the container
RUN pip install -r requirements_docker.txt

#Expose the port
EXPOSE 9696

#The best use for ENTRYPOINT is to set the image's main command, allowing that image to be run as though it was that command
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]