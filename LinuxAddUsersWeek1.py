#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 09:57:58 2020

@author: charlie
"""
#import csv
import os
import sys
filename = "users.csv"


if len(sys.argv) == 1:
	print("\tUsage: python3 AddUsers.py <country> <intel/telecom>")
	sys.exit(3)

country = sys.argv[1]
area = sys.argv[2]

#with open(filename, 'r') as data:
    #for line in csv.reader(data):
        #print(line)

setofallsets = [
# This data structure is redacted for containing passwords and other information potentially useful to students in COSC 481. If you're a student and you've found this, nice try :)
]

# These prefixes have also been redacted and replaced with 'xxx'
if area == "intel":
    if country == "china":
        c = 0
        prefix = "xxx"
    elif country == "england":
        c = 4
        prefix = "xxx"
    elif country == "france":
        c = 8
        prefix = "xxx"
    elif country == "germany":
        c = 12
        prefix = "xxx"
    elif country == "japan":
        c = 16
        prefix = "xxx"
    elif country == "rome":
        c = 20
        prefix = "xxx"
    elif country == "russia":
        c = 24
        prefix = "xxx"
    elif country == "spain":
        c = 28
        prefix = "xxx"
    else:
        print("specify a proper country in all lowercase.")
        sys.exit(3)
elif area == "telecom":
    if country == "china":
        c = 0
        prefix = "xxx"
    elif country == "england":
        c = 4
        prefix = "xxx"
    elif country == "france":
        c = 8
        prefix = "xxx"
    elif country == "germany":
        c = 12
        prefix = "xxx"
    elif country == "japan":
        c = 16
        prefix = "xxx"
    elif country == "rome":
        c = 20
        prefix = "xxx"
    elif country == "russia":
        c = 24
        prefix = "xxx"
    elif country == "spain":
        c = 28
        prefix = "xxx"
    else:
        print("specify a proper country in all lowercase.")
        sys.exit(3)
else:
    print("specify either telecom or intel")
    sys.exit(3)


os.system("groupadd IT")
os.system("groupadd intel")
os.system("groupadd telecom")
    
for d in setofallsets:
    title = d[1]
    fname = d[2+c]
    lname = d[3+c]
    user = d[4+c]
    passwd = d[5+c]
    print("title: {}, fname: {}, lname: {}, user: {}, passwd: {}".format(title,fname,lname,user,passwd))
    
    os.system("useradd -s /bin/bash -p $(openssl passwd -1 {}{}) {}".format(prefix,passwd,user))
    os.system("usermod -c \"{} {}\" {}".format(fname,lname,user))
    if title == "Telecommunications Officer":
        os.system("usermod -a -G telecom {}".format(user))
    elif title == "Intelligence Officer":
        os.system("usermod -a -G intel {}".format(user))
    elif title == "IT Staff":
        os.system("usermod -a -G IT {}".format(user))
        

os.system("rm .bash_history")
