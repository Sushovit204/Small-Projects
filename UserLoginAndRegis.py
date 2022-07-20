import time

def Login_status():
    username=input('Enter Your UserName: ')
    password=input('\nEnter Your passWord: ')

    with open(username+".txt", "r") as file:
        uw=file.readline()
        pw=file.readline()
    
    if(username==uw and password==pw):
        return True
    else:
        return False
    

choice=int(input("1.Registration\n2.Login\nChoose a method: "))
if choice ==1:
    print("\nUser Should use unused Username.")
    UserName=input('\nEnter a Username:')
    Password=input('\nEnter the password:')
    

    f=open(UserName+".txt","w")
    f.write(UserName+"\n")
    f.write(Password)
    f.close()

elif choice ==2:
    if(Login_status() == True):
        print("Invalid Login!\n")
        time.sleep(3)
    elif(Login_status() == False):
        print("Successful Login!\n")
        time.sleep(3)



        