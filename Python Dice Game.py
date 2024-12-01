#Few imports - used later
import sys
import random
import time
count = 1
#Register/Login Process
RorL = input ("Hi do you want to Login /L or Register /R . ").upper()
if RorL == "R":
    file = open ("username.txt","a")
    username = input ("Register a username. ").lower()
    file.write (username + "\n")
    file.close()
    f = open ("password.txt","a")
    password = input ("Register a password. ")
    f.write (password + "\n")
    f.close()
    RorL = input("Please press /L to Login. ").upper()
if RorL == "L":
    usernameauthentication = input ("To Login give your username. ").lower()
    with open ("username.txt") as un:
        unc = un.read()
    if usernameauthentication not in unc:
        sys.exit("Username not exist. ")
    un.close()
    while count < 6:
        passwordauthentication = input ("To Login give your password. ")
        with open ("password.txt") as pw:
            pwc = pw.read()
        if passwordauthentication not in pwc:
            print("Password not found. Attempts (Max: 5): "+(str)(count)+ "\n")
            count+=1
            if count == 6 :
                sys.exit ("Wrong password has been entered 5 times!")
        else:
            print("The username & password was right. \n")
            count+=7
    pw.close()
if RorL != "R" and RorL != "L":
    sys.exit("Please Register/Login first. ")
#Game Process
rounds=0
user1Score=0
user2Score=0
while rounds < 5:
    rounds+=1
    print ("Round " +(str)(rounds)+ " begins.")
    prompt = input ("User1 press any key to roll a dice. ")
    user1Score += random.randint(1,6)
    time.sleep (0.3)
    print ("Total score for User1: "+(str) (user1Score))
    prompt = input ("User2 press any key to roll a dice. ")
    user2Score += random.randint(1,6)
    time.sleep (0.3)
    print ("Total score for User2: "+(str)(user2Score)+ "\n")
#Comparing Results
if user1Score > user2Score:
    print ("User1 won the game. ")

elif user2Score > user1Score:
    print ("User2 won the game. ")

else:
    print ("Its a draw. ")
