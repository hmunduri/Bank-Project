#!/usr/bin/env python2
import sys,os,datetime,time
from random import randint

os.system('cls' if os.name == 'nt' else 'clear')

"""
View Trascations and last transacation has been added.
"""


class Account:
    def __init__(self):
        print("Welcome to BOFA")
        self.accnt_balance = 0
        self.translist = []
        self.customer_data = {}
        self.test_key = 0 
        self.date = datetime.date.today()
        self.option_six = ["6",  "q", "quit"]
        self.overdraft_yes = ["y",  "yes"]
        self.show_menu_and_process_request()

    def show_menu_and_process_request(self):
        while True:
            choice = input( '''
            1.Open Account
            2.Money Deposit
            3.Money withdrawal
            4.View Balance
            5.Request Loan
            6.Quit (q)
            7.View Trasactions
            8.Last Recent trasaction

            Please enter your choice: ''')
            if choice == "1":
                self.open_account()
            elif choice == "2":
                self.deposit_money()
            elif choice == "3":
                self.withdraw_money()
            elif choice == "4":
                self.view_balance()
            elif choice == "5":
                self.loan_check()
            elif choice in self.option_six:
                break
            elif choice == "7":
                 self.transaction_list() 
            elif choice == "8":
                 self.last_transaction()
            elif choice == "8":
                 account_check()
            else:
                self.screen_clear()
                print("Sorry, You have made a wrong choice")
            

    def open_account(self):
        self.screen_clear()
        new_account = int(input("Please enter the minimum balance 150 to open your account :"))
        overdraft   = input("Do you like to enable overdraft on your account(Yes or No):").lower()
        if new_account >= 150:
            self.customer_details()
            self.accnt_balance = new_account
            self.translist.append("{0}\tYour First account open Balance : {1}".format((self.date), (self.accnt_balance)))
            print("your account opened with new account number {0} and the balance is {1}".format((self.account_number), (self.accnt_balance)))
        else:
            print("Minimum Balance ($150) required to open an account,  Your application cannot be processed")

    def deposit_money(self):
        self.screen_clear()
        money = int(input("Please enter the amount you would like to deposit:"))
        self.accnt_balance += money
        self.translist.append("{0}\tDeposit trasaction\t\t: {1}".format((self.date), (self.accnt_balance)))
        print("successfully deposited your money")

    def withdraw_money(self):
        self.screen_clear()
        money = int(input("Please enter the amount you would like to withdraw from account:"))
        if self.accnt_balance >= money:
            self.accnt_balance -= money
            self.translist.append("{0}\tWithdraw trasaction\t\t: {1}".format((self.date), (self.accnt_balance)))
            print("successfully money withdrawn")
        else:
            if self.accnt_balance <= 0:
                print("Your Account is already overdrafted or the Balance is '0', Please contact the Bank")
            else:
                if overdraft in self.overdraft_yes:
                    print("You will be charged $12 overdraft penality")
                    self.accnt_balance -= 12
                    self.withdraw_money(money)
                else:
                    print("You will be charged overdraft penality")
                    self.accnt_balance -= 50
                    self.withdraw_money(money)
    def view_balance(self):
        self.screen_clear()
        print("your account balance is : {}".format(self.accnt_balance))
    def loan_check(self):
        self.screen_clear()
        if self.accnt_balance >= 500:
            print("We considered your Loan application and it will be processed")
        else:
            print("No sufficient funds,  we cannot process your application for Loan")
    def transaction_list(self):
        self.screen_clear()
        print("Date\t\tTrasaction Type\t\t\t Balance Available")
        print("==================================================================")
        for list in self.translist:
            print(list)
    def last_transaction(self):
        self.screen_clear()
        print("**** Your Last Recent Trascation *** ")
        print("Date\t\tTrasaction Type\t\t\t Balance Available")
        print("==================================================================")
        print(self.translist[-1])
    def screen_clear(self):
        os.system('clear')
    def customer_details(self):
        self.customer_data.append[Firstname]  = input("Enter the customer Last name :").split()
        Lastname  = input("Enter the customer Last name :").split()
        Contact = input("Enter your contact :").split()
        self.customer_data.append
        self.account_number = randint(0,10000)
        self.customer_data[self.account_number] = {Firstname,Lastname,Contact}
        print(self.customer_data)
krishnas_acnt = Account()
