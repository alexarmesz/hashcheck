import sys
import hashlib
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import ttk

BUF_SIZE = 65536 

'''def hashselect():

    print("(1) SHA256 \n(2) SHA512 \n(3) MD5")
    choice=input("")
    if choice =="1":
        type = ("SHA256")
        hash = hashlib.sha256()
        openfile(hash)
        output(type, hash)
    elif choice =="2":
        type = ("SHA512")
        hash = hashlib.sha512()
        openfile(hash)
        output(type, hash)
    elif choice=="3":
        type = ("MD5")
        hash = hashlib.md5()
        openfile(hash)
        output(type, hash)
    else:
        print("Please enter a valid option.")
        hashselect()'''

def hashchoice(choice, file):
    if choice =="1":
        type = ("SHA256")
        hash = hashlib.sha256()
        #output(type, hash)
    elif choice =="2":
        type = ("SHA512")
        hash = hashlib.sha512()
        #output(type, hash)
    elif choice=="3":
        type = ("MD5")
        hash = hashlib.md5()
        #output(type, hash)
    else:
        print("Please enter a valid option.")
        hashchoice()

    with open((file), 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                return hash
                outputCheck(hash, submission)
                #root.destroy()
                break
            hash.update(data)

def outputCheck():
# take inputs from hash and submission seperately defaulted to none
 pass    

'''def openfile(hash):
    file = askopenfilename()
    print(file)
    with open((file), 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                #root.destroy()
                break
            hash.update(data)'''



    


'''def output(type, hash):   
    print(type+": {0}".format(hash.hexdigest()))
    check=input("\nEnter hash value to check against\n")
    print(hash.hexdigest())
    if hash.hexdigest()==check:
        print("They match")
    else:
        print("They do not match")'''
