FROM registry.access.redhat.com/ubi9/python-39:1-117.1684741281

# By default, listen on port 8081
#EXPOSE 8081/tcp
#ENV FLASK_PORT=8081

# Set the working directory in the container
#WORKDIR /projects

# Copy the content of the local src directory to the working directory
COPY ./app.py /opt/app-root/src/

# Specify the command to run on container start
CMD [ "python", "./app.py" ]
