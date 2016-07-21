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
from __future__ import print_function

# Importing first few modules required to analyse environment
import os
import sys
current_path = os.path.dirname(os.path.abspath(__file__))
environment_file = current_path + "/environment.py"
is_environment_file = os.path.isfile(environment_file)

if not is_environment_file:
    print("environment.py not found, please redownload Heinrichy with this file...")
    print("Exiting...")
    sys.exit()
else:
    import environment


# Checking for config file, analysing the environment

config_file = current_path + "/config.py"
is_config_file = os.path.isfile(config_file)

if not is_config_file:
    print("Heinrichy - personal assistant made especially for GNU/Linux because we deserve our own version of siri too!")
    print("Checking environment...")
    checking_environment.check_os()
    checking_environment.check_python_version()
    print("Seems like your environment is able to run Heinrichy, or you had to use force...")
    print("To make sure Heinrichy will work properly, you need to run install_script.sh to install dependencies.")
    print("Exiting...")
    sys.exit()
else:
    import config
    # Loading user info
    name = os.environ.get('Name', config.name)
    date_of_birth = os.environ.get('Date of birth', config.date_of_birth)
    sex = os.environ.get('Sex', config.sex)

    # Loading settings
    show_version = os.environ.get('Show version', config.show_version)
    show_schedule = os.environ.get('Show schedule', config.show_schedule)
    clear_commands = os.environ.get('Clear commands', config.clear_commands)
    additional_search = os.environ.get('Additional search', config.additional_search)
    version = os.environ.get('Version', config.version)
    letter_color = os.environ.get('Color of the letters', config.letter_color)

    # Loading schedule
    schedule = os.environ.get('Schedule', config.schedule)
    schedule_date_format = os.environ.get('Schedule date format', config.schedule_date_format)
    print("Config file loaded...")

# Checking for schedule file

schedule_file = current_path + "/modules/schedule.py"
is_schedule_file = os.path.isfile(schedule_file)

print("Loading schedule module...")
if not is_schedule_file:
    print("Heinrichy wasn't able to detect schedule.py file in /modules which is required to run, please redownload Heinrichy with this file...")
    print("Exiting...")
    sys.exit()


# Loading additional modules, setting important variables and changing the size of terminal
print("Loading main modules...")
import json
import time
import random
import httplib2
from timeit import timeit
from time import sleep
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

try:
    # on Python2, this should work
    input = raw_input
    range = xrange
    from urllib import urlopen, urlencode
except NameError:
    # on Python3 these should work
    from urllib.request import urlopen
    from urllib.parse import urlencode

print("Setting variables...")
clear = lambda: os.system('clear')
sys.dont_write_bytecode = True
schedule_list_for_today = [];

print("Changing the size of the terminal...")
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=115))

print("Setting up the format of the dates...")
if schedule_date_format == "DD/MM/YYYY":
    schedule_date_format_type = 1
    todays_date = str(time.strftime("%d/%m/%Y"))
elif schedule_date_format == "MM/DD/YYYY":
    schedule_date_format_type = 2
    todays_date = str(time.strftime("%m/%d/%Y"))
elif schedule_date_format == "YYYY/MM/DD":
    schedule_date_format_type = 3
    todays_date = str(time.strftime("%Y/%m/%d"))
elif schedule_date_format == "YYYY/DD/MM":
    schedule_date_format_type = 4
    todays_date = str(time.strftime("%Y/%d/%m"))
else:
    print("Invalid date format, please change 'schedule_date_format' in config file...")
    print("Exiting...")
    sys.exit()


# Classes & functions

print("Loading classes and functions...")

class bcolors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREY = '\033[90m'

# Adds list with the colours so the colors can be displayed in the terminal

def list_schedule():
    total_task_number_today = 0
    for task in schedule:
        if schedule[task] == todays_date:
            if not task in schedule_list_for_today:
                schedule_list_for_today.insert(total_task_number_today, task)
            total_task_number_today = total_task_number_today + 1
    if total_task_number_today == 0:
        print("Your today's schedule;")
        print("- Your schedule is empty for today!")
    elif not total_task_number_today == 0:
        print("Your today's schedule;")
        for task in schedule_list_for_today:
            print("- " + task)
    print("\n")

# Function lists the schedule. First sets the variable total_task_number_today
# to 0 then for each item that is in the schedule from config file, checks
# if the date that comes with the task is todays date. If so, adds the task
# to the list (schedule_list_for_today) and adds one to total_task_number_today.
# Then when this is finished for every task, it checks if todays number
# of tasks is equal to zero, if so, it prints that the schedule is empty.
# If it doesn't equal to zero (it has some tasks today), for each task in the
# list (schedule_list_for_today) prints out this task. Wow, this could be
# actually useful for the future.

def print_main_screen():

    # Main 'Heinrichy' text
    print("___________________________________________________________________________________________________________________")
    print("|                                                                                                                 |")
    print("|                                                                                                                 |")
    print("|        " + color_changer + "ooooo   ooooo            o8o                        o8o            oooo" + bcolors.WHITE + "                                  |")
    print("|        " + color_changer + "`888'   `888'             ''                        `'            `888" + bcolors.WHITE + "                                   |")
    print("|         " + color_changer + "888     888   .ooooo.  oooo  ooo. .oo.   oooo d8b oooo   .ooooo.   888 .oo.   oooo    ooo" + bcolors.WHITE + "               |")
    print("|         " + color_changer + "888ooooo888  d88' `88b `888  `888P'Y88b  `888""8P  `888   d88' `'Y8  888P'Y88b   `88.   .8'" + bcolors.WHITE + "               |")
    print("|         " + color_changer + "888     888  888ooo888  888   888   888   888      888  888        888   888    `88..8'" + bcolors.WHITE + "                 |")
    print("|         " + color_changer + "888     888  888    .o  888   888   888   888      888  888   .o8  888   888     `888'" + bcolors.WHITE + "                  |")
    print("|        " + color_changer + "o888o   o888o `Y8bod8P' o888o o888o o888o d888b    o888o `Y8bod8P' o888o o888o     .8'" + bcolors.WHITE + "                   |")
    print("|                                                                                       " + color_changer + ".o..P'" + bcolors.WHITE + "                    |")
    if show_version == True:
        print("|                                                                                       " + color_changer + "`Y8P'" + bcolors.WHITE + "        " + version + "  |")
    elif show_version == False:
        print("|                                                                                       " + color_changer + "`Y8P'" + bcolors.WHITE + "                     |")
    print("|_________________________________________________________________________________________________________________|")

def print_schedule():
    # Printing schedule
    print("\n")
    if show_schedule == True:
        if not schedule:
            print("Your today's schedule;")
            print("- Your schedule is empty for today!")
            print("\n")
        else:
            list_schedule()
    elif show_schedule == False:
        print("\n")

def check_birthday():
    # Checking if today is users birthday
    if schedule_date_format_type == 1:
        if date_of_birth[:5] == str(time.strftime("%d/%m")):
            print(bcolors.YELLOW + "Happy Birthday, " + name + "!\n" + bcolors.WHITE)
    elif schedule_date_format_type == 2:
        if date_of_birth[:5] == str(time.strftime("%m/%d")):
            print(bcolors.YELLOW + "Happy Birthday, " + name + "!\n" + bcolors.WHITE)
    elif schedule_date_format_type == 3:
        if date_of_birth[5:10] == str(time.strftime("%m/%d")):
            print(bcolors.YELLOW + "Happy Birthday, " + name + "!\n" + bcolors.WHITE)
    elif schedule_date_format_type == 4:
        if date_of_birth[5:10] == str(time.strftime("%d/%m")):
            print(bcolors.YELLOW + "Happy Birthday, " + name + "!\n" + bcolors.WHITE)

def response(query):                                                            # Function gets the xml file create from engine and gets plain text from it.
    query = query.lower()
    query_original = query
    query = urlencode({'input':query})
    app_id = "Q6254U-URKKHH9JLL"
    wolfram_api = "http://api.wolframalpha.com/v2/query?appid="+app_id+"&format=plaintext&podtitle=Result&"+query
    resp, content = httplib2.Http().request(wolfram_api)
    root = ET.fromstring(content)
    error = root.get('error')
    success = root.get('success')
    numpods = root.get('numpods')
    answer= ''
    if success and int(numpods) > 0 :
        for plaintext in root.iter('plaintext'):
            if isinstance(plaintext.text, str) :
                answer = answer + plaintext.text
        return answer
    elif error:
        me_no_english1 = "Sorry, I didn't understood that."
        me_no_english2 = "I didn't get that."
        me_no_english3 = "Ohh, english language is tough, I can't understand what you said."
        me_no_english4 = "It seems like I can't answer this question."
        me_no_english = [me_no_english1, me_no_english2, me_no_english3, me_no_english4]

        if additional_search == True:
            query_original = query_original.replace(" ", "_")
            r = urlopen("https://www.evi.com/q/" + query_original).read()
            whole_content = BeautifulSoup(r, "lxml")
            answer = str(whole_content.find(class_="tk_common"))
            length = int(len(str(answer)))
            first_length = length - 9
            answer = answer[25:first_length]
            if answer.find('None'):
                return random.choice(me_no_english)
            else:
                return answer

        elif additional_search == False:
            return random.choice(me_no_english)

        elif additional_search == "Ask":
            print("It seems like I can't answer this question.")
            print("Do you want me to send query to Evi? [Y/N]")
            user_input = input("[Y/N] >")
            if user_input == "Y" or user_input == "y":
                query_original = query_original.replace(" ", "_")
                r = urlopen("https://www.evi.com/q/" + query_original).read()
                whole_content = BeautifulSoup(r, "lxml")
                answer = str(whole_content.find(class_="tk_common"))
                length = int(len(str(answer)))
                first_length = length - 9
                answer = answer[25:first_length]
                if answer.find('None'):
                    return random.choice(me_no_english)
                else:
                    return answer
            elif user_input == "N" or user_input == "n":
                return "\n Press enter to reset."
            else:
                return "Wrong command."


# -----------------------------------  Main  -----------------------------------

sleep(1)
clear()

# Checking the colour of the letters
if letter_color == "BLUE":
    color_changer = bcolors.BLUE
elif letter_color == "GREY":
    color_changer = bcolors.GREY
elif letter_color == "PINK":
    color_changer = bcolors.PINK
elif letter_color == "YELLOW":
    color_changer = bcolors.YELLOW
elif letter_color == "GREEN":
    color_changer = bcolors.GREEN
elif letter_color == "RED":
    color_changer = bcolors.RED
elif letter_color == "WHITE":
    color_changer = bcolors.WHITE

# Showing main text
if clear_commands == True:
    while True:

        # Printing main 'Heinrichy' text
        clear()
        print_main_screen()

        # Printing out schedule
        print_schedule()

        # Printing out 'happy birthday'
        check_birthday()

        # Asking for user input
        print("How can I help you today, " + name + "?")
        user_input = input(">")
        if user_input == "schedule":
            exec(compile(open(schedule_file).read(), schedule_file, 'exec'))
        else:
            print(response(user_input))
            pause = input()

elif clear_commands == False:

    # Printing main 'Heinrichy' text
    print_main_screen()

    # Printing out schedule
    print_schedule()

    # Printing out 'happy birthday'
    check_birthday()

    # Asking for user input
    while True:
        print("How can I help you today, " + name + "?")
        user_input = input(">")
        if user_input == "schedule":
            exec(compile(open(schedule_file).read(), schedule_file, 'exec'))
        else:
            print(response(user_input))
            pause = input()

else:
    print("Variable clear_commands has invalid value, please change to True or False.")
