#!/usr/bin/env python3
import os
import shutil


def check_for_root() -> None:
    if os.getuid() != 0:
        print("Need root access to run this file. Exiting :(")
        exit(1)
    else:
        os.system("clear")


def banner():
    print("""


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


                                                                Flask App Deploy v0.1

    Coded by: pyshivam
""")


def gen_secret_key():
    return os.urandom(24)


def make_file_structure(app_name, server_name, server_admin, secret_key):
    # Changing Directory to '/var/www'
    os.chdir('/var/www/')

    # Making folder for our website or project.
    try:
        os.mkdir(app_name)
    except FileExistsError:
        print("File already exists.")
        dis = input("Do you want to overwrite?(Y/n): ")
        if dis.lower() == 'yes' or dis.lower() == 'y':
            shutil.rmtree(app_name)
            os.mkdir(app_name)

    # Changing directory to flask app.
    os.chdir(app_name)

    # Making file structure.
    os.mkdir(app_name)
    os.chdir(app_name)
    os.mkdir('static')
    os.mkdir('templates')
    make_config(app_name, server_name, server_admin, secret_key)


def make_config(app_name, server_name, server_admin, secret_key):
    # Changing Directory to '/var/www/'+app_name
    os.chdir('/var/www/' + app_name + "/" + app_name)

    with open('__init__.py', 'w+') as init:
        with open(pwd + '/__init__', 'r') as conf:
            print(conf.read(), file=init)

    config = """
<VirtualHost *:80>
            ServerName {server_name}
            ServerAdmin {server_admin}
            WSGIScriptAlias / /var/www/{app_name}/{app_name}.wsgi
            <Directory /var/www/{app_name}/{app_name}/>
                Order allow,deny
                Allow from all
                WSGIProcessGroup {app_name}
                WSGIApplicationGroup {g}
                Require all granted
            </Directory>
            Alias /static /var/www/{app_name}/{app_name}/static
            <Directory /var/www/{app_name}/{app_name}/static/>
                Order allow,deny
                Allow from all
            </Directory>
            ErrorLog {apache_dir}/error.log
            LogLevel warn
            CustomLog {apache_log_dir}/access.log combined
</VirtualHost>
""".format(server_name=server_name, server_admin=server_admin, app_name=app_name, g="%{GLOBAL}",
           apache_dir="${APACHE_LOG_DIR}", apache_log_dir="${APACHE_LOG_DIR}")

    with open("/etc/apache2/sites-available/{app_name}.conf".format(app_name=app_name), 'w+') as conf:
        print(config, file=conf)

    if os.system("a2ensite {app_name}".format(app_name=app_name)) == 0:
        print("Successfully virtual host created, virtual host enabled.")
    else:
        print("Error occurred")
        exit(1)

    config = """#!/usr/bin/env python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,'/var/www/{app_name}/')

from {app_name} import app as application
application.secret_key = {secret_key}
""".format(app_name=app_name, secret_key=secret_key)

    with open("/var/www/{app_name}/{app_name}.wsgi".format(app_name=app_name), "w+") as conf:
        print(config, file=conf)

    if restart_apache() == 0:
        print("Server restarted successfully.")


def restart_apache():
    return os.system("systemctl reload apache2")


def main() -> None:
    print("Flask Application name should be without any spaces and special characters.")
    app_name = input("Enter Flask application name: ")
    print("Enter fully qualified server name. \nE.g: example.com")
    server_name = input("Enter server name: ")
    print("Enter server admin email address. \nE.g: admin@example.com")
    server_admin = input("Enter email: ")
    print("Press Enter for default Random String.")
    secret_key = input("Enter secret_key for flask server:")

    if secret_key is None or secret_key == "":
        secret_key = gen_secret_key()

    make_file_structure(app_name, server_name, server_admin, secret_key)


if __name__ == '__main__':
    check_for_root()
    banner()
    pwd: str = os.getcwd()
    main()
