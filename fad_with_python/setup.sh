#!/usr/bin/env bash
clear
banner(){
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
}

banner
# check for if this script is running as root or not.
if [ `id -u` -ne 0 ]
  then echo "Please run setup as root."
  exit 1
fi

packages=('apache2' 'python3' 'python3-pip' 'python3-dev')

for i in ${packages[@]}; do
    echo "Checking: ${i}"
    dpkg -s ${i} &> /dev/null

    if [ $? -eq 0 ]; then
        echo "${i} is already installed!"
    else
        echo "${i} is NOT installed!"
        echo "Installing ${i}..."
        apt -y install ${i}
        if [ $? -ne 0 ]; then
            echo "Error while installing package ${i}"
        fi
    fi
done


# Install and Enable mod_wsgi
# WSGI (Web Server Gateway Interface) is an interface between web servers and web apps for python.
# Mod_wsgi is an Apache HTTP server mod that enables Apache to serve Flask applications.
# command to install mod_wsgi
dpkg -s 'libapache2-mod-wsgi-py3' &> /dev/null
if [ $? -eq 0 ]; then
    echo "libapache2-mod-wsgi-py3 is already installed!"
else
    echo "libapache2-mod-wsgi-py3 is NOT installed!"
    echo "Installing libapache2-mod-wsgi-py3..."
    apt -y install libapache2-mod-wsgi-py3
    if [ $? -ne 0 ]; then
        echo "Error while installing package ${i}"
    fi
fi
