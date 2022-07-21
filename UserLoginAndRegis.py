import time

def Login_status():
    username=input('Enter Your UserName: ')
    password=input('\nEnter Your PassWord: ')

    try:
        with open(username+".txt", "r") as file:
            uw=file.readline()
            pw=file.readline()
        file.close()
        print(uw+" "+pw)
        if(username==uw and password==pw):
            return True
        else:
            return False
    except IOError:
        print("No such creditinal file exits")
        return False

    
    
def _main_():
    choice=int(input("1.Registration\n2.Login\nChoose a method: "))
    if choice ==1:
        print("\nUser Should use unused Username.")
        UserName=input('\nEnter a Username:')
        Password=input('\nEnter the password:')


        f=open(UserName+".txt","w")
        f.write(UserName+"\n")
        f.write(Password)
        f.close()
        _main_()

    elif choice ==2:
        if(Login_status() == False):
            print("Invalid Login!\n")
            time.sleep(1)
        elif(Login_status() == True):
            print("Successful Login!\n")
            time.sleep(1)

_main_()

        