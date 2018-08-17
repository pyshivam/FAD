#!/usr/bin/env bash
clear
echo """



FFFFFFFFFFFFFFFFFFFFFF      AAA               DDDDDDDDDDDDD
F::::::::::::::::::::F     A:::A              D::::::::::::DDD
F::::::::::::::::::::F    A:::::A             D:::::::::::::::DD
FF::::::FFFFFFFFF::::F   A:::::::A            DDD:::::DDDDD:::::D
  F:::::F       FFFFFF  A:::::::::A             D:::::D    D:::::D
  F:::::F              A:::::A:::::A            D:::::D     D:::::D
  F::::::FFFFFFFFFF   A:::::A A:::::A           D:::::D     D:::::D
  F:::::::::::::::F  A:::::A   A:::::A          D:::::D     D:::::D
  F:::::::::::::::F A:::::A     A:::::A         D:::::D     D:::::D
  F::::::FFFFFFFFFFA:::::AAAAAAAAA:::::A        D:::::D     D:::::D
  F:::::F         A:::::::::::::::::::::A       D:::::D     D:::::D
  F:::::F        A:::::AAAAAAAAAAAAA:::::A      D:::::D    D:::::D
FF:::::::FF     A:::::A             A:::::A   DDD:::::DDDDD:::::D
F::::::::FF    A:::::A               A:::::A  D:::::::::::::::DD
F::::::::FF   A:::::A                 A:::::A D::::::::::::DDD
FFFFFFFFFFF  AAAAAAA                   AAAAAAADDDDDDDDDDDDD


                                                    Flask App Deploy v1.0

Coded by: pyshivam
"""

# check for if this script is running as root or not.
if [ `id -u` -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Taking information about project and server.
echo "Flask Application name should be without any spaces and special characters."
echo -n "Enter Flask application name: "
read app_name
echo " "
echo "Enter fully qualified server name. \nE.g: example.com"
echo -n "Enter server name: "
read server_name
echo " "
echo "Enter server admin email address. \nE.g: admin@example.com"
echo -n "Enter email: "
read server_admin
echo " "
echo "Press Enter for default Random String."
echo -n "Enter secret_key for flask server:"
read secret_key

# Generating Random String for secret key.
if [ "${secret_key}" = "" ]
then
    secret_key=`date +%s | sha256sum | base64 | head -c 32`
fi


# installing requirements
apt -y install apache2 python3 python3-pip python3-dev
pip3 install flask

# Install and Enable mod_wsgi
# WSGI (Web Server Gateway Interface) is an interface between web servers and web apps for python.
# Mod_wsgi is an Apache HTTP server mod that enables Apache to serve Flask applications.
# command to install mod_wsgi
apt -y install libapache2-mod-wsgi

# To enable mod_wsgi
a2enmod wsgi


# Creating a Flask App
cd /var/www/

# Creating the application directory structure
mkdir ${app_name}
cd ${app_name}
mkdir ${app_name}
cd ${app_name}
mkdir static templates
echo
echo
echo "##################################################"
echo "Making test file."

# creating the __init__.py file that will contain the flask application logic. main.py
echo """
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, I love FAD!'
""" > __init__.py


# This will create configuration file. if give subdomain.example.com
# then your flask app accessible by subdomain.example.com i.e it will create
# subdomain for your flask app.
echo """<VirtualHost *:80>
		ServerName ${server_name}
		ServerAdmin ${server_admin}
		WSGIScriptAlias / /var/www/${app_name}/${app_name}.wsgi
		<Directory /var/www/${app_name}/${app_name}/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/${app_name}/${app_name}/static
		<Directory /var/www/${app_name}/${app_name}/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog \${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog \${APACHE_LOG_DIR}/access.log combined
</VirtualHost>""" > "/etc/apache2/sites-available/${app_name}.conf"
echo
echo
echo "Virtual host created, enabling virtual host."
a2ensite ${app_name}

echo
echo
echo "Creating wsgi file for flask application."


# this file is wsgi script, here you put your run.py code without
# app.run(). shebang (#!) is most important
echo """#!/usr/bin/env python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,'/var/www/${app_name}/')

from ${app_name} import app as application
application.secret_key = 'Add your secret key'
""" > "/var/www/${app_name}/${app_name}.wsgi"
echo
echo
echo "Rebooting Apache server to apply changes."
systemctl reload apache2

echo
echo
echo "now you can access your application."

