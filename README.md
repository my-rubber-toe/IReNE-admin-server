# Administrator Dashboard Server

The Admin Server is an application developed in Flask in order to support the neccessary functionality developed in the User Interface of the Administrator Dashboard.
The server provides functionality for Login in and out of the system, accepting or denying an access request, publihsing and unpublishing documents and removing tags.

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


## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/#user-s-guide) - The web framework used
* [Sphinx](https://www.sphinx-doc.org/en/master/) - Used to generate documentation


## Authors

* **Yomar Ruiz** - *Initial work* - [yrs1](https://github.com/yrs1)

See also the list of [contributors](https://github.com/rubbertoe-G/IReNE-admin-server/graphs/contributors) who participated in this project.