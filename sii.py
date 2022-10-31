# DEPENDENCIES:
# pip install termcolor
# pip install pyfiglet

import os
import getpass
import msvcrt as m
from termcolor import colored
from pyfiglet import Figlet


def welcome():
    # Generate some ASCII art with a welcome message
    figure = Figlet(font='isometric4')
    print(colored(figure.renderText('SiI'), "magenta"))
    print("Welcome to the", colored("Simple iDRAC Interface", "blue"))
    print(colored("Copyright (c) 2022 Maximilian Liebmann", "cyan"))


def login():
    # Let the user enter their password (noecho)
    pw = getpass.getpass("\nEnter IPMI (iDRAC) Password: ")

    return pw


def constructFinalCommand(pw, command):
    # Change the user to login with
    USER = "root"

    # Change change the adress of the host machine
    HOST = "192.168.1.21"

    # Base command to execute commands with IPMI v2 / RMCP+
    comm = """ipmitool -I lanplus -v -H host__ -U user__ -P pw__ comm__"""

    # Replace the placeholders with the right values
    comm = comm.replace(
        "host__", HOST).replace(
        "user__", USER).replace(
        "pw__", pw).replace(
        "comm__", command)

    return comm


def chooseCommand():
    # Change color of the numbers and the escape key
    numberColor = "green"
    exitColor = "red"

    # Print out the choosable commands
    print("Choose a command:\n\n", colored(
        "[1]", numberColor), "STATUS    Show system status\n", colored(
        "[2]", numberColor), "ON        Turn on remote system\n", colored(
        "[3]", numberColor), "OFF       Turn off remote system\n", colored(
        "[4]", numberColor), "COMMAND   Enter a custom command\n\n", colored(
        "[ESC]", exitColor), "EXIT    Exit program")

    # Wait for a key to be pressed (escape keys are Ctrl+C and ESC)
    match m.getch():
        case b"1":
            chosenCommand = "chassis status"
        case b"2":
            chosenCommand = "chassis power on"
        case b"3":
            chosenCommand = "chassis power off"
        case b"4":
            chosenCommand = input(colored("\nEnter your command: ", "yellow"))
        case b"\x1b":
            exit()
        case b"\x03":
            exit()
        case _:
            print("Please enter a valid number.")
            exit()

    return chosenCommand


# Main function calling welcome and executing the command in the console
def main():
    welcome()
    os.system(constructFinalCommand(login(), chooseCommand()))


# Calling the main function
main()
