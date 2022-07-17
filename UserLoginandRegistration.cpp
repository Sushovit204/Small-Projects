//This a C++ project to login a user and check and save its creditials

#include<iostream>
#include<fstream>
#include<string>

using namespace std;

bool IsLoggedIn(){
    string username, password, un, pw;

    cout<<"Enter Username: "; cin>>username;
    cout<<"\nEnter Password: "; cin>>password;

    ifstream read(username + ".txt");
    getline(read,un);
    getline(read,pw);

    if (username == un && password == pw){
        return true;
    }
    else{
        return false;
    }
}

int main(){
    int choice;

    cout<<"1.Registration\n2.Login\nChoose a method"<<endl; cin>>choice;

    if(choice ==1){
        string username, password;
        cout<<"(User should use unused username))"<<endl;
        cout<<"Enter Username: "; cin>>username;
        cout<<"\nEnter Password: "; cin>>password;

        ofstream file;
        file.open(username+".txt");
        file<<username<<endl<<password;
        file.close();

        main();

    }
    else if(choice ==2){
        bool status = IsLoggedIn();

        if(!status){
            cout<<"Invalid Login!"<<endl;
            system("PAUSE");
            return 0;
        }
        else
            cout<<"Successfully Logged In!"<<endl;
            system("PAUSE");
            return 1;
        }
    }


//Saves different text files for each registered user