import time
import os
import subprocess
from sys import exit

os.system("")


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


fileName = input("Enter file name (with the file extension) : ")

lines = open(fileName, 'r').readlines()

print("Found {} users in the file".format(len(lines)))

valid = input("Do you want to continue? (y/n) : ")
if valid != "y" and valid != "Y":
    print("Exiting...")
    exit()


def action():
    print("1. Create users")
    print("2. Delete users")
    print("3. List users in file")
    print("4. Exit")
    act = int(input("What do you want to do? : "))

    if act == 1:
        create_users()
    elif act == 2:
        delete_users()
    elif act == 3:
        list_users()
    else:
        exit()


def create_users():
    start = time.time()
    print("Creating users...")
    for line in lines:
        user = line.strip().split(":")
        print("Creating user : {}".format(user[0]))
        subprocess.call(["useradd", "-m", "-p", "$(openssl passwd -1 " + 
                         user[1] + ")", user[0]])
    print("Done creating users. Took {} ms\n".format(time.time() - start))
    action()


def delete_users():
    start = time.time()
    print("Deleting users...")
    for line in lines:
        user = line.strip().split(":")
        print("Removing user : {}".format(user))
        subprocess.call(["userdel", "-r", "-f", user[0]])
    print("Done deleting users. Took {} ms\n".format(time.time() - start))
    action()
    

def list_users():
    start = time.time()
    print("Listing users...")
    for line in lines:
        user = line.strip().split(":")
        print("User :",user[0],"Password :", user[1])
    print("Done listing users. Took {} ms\n".format(time.time() - start))
    action()


action()