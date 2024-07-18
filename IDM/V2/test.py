from easygui import *
import os
import urllib.request
import requests
from tkinter import messagebox

text = "Enter the following details"
title = "IDM (Internet Download Manager)"
input_list = ["URL", "Path", "File name", "File type"]
default_list = ["", "", "", ""]
output = multenterbox(text, title, input_list, default_list)

url = output[0]
path = output[1]
filename = output[2]
filetype = output[3]
fullName = filename + '.' +  filetype

messagebox.showinfo("showinfo", "Downloading...") 
os.chdir(path)
try:
    response = requests.get(url)
    with open(fullName, 'wb') as file:
	    file.write(response.content)
except:
    urllib.request.urlretrieve(url, fullName)
messagebox.showinfo("showinfo", "Downloaded succesfully in " + path + " as " + fullName) 