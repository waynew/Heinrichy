# -*- coding: UTF-8 -*-

#               _   _      _            _      _
#              | | | | ___(_)_ __  _ __(_) ___| |__  _   _
#              | |_| |/ _ | | '_ \| '__| |/ __| '_ \| | | |
#              |  _  |  __| | | | | |  | | (__| | | | |_| |
#              |_| |_|\___|_|_| |_|_|  |_|\___|_| |_|\__, |
#                                                    |___/            __Alpha_20
#
#   Heinrichy - personal assistant made especially for GNU/Linux because we
#                   deserve our own version of siri too!
#								      By michpcx



# Script schedule.py allows you to modify your schedule which then will
# be displayed in Heinrichy


# Importing main modules
import os
import sys
import time
import calendar
from sys import platform as _platform
from unipath import Path

# Setting path to import config
current_path = os.path.dirname(os.path.abspath(__file__))
current_path = Path(current_path)
config_file = current_path
sys.path.append(config_file)
import config

# Importing schedule
schedule = os.environ.get('Schedule', config.schedule)

#Setting variable
exit_code = 0


# -----------------------------------  Main  -----------------------------------

print "\n"
print "Welcome to schedule module of Heinrichy. Here you can modify your schedule."
print "Your full schedule including dates;"
if not schedule:
    print "Your schedule is empty."
else:
    for task in schedule:
        print "- " + task + " (" + schedule[task] + ")"


while exit_code == 0:
    # User input
    user_input = raw_input("schedule>")
    user_input = user_input.lower()

    # Commands

    # Help - displays help
    if any(command in user_input for command in ("help", "--help", "help me", "i need help")):
        print "\n"
        print "Welcome to schedule module where you can modify your daily schedule. You can add/remove/change events how ever"
        print "you want. Just use one of the commands below;"
        print "\n"
        print "add [name of the task] - adds new task to the schedule,"
        print "list - lists your newest schedule"
        print "remove [name of the task] - removes the task from the schedule,"
        print "rename [name of the task] - changes the name of already existing task,"
        print "move [name of the task] - moves one task to another date"
        print "save/update - saves your schedule to the file"

    # Add - add the task to schedue
    elif user_input[:4] == "add ":
        task = user_input.split(' ', 1)[1]
        print " Adding '" + task + "' to the schedule list, please type in a date for this task in format dd/mm/yyyy;"
        year = int(time.strftime("%Y"))
        month = int(time.strftime("%m"))
        cal = calendar.month(year, month)
        print "\n" + cal + "Todays date is: " + str(time.strftime("%d/%m/%Y"))
        date_of_task = raw_input("schedule, date>")
        if date_of_task == "":
            print "You haven't chosen any date, selecting todays date..."
            date_of_task = str(time.strftime("%d/%m/%Y"))
            schedule[task.lower()] = date_of_task
            print "Your task has been added."
        elif date_of_task[:2].isdigit() == False:  # Fix it
            print "This is not a date!"
        else:
            schedule[task.lower()] = date_of_task
            print "Your task has been added."

    # List - lists the tasks
    elif user_input == "list" or user_input == "ls":
        for task in schedule:
            print "- " + task + " (" + schedule[task] + ")"

    # Remove - deletes the task from the schedue
    elif user_input[:7] == "remove " or user_input[:7] == "delete ":
        task = user_input.split(' ', 1)[1]
        if task in schedule.keys():
            del schedule[task]
            print "Your task has been deleted."
        elif task not in schedule.keys():
            print "That task is not on the list!"

    # Rename - rename the task
    elif user_input[:7] == "rename " or user_input[:12] == "change name ":
        task = user_input.split(' ', 1)[1]
        if task in schedule.keys():
            print "Type in new name for this task;"
            new_task_name = raw_input("schedule, new_task_name>")
            schedule[new_task_name] = schedule[task]
            del schedule[task]
            print "Your task's name has been changed."
        elif task not in schedule.keys():
            print "That task is not on the list!"

    # Move - moves the task to different date
    elif user_input[:5] == "move ":
        task = user_input.split(' ', 1)[1]
        if task in schedule.keys():
            print "Type in new date for this task;"
            year = int(time.strftime("%Y"))
            month = int(time.strftime("%m"))
            cal = calendar.month(year, month)
            print "\n" + cal + "Todays date is: " + str(time.strftime("%d/%m/%Y"))
            new_task_date = raw_input("schedule, new_task_date dd/mm/yyyy>")
            if new_task_date[:2].isdigit() == True and new_task_date[4:5].isdigit() == True and new_task_date[7:10].isdigit() == True:
                schedule[task] = new_task_date
                print "Your task has been moved."
            else:
                print "This date is invalid."
        elif task not in schedule.keys():
            print "That task is not on the list!"

    # Save - saves the schedule to config file
    elif user_input == "save" or user_input == "update":
        with open(config_file + "/config.py", "r+") as config_file_open:
            config_full = config_file_open.readlines()
            config_full[13] = "schedule = " + str(schedule)
        with open(config_file + "/config.py", "w") as config_file_open:
            config_file_open.writelines(config_full)
        print "Your schedule has been updated, you can go back to heinrichy using 'exit' command."

    # Exit - exits the module to go back to Heinrichy
    elif user_input == "exit":
        print "You are about to exit 'schedule module'. Are you sure you want to continue? [Y/N]"
        user_input = raw_input("schedule, [Y/N]>")
        if user_input == "Y" or user_input == "y":
            exit_code = 1
        elif user_input == "N" or user_input == "n":
            print "Alright then, you can carry on to modify your schedule."
        else:
            print "Wrong command..."

    # Invalid command
    else:
        print "Invalid command."
