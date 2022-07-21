# imports
import random as rnd
import time
import os
import socket
ver = 1.1

# Detect if 192.168.0.116 is online.
# If not, Proceed as normal.
# If yes, detect if it has a updated version.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if server.connect(('192.168.0.116', 8080)) == ConnectionRefusedError:
    print('Server is offline.')
    print('Proceeding as normal.')
    server.close()
else:
    print('Server is online.')
    print('Checking for updates.')
    server.send(b'Do you have an updated version?')
    # If server has a newer version, update.
    if int(server.recv(1024).decode) <= ver:
        print('Server has a newer version.')
        print('Updating.')
        server.send(b'Lemme update.')
        # Get the download link.
        # If the link is null, don't update.
        if server.recv(1024) == b'0':
            print("Server doesn't have a download link.")
        else:
            link = server.recv(1024).decode()
            print('Downloading from: ' + link)
            os.system('powershell wget ' + link)
            print('Downloaded.')
            print('Updating.')
            print('Updated.')
            print('Exiting.')
            exit()
        print('Update complete.')
        server.close()
        exit()
    else:
        print('Server has the latest version.')
        server.close()
        print('Proceeding as normal.')

# Main vars
level = 1
xp = 0
coins = 0
coinm = 1

# Number stuff
minnum = 0
maxnum = 5
rndnum1 = 0
rndnum2 = 0

# Main game
while(1):
    rndnum1 = rnd.randint(minnum, maxnum)
    rndnum2 = rnd.randint(minnum, maxnum)
    print("What is ", end="")
    print(rndnum1, end="")
    print(" + ", end="")
    print(rndnum2, end="")
    print("?", end="\n")
    ans = int(input())
    if ans == rndnum1 + rndnum2:
        print("Correct!")
        coins = coins + (1 * coinm)
        xp = xp + 1
        if xp == level * 10:
            level = level + 1
            xp = 0
            coins = coins + 30
            print("You leveled up!")
            print("Your level is now ", end=str(level))
            print("!")
        print("You now have ", end=str(coins))
        print(" coins!")
        print("Your XP is now ", end=str(xp))
        print(" out of ", end=str(level * 10))
        print("!")
        # wait a bit
        print("\n")
        time.sleep(1)
        # clear screen (cls)
        os.system('cls')
    else:
        print("Wrong!")
        print("The answer was ", end="")
        print(rndnum1 + rndnum2, end="\n")
        # wait a bit
        print("\n")
        time.sleep(1)
        # clear screen (cls)
        os.system('cls')
    if coins > 2:
        print("Would you like to go to the shop?")
        print("You have ", end=str(coins))
        print(" coins.")
        print("Y/N")
        temp = input()
        if temp == "Y" or temp == "y":
            # wait a bit
            print("\n")
            time.sleep(1)
            # clear screen (cls)
            os.system('cls')
            print("1. Harder Questions")
            print("Costs 3 coins")
            print("2. Coin multiplier")
            print("Costs 5 coins")
            temp = int(input())
            if temp == 1:
                if coins > 2:
                    print("Bought Harder Questions!")
                    maxnum = maxnum + 1
                    coins = coins - 3
            elif temp == 2:
                if coins > 4:
                    print("Bought Coin Multiplier!")
                    coinm = coinm + 1
                    coins = coins - 5
            else:
                print("Invalid input!")
            print("You now have ", end=str(coins))
            print(" coins!")
        # wait a bit
        print("\n")
        time.sleep(1)
        # clear screen (cls)
        os.system('cls')


