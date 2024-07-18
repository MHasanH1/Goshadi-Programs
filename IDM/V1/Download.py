import os
import urllib.request
from Lib.gui import IDMGui

def selectFile():
    path = instance.createDirectorySelector()
    return path

instance = IDMGui("IDM")

instance.print("Enter Your URL: ", w=20, h=3)
input = instance.createInputField()
instance.setPosition(input,x=200,y=20)

button1 = instance.createButton(selectFile, text="...")
instance.setPosition(button1,x=100,y=50)

instance.run()

# url = input("Enter Your URL: ")
# path = input("Enter Your Path: ")
# fileName = input("Enter Your File Name: ")
# fileType = input("Enter Your File Type: ")
# fullName = fileName + '.' + fileType

# print("Downloading...")
# os.chdir(path)
# urllib.request.urlretrieve(url, fullName)
# print("Downloaded succesfully in " + path + " as " + fullName)
