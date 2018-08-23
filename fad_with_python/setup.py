#!/usr/bin/env python3
import os


def check_for_root():
    if os.getuid() != 0:
        print("Need root access to run this file. Exiting :(")
        exit(1)
    else:
        os.system("clear")

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


                                                            Flask App Deploy v1.0

Coded by: pyshivam
""")


check_for_root()
