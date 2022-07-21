import time
import os

def Login_status():
    username=input('Enter Your Username: ')
    password=input('\nEnter Your Password: ')

    try:
        with open(username+".txt", "r") as file:
            un=file.readline().rstrip()
            pw=file.readline().rstrip()
        file.close()
        if(username==un and password==pw):
            return True
        else:
            return False
    except IOError:
        print("No Such Login credentital file exits.")
        return False    
    
def _main_():
    choice=input("1.Registration\n2.Login\nChoose a method: ")
    if choice ==str(1):
        print("\nUser Should use unused Username.")
        UserName=input('\nEnter a Username:')
        Password=input('\nEnter the password:')


        f=open(UserName+".txt","w")
        f.write(UserName+"\n")
        f.write(Password)
        f.close()
        _main_()

    elif choice ==str(2):
        if(Login_status() == True):
            print("Successful Login!\n")
            os.system("PAUSE")
        else:
            print("Invalid Login Creditinals!\n")
            os.system("PAUSE")

    else:
        print("Enter a valid input.\n")
        time.sleep(1)
        _main_()
_main_()

        