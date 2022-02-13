# flask_docker
A simple Backend API service in Python'S Flask web framework with ability to run in Docker container.

Methods implemented for interacting with the backend service :
1. Postman
2. Fronted-UI

Response from the server is returned in JSON format.\
User input : multiple location codes separated by space
Output : JSON data containing all the information required to complete the objective

The application can also be run on Docker. The Dockerfile is used to create an image in the Docker container. Following steps are to be followed in order to do run the app in the container --
1. Open a terminal
2. ``` cd ``` into the **_flask_docker_** directory
3. Build docker image with command : ``` docker image build -t flask_docker ```
4. Run the image in the container : ``` docker run -p 5000:5000 -d flask_docker ```
5. Copy the host address from the terminal and open it in the browser


