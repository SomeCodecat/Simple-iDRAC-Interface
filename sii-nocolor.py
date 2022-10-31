import os
import getpass
import msvcrt as m


def welcome():
    # Welcome Message
    print("Welcome to the Simple iDRAC Interface\n")
    print("Copyright (c) 2022 SomeCatThatCodes")


def login():
    # Let the user enter their password (noecho)
    pw = getpass.getpass("Enter IPMI (iDRAC) Password: ")

    return pw


def constructFinalCommand(pw, command):
    # Change the user to login with
    USER = "root"

    # Change change the adress of the host machine
    HOST = "O.O.O.O"

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
    # Print out the choosable commands
    print("""Choose a command:
    [1] System status
    [2] Turn system on
    [3] Turn system off
    [4] Enter a custom command

    [ESC] Exit program
    """)

    # Wait for a key to be pressed (escape keys are Ctrl+C and ESC)
    match m.getch():
        case b"1":
            chosenCommand = "chassis status"
        case b"2":
            chosenCommand = "chassis power on"
        case b"3":
            chosenCommand = "chassis power off"
        case b"4":
            chosenCommand = input("Enter your command: ")
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
