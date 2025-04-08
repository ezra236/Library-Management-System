class User:
    def __init__(self):
        self.user_data = {}


    def sign(self):
        print("WELCOME TO THE LIBRARY SYSTEM!")

        input1 = input("ENTER YOUR NAME: ")
        input2 = input("ENTER YOUR NEW PASSWORD: ")
        input3 = input("ENTER YOUR NATIONAL ID: ")
        input4 = int(input("ENTER YOUR PHONE: "))
        input5 = input("ENTER YOUR EMAIL: ")

        self.user_data [input3] = {
            "name": input1,
            "password": input2,
            "phone": input4,
            "email": input5
        }

        print("SUCCESSFULLY SIGNED IN!")

    def login(self):
        print("WELCOME BACK TO THE LIBRARY!")

        input6 = input("ENTER YOUR NAME: ")
        input7 = input("ENTER YOUR PASSWORD: ")

        for user in self.user_data.values():
            if user["name"] == input6 and user["password"] == input7:
                print("Logged In Successfully!")
                obja = Member(self.user_data)
                obja.borrow()
                return

        print("Login failed: Name or password incorrect.")
            

    def change_password(self):

        input8 = input("ENTER YOUR EMAIL: ")
        input9 = input("ENTER YOUR NAME: ")
        input10 = input("ENTER THE NEW PASSWORD: ")

        for user in self.user_data.values():
            if user["name"] == input9 and user["email"] == input8:
                user["password"] = input10

                print("PASSWORD CHANGED SUCCESSFULLY!")



class Member(User):
    def __init__(self, user_data):
        super().__init__()
        self.user_data = user_data
        self.books = ["48 LAWS OF POWER", "LAWS OF SEDUCTION", "STRATEGIES FOR WAR", "THE PRINCE", "WIN FRIENDS"]
        self.borrowed_items = {}

    def borrow(self):
        print("BOOK SECTIONS!")
        print("\nBOOKS AVAILABLE: ")
        for i in self.books:
            print(i)
        
        input11 = input("ENTER THE BOOK YOU WANT TO BORROW: ")
        input12 = input("ENTER YOUR EMAIL: ")

        for user in self.user_data.values():
            if user["email"] == input12:
                # Initialize list if user hasn't borrowed anything yet
                if input12 not in self.borrowed_items:
                    self.borrowed_items[input12] = []

                self.borrowed_items[input12].append(input11)

                print("BORROW SUCCESSFUL!")
                return

            else:
                print("NO SUCH EMAIL!")


class Librarian(Member):
    def __init__(self):
        super(). __init__()
        self.verifyy = {
            "name":{"password": 123}
        }

    def log(self):
        input13 = input("ENTER NAME: ")
        input14 = input("ENTER PASSWORD: ")

        if input13 in self.verifyy:
            if str(self.verifyy[input13]["password"]) == input14:
                print("Login Successfully!")

            else:
                print("Login not succesfull")

        else:
            print("Name not  found!")


        input15 = input("CHOOSE OPTION: \n 1. Add \n 2. Remove").lower()
        
        if input15 == "1" or input15 == "add":
            input16 = input("ENTER NAME OF THE NEW BOOK: ")
            self.books.append(input16)
        elif input15 == "2" or input15 == "remove":
            input17 = input("ENTER THE NAME OF THE BOOK TO REMOVE: ")
            self.books.remove(input17)
            print(f"{input17} removed successfully.")


obj1 = User()

while True:
    print("\n====== LIBRARY SYSTEM MENU ======")
    option = int(input("CHOOSE AN OPTION:\n1. Create account\n2. Log In\n3. Admin Log In\n4. Change password\n5. Exit\n>> "))

    if option == 1:
        obj1.sign()
    elif option == 2:
        obj1.login()
    elif option == 3:
        objl = Librarian()  
        objl.log()
    elif option == 4:
        obj1.change_password()
    elif option == 5:
        print("Exiting system... Goodbye!")
        break  # <-- use break to stop the while loop
    else:
        print("Invalid option. Please choose a number from 1 to 5.")
