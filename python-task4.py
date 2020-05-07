import json
import datetime
import random
import os

while True:
    print("1. Staff Login")
    print("2. Close App")
    option = input("Select an option: ")

    if option == "1" or option == "2":
        break
    else:
        continue

if option == "1":
    session = False
    while session == False:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        f = open("staff.txt", "r")
        users = json.loads(f.read())
        f.close()

        for user in users:
            if user['username'] == username and user['password'] == password:
                user["login_time"] = datetime.datetime.now()
                f = open("session.txt", "w")
                f.write(str(user))
                f.close()
                
                while True:
                    print("1. Create new bank account")
                    print("2. Check Account Details")
                    print("3. Logout")
                    sessionOption = input("Select an option: ")

                    if sessionOption == "1":
                        account_name = input("Enter account name: ")
                        opening_balance = input("Enter your opening balance: ")
                        account_type = input("Enter account type: ")
                        account_email = input("Enter account email ")
                        account_number = str(random.randint(1000000000, 9999999999))

                        account_details = {
                            "account_name": account_name,
                            "opening_balance": opening_balance,
                            "account_type": account_type,
                            "account_email": account_email,
                            "account_number": account_number
                        }

                        f = open("customer.txt", "w")
                        json.dump(account_details, f)
                        f.close()
                        print(f"Account creation successfull. Here is your new account number: {account_number}")
                        continue
                    elif sessionOption == "2":
                        account_number = input("Enter your account number: ")

                        f = open("customer.txt", "r")
                        accounts = json.loads(f.read())
                        f.close()

                        for account in accounts:
                            print(account)
                            exit
                            if accounts['account_number'] == account_number:
                                print(f"Account name: {account['account_name']} \n Opening Balance: {account['opening_balance']} \n Account type: {account['account_type']} \n Account email: {account['account_email']}")
                                break
                            else:
                                print(f"Account number {account_number} not found")
                                break
                    elif sessionOption == "3":
                        os.remove("session.txt")
                        break
                    else:
                        continue
                break
            else:
                print("That did not work. Try again.")
                break
else:
    print("App closed")