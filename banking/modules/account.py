#!/usr/bin/env python2
import sys,os,datetime,time
os.system('cls' if os.name == 'nt' else 'clear')

"""
View Trascations and last transacation has been added.
"""


class Account:
    def __init__(self):
        print("Welcome to BOFA")
        self.accnt_balance = 0
        self.translist = []
        self.date = datetime.date.today()
        self.option_six = ["6",  "Q", "q",  "quit", "Quit"]
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
                self.screen_clear()
                new_account = int(input("Please enter the minimum balance 150 to open your account :"))
                overdraft   = input("Do you like to enable overdraft on your account(Yes or No):").lower()
                if new_account >= 150:
                    self.accnt_balance = new_account
                    self.translist.append("{0}\tYour First account open Balance : {1}".format((self.date), (self.accnt_balance)))
                    self.open_account()
                else:
                    print("Minimum Balance ($150) required to open an account,  Your application cannot be processed")
            elif choice == "2":
                self.screen_clear()
                money = int(input("Please enter the amount you would like to deposit:"))
                self.deposit_money(money)
            elif choice == "3":
                self.screen_clear()
                money = int(input("Please enter the amount you would like to withdraw from account:"))
                if self.accnt_balance >= money:
                    self.withdraw_money(money)
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
            elif choice == "4":
                self.screen_clear()
                self.view_balance()
            elif choice == "5":
                self.screen_clear()
                if self.accnt_balance >= 500:
                    print("We considered your Loan application and it will be processed")
                else:
                    print("No sufficient funds,  we cannot process your application for Loan")
            elif choice in self.option_six:
                break
            elif choice == "7":
                self.screen_clear()
                print("Date\t\tTrasaction Type\t\t\t Balance Available")
                print("==================================================================")
                for list in self.translist:
                    print(list)
            elif choice == "8":
                self.screen_clear()
                print("**** Your Last Recent Trascation *** ")
                print(self.translist[-1])
            else:
                print("Sorry, You have made a wrong choice")
            

    def open_account(self):
        print("your account opened with new balance  : {}".format(self.accnt_balance))

    def deposit_money(self, money):
        self.accnt_balance += money
        self.translist.append("{0}\tDeposit trasaction\t\t: {1}".format((self.date), (self.accnt_balance)))
        print("successfully deposited money")

    def withdraw_money(self, money):
        self.accnt_balance -= money
        self.translist.append("{0}\tWithdraw trasaction\t\t: {1}".format((self.date), (self.accnt_balance)))
        print("successfully money withdrawn")

    def view_balance(self):
        print("your account balance is : {}".format(self.accnt_balance))
    def screen_clear(self):
        os.system('clear')
    

krishnas_acnt = Account()
