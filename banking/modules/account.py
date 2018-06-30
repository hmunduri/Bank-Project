#!/usr/bin/env python3
import sys


class Account:
    def __init__(self):
        print("Welcome to BOFA")
        self.accnt_balance = 0
        self.show_menu_and_process_request()

    def show_menu_and_process_request(self):
        choice = input( '''
        1.Open Account
        2.Money Deposit
        3.Money withdrawal
        4.View Balance

        Please enter your choice: ''')
        
        if choice == "1":
            new_account = int(input("Please enter the minimum balance 150 to open your account :"))
            if new_account >= 150:
                self.open_account()
            else:
                print("No sufficient Your application is declined")
        elif choice == "2":
            self.deposit_money(20)
        elif choice == "3":
            self.withdraw_money(30)
        elif choice == "4":
            self.view_balance()
        else:
            print("Please select the correct choice from above")



    def open_account(self):
        self.accnt_balance += 150 # 10 += 100 is nothing but 100 + 10
        print("your account opened with minimum balance: {}".format(self.accnt_balance))

    def deposit_money(self, money):
        self.accnt_balance += money
        print("successfully deposited moeny")

    def withdraw_money(self, money):
        self.accnt_balance -= money
        print("successfully money withdrawn")

    def view_balance(self):
        print("your accoutn balance is : {}".format(self.accnt_balance))



krishnas_acnt = Account()
