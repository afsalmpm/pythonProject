def positive_float_entry(float_input):  # Positive Float entry function
    while True:
        try:
            user_float_input = float(input(f'Enter {float_input}: '))
            if user_float_input > 0:
                break  # Loop exit method
            else:
                print(f"invalid {float_input} entry")
        except ValueError:
            print(f"invalid {float_input} entry")
    return user_float_input


class Bank:
    def __init__(self):
        self.client_details_list = []
        self.loggedin = False
        self.cash = 100
        self.TransferCash = False

    def register(self, name, ph, password):
        cash = self.cash
        print(name, ph, password)
        conditions = True
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("Invalid Phone number ! please enter 10 digit number")
            conditions = False

        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5 and less than 18 character")
            conditions = False

        if conditions:  # If condition == True
            print("Account created successfully")
            self.client_details_list = [name, ph, password, cash]
            with open(f"{name}.txt", "w") as f:
                for details in self.client_details_list:
                    f.write(str(details) + "\n")

    def login(self, name, ph, password):
        try:
            with open(f"{name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")
                if str(ph) in str(self.client_details_list):
                    if str(password) in str(self.client_details_list):
                        self.loggedin = True

                if self.loggedin == True:
                    print(f"{name} logged in")
                    self.cash = int(self.client_details_list[3])
                    self.name = name

                else:
                    print("Wrong details")
        except FileNotFoundError:
            print("Wrong details")

    def add_cash(self, amount):
        if amount > 0:
            self.cash += amount
            with open(f"{name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[3]), str(self.cash)))

            print("Amount added successfully")

        else:
            print("Enter correct value of amount")

    def Tranfer_cash(self, amount, name, ph):
        with open(f"{name}.txt", "r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in self.client_details_list:
                self.TransferCash = True

        if self.TransferCash == True:
            total_cash = int(self.client_details_list[3]) + amount
            left_cash = self.cash - amount
            with open(f"{name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[3]), str(total_cash)))

            with open(f"{self.name}.txt", "r") as f:
                details_2 = f.read()
                self.client_details_list = details_2.split("\n")

            with open(f"{self.name}.txt", "w") as f:
                f.write(details_2.replace(str(self.client_details_list[3]), str(left_cash)))

            print("Amount Transfered Successfully to", name, "-", ph)
            print("Balacne left =", left_cash)
            self.cash = left_cash

    def password_change(self, password):
        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5 and less than 18 character")
        else:
            with open(f"{self.name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[2]), str(password)))
            print("new Password set up successfully")

    def ph_change(self, ph):
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("Invalid Phone number ! please enter 10 digit number")
        else:
            with open(f"{self.name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[1]), str(ph)))
            print("new Phone number set up successfully")


if __name__ == "__main__":
    Bank_object = Bank()
    print("Welcome to my Bank")
    print("1.Login")
    print("2.Creata a new Account")
    user = ValueError
    while user == ValueError:
        try:
            user = int(input("Make decision: "))
            if user > 2:
                print("Invalid decision")
                user = ValueError
        except ValueError:
            user = ValueError
            print("Invalid decision")


    if user == 1:
        print("Logging in")
        name = input("Enter Name: ")
        ph = str(int(positive_float_entry("Phone Number")))
        password = input("Enter password: ")
        Bank_object.login(name, ph, password)
        while True:
            if Bank_object.loggedin:
                print("1.Add amount")
                print("2.Check Balance")
                print("3.Transfer amount")
                print("4.Edit profile")
                print("5.Logout")
                logged_in_user = int(input())
                if logged_in_user == 1:
                    print("Balance =", Bank_object.cash)
                    amount = int(positive_float_entry("the amount"))
                    Bank_object.add_cash(amount)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif logged_in_user == 2:
                    print("Balance =", Bank_object.cash)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif logged_in_user == 3:
                    print("Balance =", Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    if 0 <= amount <= Bank_object.cash:
                        name = input("Enter person name: ")
                        ph = input("Enter person phone number: ")
                        Bank_object.Tranfer_cash(amount, name, ph)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif amount < 0:
                        print("Enter please correct value of amount")

                    elif amount > Bank_object.cash:
                        print("Not enough balance")

                elif logged_in_user == 4:
                    print("1.Password change")
                    print("2.Phone Number change")
                    edit_profile = int(input())
                    if edit_profile == 1:
                        new_passwrod = input("Enter new Password: ")
                        Bank_object.password_change(new_passwrod)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif edit_profile == 2:
                        new_ph = int(input("Enter new Phone Number: "))
                        Bank_object.ph_change(new_ph)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break

                elif logged_in_user == 5:
                    break

    if user == 2:
        print("Creating a new  Account")
        name = input("Enter Name: ")
        ph = str(int(positive_float_entry("Phone Number")))
        password = input("Enter password: ")
        Bank_object.register(name, ph, password)
# updated
# code.txt
# Displaying
# updated
# code.txt.
