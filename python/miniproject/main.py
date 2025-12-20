print("How may I help you")
user={}
#login route
def login():
    username=input("enter username:- ")
    password=input("enter password:- ")
    useracount=user.get(username)
    if useracount is not None and useracount == password:
        print(f"Welcome, {username}!")
    else:
        print(f"Username '{username}' and/or password are wrong")

#register route
def register():
    username=input("enter username:- ")
    password=input("enter password:- ")
    useracount=user.get(username)
    if(useracount):
        print("Account allready exist plese Login")
    else:
        user.update({username:password})
        print("Thank You")

#acount delete route
def delete():
    username=input("enter username:- ")
    password=input("enter password:- ")
    useracount=user.get(username)
    if useracount is not None and useracount == password:
        user.pop(username)
        print("Account deleted successfully.")
    else:
        print("Username and/or password are wrong. Account not deleted.")
            
def showuser():
    print(user)
    
userinput=-1

while(userinput!=0):
    print("0: Exit")
    print("1: Register")
    print("2: Login")
    print("3: Delete Acount")
    print("4: Show User")
    userinput=int(input("Enter your choice:- "))
    if(userinput==1):
        register()
    elif(userinput==2):
        login()
    elif(userinput==3):
        delete()
    elif(userinput==4):
        showuser()

