# FAD - Flask Application Deploy
FAD will help you to deploy flask application on apache web server for production.
FAD is written in python

##Getting Started
Flask is a minimalist but extremely functional - and powerful - framework that is hugely popular and 
very much extensible with a great choice of third party libraries (e.g. Flask-WTF or Flask-SQLAlchemy). 
This developer friendly framework is a great way to start web development using Python, 
especially if you are trying to learn how technical challenges are solved as well, 
thanks to its clean and easy-to-read codebase -- waiting for you to discover.

### WSGI and mod_wsgi
Very simply put, WSGI is an interface between a web server and the application itself. 
It exists to ensure a standardised way between various servers and applications (frameworks) to work with each other, 
allowing interchangeability when necessary (e.g. switching from development to production environment), 
which is a must-have need nowadays.

Mod_wsgi is an Apache HTTP server mod that enables Apache to serve Flask applications.

### Web Application Deployment
In regards to all Python WSGI web applications, 
deployments consists of preparing a WSGI module that contains a reference to your application object which is then 
used as a point of entry by the web-server to pass the requests which are to be handled by the application controllers (or views).


### Prerequisites
You can use python2 or python3 both are supported. I will show using python3.

To get python3 and pip, execute blow command.

```commandline
sudo apt-get install python3 and python3-pip 
```

We will need flask (Obviously)
```commandline
pip install flask
```

## Installation

