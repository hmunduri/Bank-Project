#!/usr/bin/env python2
import sys
import os 
import datetime
import time
import ast
from random import randint
from logger import Logger 

os.system('cls' if os.name == 'nt' else 'clear')

"""
Banking Project
"""


class Account:
    def __init__(self,logger):
        print("Welcome to BOFA")
        self.accnt_balance = 0
        self.logger = logger
        self.translist = []
        self.customer_data = {}
        self.date = datetime.datetime.strptime(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")
        self.option_six = ["6",  "q", "quit"]
        self.overdraft_yes = ["y",  "yes"]
        self.account_open = False
        self.overdraft_plan = False
        self.file_location = "/Users/hima/Python/Bank-Project/banking/files/customer_data.txt"
        self.trans_file_location = "/Users/hima/Python/Bank-Project/banking/files/transaction_list.txt"
        self.is_valid_user = False

    def show_menu_and_process_request(self):
        try:
            self.logger.log("Showing main menu to user")
            choice = input( '''
            1.Open Account
            2.Login
            Please enter your choice: ''')
            self.logger.log("User choice: {}".format(choice))
            if choice == "1":
                self.open_account()
            elif choice == "2":
                account_number = input("Please enter your account number:")
                self.validate_user_and_process_request(account_number)
                if self.is_valid_user:
                    self.customer_options()
                else:
                    print("Please provide valid account number")
            elif choice.lower() in self.option_six:
                sys.exit(0)
            else:
                print("Please select options 1 or 2")
                self.show_menu_and_process_request()
        except (KeyboardInterrupt):
            print("\n*****You have interupted or pressed ^C*****")

    def customer_options(self):
        while True:
            choice = input('''
            1.Change Profile            
            2.Money Deposit
            3.Money withdrawal
            4.View Balance
            5.Request Loan
            6.Quit (q)
            7.View Trasactions
            8.Last Recent trasaction
            9.View customer details
            Please enter your choice: ''')
            if choice == "1":
                self.change_profile()
            elif choice == "2":
                self.deposit_money()
                self.update_cust_data()
            elif choice == "3":
                self.withdraw_money()
                self.update_cust_data()
            elif choice == "4":
                self.view_balance()
            elif choice == "5":
                self.loan_check()
            elif choice.lower() in self.option_six:
                break
            elif choice == "7":
                self.transaction_list()
            elif choice == "8":
                self.last_transaction()
            elif choice == "9":
                self.customer_details()
            else:
                self.screen_clear()
                print("Sorry, You have made a wrong choice")
    
    def validate_user_and_process_request(self, account_num):
        with open(self.file_location, 'r') as file:
            for cust_record in file:
                cust_record = ast.literal_eval(cust_record)
                if int(account_num) == cust_record["account_number"]:
                    self.logger.log(self.customer_data)
                    self.customer_data = cust_record
                    self.is_valid_user = True
                    self.logger.log("is the  valid user: {}".format(self.is_valid_user)) 
                    break 
    def change_profile(self):
        try:
            print("At this moment, you can only update your contact details")
            customer_new_contact = int(input("Please enter the new contact:"))
            with open(self.file_location, 'r') as file:
                for cust_record in file:
                    cust_record = ast.literal_eval(cust_record)
                    cust_record["contact_number"] = customer_new_contact
                    self.customer_data = cust_record
                    self.logger.log("New customer details {} has been updated.".format(customer_new_contact))
                    self.cust_data_write_to_file()
        except (KeyboardInterrupt):
            print("\n*****You have interupted or pressed ^C*****")
        except Exception as error:
            self.logger.log(str(error))
            print("We are sorry for inconvience, something went wrong please try again.")

    def open_account(self):
        try:
            self.screen_clear()
            new_account = int(input("Please enter the minimum balance 150 to open your account :"))
            overdraft   = input("Do you like to enable overdraft on your account(Yes or No):").lower()
            if overdraft in self.overdraft_yes:
                self.overdraft_plan = True
            if new_account >= 150:
                self.accnt_balance = new_account
                self.customer_entries()
                self.translist.append("{0}\tYour First account open Balance : {1}".format((self.date), (self.accnt_balance)))
                print("your account opened with new account number {0} and the balance is {1}".format((self.account_number), (self.accnt_balance)))
                self.logger.log("Account opened with new account number {0} and the balance is {1}".format((self.account_number), (self.accnt_balance)))
                self.account_open = True
                self.update_cust_data()
            else:
                print("Minimum Balance ($150) required to open an account,  Your application cannot be processed")
        except Exception as error:
            self.logger.log(str(error))
            print("Please provide the amount in $ Dollars")
        except (KeyboardInterrupt, SystemExit):
            print("\n*****You have interupted or pressed ^C*****")

    def deposit_money(self):
        try:
            self.screen_clear()
            money = int(input("Please enter the amount you would like to deposit:"))
            self.logger.log("user requested {} amount for deposit".format(money))
            with open(self.file_location, 'r+') as file:
                for cust_record in file:
                    cust_record = ast.literal_eval(cust_record)
                    self.accnt_balance = cust_record["balance_avail"]
                    self.accnt_balance += money
                    with open(self.trans_file_location, 'a') as file:
                        file.write("Deposit trasaction of {0}: {1}".format((money), (self.accnt_balance)) + "\n" )
                    self.logger.log("Deposited an amount of {0} and your latest available balance is {1}".format((money), (self.accnt_balance)))
                    print("successfully deposited your money")
        except Exception as error:
            self.logger.log(str(error))
            print("Please provide the amount in $ Dollars")
        except (KeyboardInterrupt, SystemExit):
            print("\n*****You have interupted or pressed ^C*****")  

    def withdraw_money(self):
        try:
            self.screen_clear()
            money = int(input("Please enter the amount you would like to withdraw from account:"))
            self.logger.log("user requested {} amount for withdrawl".format(money))
            with open(self.file_location, 'r+') as file:
                for cust_record in file:
                    cust_record = ast.literal_eval(cust_record)
                    self.accnt_balance = cust_record["balance_avail"]
                    self.overdraft_plan = cust_record["overdraft_plan"]
                    if self.accnt_balance >= money:
                        self.accnt_balance -= money
                        with open(self.trans_file_location, 'a') as file:
                            file.write("withdrawl trasaction of {0}: {1}".format((money), (self.accnt_balance)) + "\n" )
                        self.logger.log("withdrawl an amount of {0} and your latest available balance is {1}".format((money), (self.accnt_balance)))
                        print("successfully money withdrawn")
                    else:
                        if self.accnt_balance <= 0:
                            print("Your Account is already overdrafted or the Balance is '0', Please contact the Bank")
                        else:
                            if self.overdraft_plan:
                                print("You will be charged $12 overdraft penality")
                                overdraft_charges = 12 
                                self.accnt_balance -= money
                                with open(self.trans_file_location, 'a') as file:
                                    file.write("withdrawl trasaction of {0}: {1}".format((money), (self.accnt_balance)) + "\n" )
                                self.logger.log("withdrawl an amount of {0} and your latest available balance is {1}".format((money), (self.accnt_balance)))
                                self.accnt_balance -= overdraft_charges
                                with open(self.trans_file_location, 'a') as file:
                                    file.write("overdraft charges of {0}: {1}".format((overdraft_charges), (self.accnt_balance)) + "\n" )
                                self.logger.log("Over draft penality of {0} and your latest available balance is {1}".format((50), (self.accnt_balance)))
                                print("successfully money withdrawn")    
                            else:
                                print("You will be charged $50 overdraft penality")
                                overdraft_charges = 50
                                self.accnt_balance -= money
                                with open(self.trans_file_location, 'a') as file:
                                    file.write("withdrawl trasaction of {0}: {1}".format((money), (self.accnt_balance)) + "\n" )
                                self.logger.log("withdrawl an amount of {0} and your latest available balance is {1}".format((money), (self.accnt_balance)))
                                self.accnt_balance -= overdraft_charges
                                with open(self.trans_file_location, 'a') as file:
                                    file.write("overdraft charges of {0}: {1}".format((overdraft_charges), (self.accnt_balance)) + "\n" )
                                self.logger.log("Over draft penality of {0} and your latest available balance is {1}".format((50), (self.accnt_balance)))
                                print("successfully money withdrawn")
        except Exception as error:
            self.logger.log(str(error))
            print("Please provide the amount in $ Dollars")
        except (KeyboardInterrupt, SystemExit):
            print("\n*****You have interupted or pressed ^C*****") 
    
    #def withdraw_trasaction(self):
    #    self.accnt_balance -= money
    #    with open(self.trans_file_location, 'a') as file:
    #        file.write("withdrawl trasaction of {0}: {1}".format((money), (self.accnt_balance)) + "\n" )
    #    self.logger.log("withdrawl an amount of {0} and your latest available balance is {1}".format((money), (self.accnt_balance)))
    #    print("successfully money withdrawn")  

    def view_balance(self):
        self.screen_clear()
        with open(self.file_location, 'r') as file:
            for cust_record in file:
                cust_record = ast.literal_eval(cust_record)
                self.accnt_balance = cust_record["balance_avail"]
                self.logger.log("viewed your balance is : {}".format(self.accnt_balance))
                print("your account balance is : {}".format(self.accnt_balance))

    def loan_check(self):
        self.screen_clear()
        self.view_balance()
        if self.accnt_balance >= 500:
            print("We considered your Loan application and it will be processed")
            self.logger.log("Loan application considered")
        else:
            print("No sufficient funds,  we cannot process your application for Loan")
            self.logger.log("Loan application Rejected")

    def account_open_check(self):
        if self.account_open == True :
           return
        else:
           print("Please open account first")
           self.show_menu_and_process_request()
           
    def transaction_list(self):
        self.screen_clear()
        print("Date\t\tTrasaction Type\t\t\t Balance Available")
        print("==================================================================")
        with open(self.trans_file_location, 'r') as file1:  
            trans_contents = file1.readlines()
            for line in trans_contents:
                print(line)

    def last_transaction(self):
        self.screen_clear()
        print("**** Your Last Recent Trascation *** ")
        print("Date\t\tTrasaction Type\t\t\t Balance Available")
        print("==================================================================")
        with open(self.trans_file_location, 'r') as file1:
            trans_contents = file1.readlines()[-1]
            print(trans_contents)

    def screen_clear(self):
        os.system('clear')

    def customer_entries(self):
        self.customer_data["Firstname"]  = input("Enter the customer First name :")
        self.customer_data["Lastname"]   = input("Enter the customer Last name :")
        self.customer_data["contact_number"]    = input("Enter your contact :")
        self.customer_data["overdraft_plan"] = self.overdraft_plan
        self.account_number = randint(0,10000)
        self.customer_data["account_number"] = self.account_number
        self.customer_data["opening_balance"] = self.accnt_balance
        self.cust_data_write_to_file()

    def customer_details(self):
        with open(self.file_location, 'r+') as file:
            for cust_record in file:
                cust_record = ast.literal_eval(cust_record)
                self.customer_data = cust_record
                self.screen_clear()
                print("*********Your Account details*********")
                for (key,value) in self.customer_data.items():
                    print(("\n" "{0}\t:{1}".format((key), (value))) + "\n" )
                self.logger.log("customer verified verified.")

    def update_cust_data(self):
        self.customer_data["balance_avail"] = self.accnt_balance 
        self.cust_data_write_to_file()
    
    def cust_data_write_to_file(self):     
        with open(self.file_location, 'w+') as file:
            file.write(str(self.customer_data) + "\n")

    def open_file_location(self): 
        with open(self.file_location, 'r+') as file:
            for cust_record in file:
                cust_record = ast.literal_eval(cust_record)

    def main(self):
        self.show_menu_and_process_request()



if __name__=="__main__":
    path = "/Users/hima/python/Bank-Project/banking/logs/"
    timestamp = datetime.datetime.strptime(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")
    filename = "session{}".format(timestamp.isoformat().rstrip("."))
    logger = Logger(path, filename)
    krishnas_acnt = Account(logger)
    krishnas_acnt.main()
