# Hailey Stouder
# Computer Networks - Project 1

import socket

# HOST = "34.173.12.133"
# PORT = 3389
# LOGFILE = "logFile.txt"
# 34.173.12.133,3389,logFile.txt

# read and parse command line arguments
userInput = input("Enter host, port, and file name in comma separated format: ").split(',')
HOST = userInput[0]
PORT = int(userInput[1])
LOGFILE = open(userInput[2], "a")

# create a socket stream
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # connect to server
    try:
        s.connect((HOST, PORT))
        LOGFILE.write("\nSuccessfully connected. IP: " + HOST + "   Port: " + str(PORT))
    except Exception as e:
        print("\nError connecting to server: " + str(e))
        LOGFILE.write("\nError connecting to server: " + str(e))

    # send a string to server
    try:
        message = input("Enter a message to send to server: ")
        s.send(message.encode('utf-8'))

    except Exception as e:
        print("\nError sending message to server: " + str(e))
        LOGFILE.write("\nError sending message to server: " + str(e))

    # receive, decode, and log reply from server
    try:
        data = s.recv(1024)
        data = data.decode('utf-8')
        LOGFILE.write("\nMessage received: " + str(data))
        print(f"\nMessage received: {data!r}")
    except Exception as e:
        print("\nError receiving message from server: " + str(e))
        LOGFILE.write("\nError receiving message from server: " + str(e))

    # close connection to server
    try:
        s.close()
        LOGFILE.write("\nClosing connection.\n\n---------------------------\n")
    except Exception as e:
        print("\nError closing connection to server: " + str(e))
        LOGFILE.write("\nError closing connection to server: " + str(e))
