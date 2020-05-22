# -*- coding: utf-8 -*-
"""
Created on Sun May 10 15:10:03 2020

@author: Ravi
"""


class atm:
    
    def __init__(self):
        self.balance=1000
        self.pin='12345'
        self.count=0
        
        print("Hello welcome to MyBank ATM.")
    
    def function(self):
        while 1:
            d=input('Please enter your five digit pin? ')
            if d==self.pin:
                user=input('Press 1 for Withdraw\nPress 2 for Deposit\nPress 3 for Balance\nPress 4 for Exit\n')
                if user=='1':
                    money=int(input('How much do you want to withdraw? '))
                    if money%100==0 and money<= self.balance and money>=100:
                        self.balance=self.balance-money
                        print('The withdrawn amount is ',money)
                        print('The updated balance is ',self.balance)
                    else:
                        
                        print('Invalid amount: Please note, the amount entered should be a multiple of 100, should be greater than 100 and less than the principal amount')
                        
                if user=='2':
                    
                    newmoney=int(input('How much do you want to deposit? '))
                    if newmoney%100==0 and newmoney>=100:
                        self.balance=self.balance+newmoney
                        print('You deposited ',newmoney)
                        print('The new amount is ',self.balance)
                    else:
                        print('Invalid amount: Please note that the amount should be a multiple of 100 and greater than or equal 100')
                
                if user=='3':
                    print('The balance is',self.balance)
                   
                if user=='4':
                    break
                redo=input('Do you want to continue or exit?[y/n] ')
                if redo.lower()=='y':
                    continue
                else:
                    break
            else:
                self.count=self.count+1
                print('Invalid Pin ur left with ',3-self.count,'option')
                if self.count==3:
                    print('ATM Blocked. PIN entered incorrectly three times')
                    break
             
t=atm()
t.function()