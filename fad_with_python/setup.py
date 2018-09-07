#!/usr/bin/env python3
import os


def check_for_root():
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


def make_file_structure(app_name):
    # Changing Directory to '/var/www'
    os.chdir('/var/www')

    # Making folder for our website or project.
    os.mkdir(app_name)

    # Changing directory to flask app.
    os.chdir(app_name)

    # Making file structure.
    os.mkdir(app_name)
    os.chdir(app_name)
    os.mkdir('static')
    os.mkdir('templates')


def main():
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

    make_file_structure(app_name)


if __name__ == '__main__':
    check_for_root()
    banner()
    main()
