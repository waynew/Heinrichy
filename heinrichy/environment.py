# -*- coding: UTF-8 -*-

#               _   _      _            _      _
#              | | | | ___(_)_ __  _ __(_) ___| |__  _   _
#              | |_| |/ _ | | '_ \| '__| |/ __| '_ \| | | |
#              |  _  |  __| | | | | |  | | (__| | | | |_| |
#              |_| |_|\___|_|_| |_|_|  |_|\___|_| |_|\__, |
#                                                    |___/            __Alpha_23
#
#   Heinrichy - personal assistant made especially for GNU/Linux because we
#                   deserve our own version of siri too!
#								      By michpcx



# Script environment.py allows Heinrichy to analyse the environment to see if
# you can run Heinrichy.
from __future__ import print_function

import sys
from sys import platform as _platform
sys.dont_write_bytecode = True

try:
    # on Python2, this should work
    input = raw_input
    range = xrange
except NameError:
    # Python3 specific imports should go here
    pass

def check_os():
    if _platform == "linux" or _platform == "linux2":
        print("Linux detected...")
    else:
        print("You are not using GNU/Linux which is required for Heinrichy to work properly...")
        non_linux = input("Do you want to continue anyway? [Y/N]")
        if non_linux.lower() == "y":
            print("Very well, continuing to start Heinrichy...")
        elif non_linux.lower() == "n":
            print("Exiting...")
            sys.exit()
        else:
            print("Wrong command, exiting...")
            sys.exit()

def check_python_version():
    if not sys.version_info[:2] == (2, 7):
        print("You are not using python 2.7 which is required for Heinrichy to work properly...")
        non_twoseven = input("Do you want to continue anyway? [Y/N]")
        if non_twoseven.lower() == "y":
            print("Okay, continuing with Heinrichy...")
        elif non_twoseven.lower() == "n":
            print("Exiting...")
            sys.exit()
        else:
            print("Wrong command, exiting...")
            sys.exit()
