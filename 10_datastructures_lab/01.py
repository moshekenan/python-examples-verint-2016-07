# -*- coding: utf-8 -*-
"""
excersize #1
Check username and password
"""

#list of valid usernames and passwords
valid_accounts = {'apple' : 'red', 'lettuce' : 'green', 'lemon' : 'yellow', 'orange' : 'orange' }

#user input
user_name = raw_input("Please enter username: ")
password = raw_input("Please enter password: ")

#return_str = "access denied"
return_str = u"אין כניסה"

#check validity
for valid in valid_accounts:
    if user_name == valid and password == valid_accounts[valid]:
        #return_str = "Welcome"
        return_str = u"ברוכים הבאים"        

print return_str        
