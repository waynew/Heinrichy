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



# Script schedule.py allows you to modify your schedule which then will
# be displayed in Heinrichy
from __future__ import print_function


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
schedule_date_format = os.environ.get('Schedule date format', config.schedule_date_format)

#Setting variables
exit_code = 0

if schedule_date_format == "DD/MM/YYYY":
    schedule_date_format_type = 1
elif schedule_date_format == "MM/DD/YYYY":
    schedule_date_format_type = 2
elif schedule_date_format == "YYYY/MM/DD":
    schedule_date_format_type = 3
elif schedule_date_format == "YYYY/DD/MM":
    schedule_date_format_type = 4
else:
    print("Invalid date format, please change 'schedule_date_format' in config file...")
    print("Exiting...")
    sys.exit()


# -----------------------------------  Main  -----------------------------------

print("\n")
print("Welcome to schedule module of Heinrichy. Here you can modify your schedule.")
print("Your full schedule including dates;")
if not schedule:
    print("Your schedule is empty.")
else:
    for task in schedule:
        print("- " + task + " (" + schedule[task] + ")")


while exit_code == 0:
    # User input
    user_input = input("schedule>")
    user_input = user_input.lower()

    # Commands

    # Help - displays help
    if any(command in user_input for command in ("help", "--help", "help me", "i need help")):
        print("\n")
        print("Welcome to schedule module where you can modify your daily schedule. You can add/remove/change events how ever")
        print("you want. Just use one of the commands below;")
        print("\n")
        print("add [name of the task] - adds new task to the schedule,")
        print("list - lists your newest schedule")
        print("remove [name of the task] - removes the task from the schedule,")
        print("rename [name of the task] - changes the name of already existing task,")
        print("move [name of the task] - moves one task to another date")
        print("exit - exits schedule module")

    # Add - add the task to schedue
    elif user_input[:4] == "add ":
        task = user_input.split(' ', 1)[1]
        print(" Adding '" + task + "' to the schedule list, please type in a date for this task in the format " + schedule_date_format)
        year = int(time.strftime("%Y"))
        month = int(time.strftime("%m"))
        cal = calendar.month(year, month)

        if schedule_date_format_type == 1:
            date = str(time.strftime("%d/%m/%Y"))
        elif schedule_date_format_type == 2:
            date = str(time.strftime("%m/%d/%Y"))
        elif schedule_date_format_type == 3:
            date = str(time.strftime("%Y/%m/%d"))
        elif schedule_date_format_type == 4:
            date = str(time.strftime("%Y/%m/%d"))

        print("\n" + cal + "Todays date is: " + date)
        date_of_task = input("schedule, date>")
        if date_of_task == "":
            print("You haven't chosen any date, selecting todays date...")
            schedule[task.lower()] = date
            print("Your task has been added.")
        elif date_of_task[:2].isdigit() == False:
            print("This is not a date!")
        else:
            schedule[task.lower()] = date_of_task
            print("Your task has been added.")

    # List - lists the tasks
    elif user_input == "list" or user_input == "ls":
        for task in schedule:
            print("- " + task + " (" + schedule[task] + ")")

    # Remove - deletes the task from the schedue
    elif user_input[:7] == "remove " or user_input[:7] == "delete ":
        task = user_input.split(' ', 1)[1]
        if task in list(schedule.keys()):
            del schedule[task]
            print("Your task has been deleted.")
        elif task not in list(schedule.keys()):
            print("That task is not on the list!")

    # Rename - rename the task
    elif user_input[:7] == "rename " or user_input[:12] == "change name ":
        task = user_input.split(' ', 1)[1]
        if task in list(schedule.keys()):
            print("Type in new name for this task;")
            new_task_name = input("schedule, new_task_name>")
            schedule[new_task_name] = schedule[task]
            del schedule[task]
            print("Your task's name has been changed.")
        elif task not in list(schedule.keys()):
            print("That task is not on the list!")

    # Move - moves the task to different date
    elif user_input[:5] == "move ":
        task = user_input.split(' ', 1)[1]
        if task in list(schedule.keys()):
            print("Type in new date for this task;")
            year = int(time.strftime("%Y"))
            month = int(time.strftime("%m"))
            cal = calendar.month(year, month)
            print("\n" + cal + "Todays date is: " + str(time.strftime("%d/%m/%Y")))
            new_task_date = input("schedule, new_task_date dd/mm/yyyy>")
            if new_task_date[:2].isdigit() == True and new_task_date[4:5].isdigit() == True and new_task_date[7:10].isdigit() == True:
                schedule[task] = new_task_date
                print("Your task has been moved.")
            else:
                print("This date is invalid.")
        elif task not in list(schedule.keys()):
            print("That task is not on the list!")

    # Exit - exits the module to go back to Heinrichy
    elif user_input == "exit":
        print("You are about to exit 'schedule module'. Are you sure you want to continue? [Y/N]")
        user_input = input("schedule, [Y/N]>")
        if user_input == "Y" or user_input == "y":
            with open(config_file + "/config.py", "r+") as config_file_open:
                config_full = config_file_open.readlines()
                config_full[15] = "schedule = " + str(schedule)
            with open(config_file + "/config.py", "w") as config_file_open:
                config_file_open.writelines(config_full)
            exit_code = 1
        elif user_input == "N" or user_input == "n":
            print("Alright then, you can carry on to modify your schedule.")
        else:
            print("Wrong command...")

    # Invalid command
    else:
        print("Invalid command.")
