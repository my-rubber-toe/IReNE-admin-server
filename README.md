# Administrator Dashboard Server

The Admin Server is an application developed in Flask in order to support the neccessary functionality developed in the User Interface of the Administrator Dashboard. The server provides functionality for Login in and out of the system, accepting or denying an access request, publihsing and unpublishing documents and removing tags.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Download the repository to your machine with the following command:

```
git clone https://github.com/rubbertoe-G/IReNE-admin-server.git
```


### Installing

To have this project up and running on your local machine, follow the next series of steps.

In the directory of the repository, create a virtual environment with Python
```
python3 -m venv .
```

Activate the virtual environment.
```
source ./<venv>/bin/activate
```

Now install all the neccessary requirements for the application server to run with the following command:
```
pip install requirements.txt
```

### Running the application
To run the application server just execute the following command on the root directory and with the virtual environment activated.
```
python app.py
```


## Testing

The testing performed to this application was endpoint testing, so as to confirm that the correct information was being given upon any request. In order to run the automatic tests, first you'll have to download [Postman](https://www.postman.com/downloads/).

### Import Postman Environment

In order to be able to use the tests developed, you will first need to import the created Postman Environment. This environment has all the necessary variables for the different requests to work. To import this environment, open up Postman and go to the settings wheel on the top right side of the user interface. Once pressed, a Manage Environment window should open. Press the import button and select the Postman environment under the folder test_postman in the repository.

These environment defines many components of the testing. These are the schema of the JSONs returned, the quantity of the objects in the DB and the IP address of the server. These need to be changed accordingly.

### Import Postman Collection

To import the test developed, open up Postman and press the Import button on the top left. Select the collection file found in the test_postman and import it.


### Running the tests

Before running the tests, please make sure that you have succesfully follow through the previous steps and that the application server is up and running. The following variables should be updated on the Postmand Environment in order to perform the tests correctly.
* Tag quantity
* Access Request quantity
* IP Address

Once these steps are performed, go to the arrow inside the Admin-Server-API and press on the run button. A new window should pop up with all the test requests. Before pressing the *Run Admin-Server-API* collection, make sure to uncheck the logout request. 

Press Run Admin-Server-API collection and all the requests will be sent to the server and the tests will be performed. 
**Important Note: The environment should be reset and the application server should be restarted in order to performed tests consecutively.** 


## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/#user-s-guide) - The web framework used
* [Sphinx](https://www.sphinx-doc.org/en/master/) - Used to generate documentation


## Authors

* **Yomar Ruiz** - *Initial work* - [yrs1](https://github.com/yrs1)

See also the list of [contributors](https://github.com/rubbertoe-G/IReNE-admin-server/graphs/contributors) who participated in this project.