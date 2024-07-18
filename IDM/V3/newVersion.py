import os
import urllib.request
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import requests

ROOT = tk.Tk()
ROOT.withdraw()

url = simpledialog.askstring(title="Test", prompt="What's your URL?:")
path = simpledialog.askstring(title="Test", prompt="What's your Path?:")
fileName = simpledialog.askstring(title="Test", prompt="What's your FileName?:")
fileType = simpledialog.askstring(title="Test", prompt="What's your FileType?:")
fullName = fileName + '.' +  fileType

messagebox.showinfo("showinfo", "Downloading...") 
os.chdir(path)
try:
    response = requests.get(url)
    with open(fullName, 'wb') as file:
	    file.write(response.content)
except:
    urllib.request.urlretrieve(url, fullName)
    
messagebox.showinfo("showinfo", "Downloaded succesfully in " + path + " as " + fullName) 