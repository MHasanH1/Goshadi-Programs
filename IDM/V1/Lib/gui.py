import tkinter as tk
from tkinter import *
from tkinter import filedialog

class IDMGui():
    def __init__(self,title):
        mywindow=tk.Tk()
        self.window=mywindow
        self.window.title(title)
        self.window.geometry("500x300")
    
    def resizeWindow(self,width=500,height=300):
        string= f"{width}x{height}"
        self.window.geometry(string)

    def createButton(self,function,text="",width=5,height=1,**kwargs):
        fg=kwargs.get('fg',None)
        bg=kwargs.get('bg',None)
        imagePath=kwargs.get('image',None)
        activeback=kwargs.get("activebackground",None)
        activefore=kwargs.get("activeforeground",None)
        click_btn=None
        if imagePath!=None:
            click_btn= PhotoImage(file=imagePath)
        button=tk.Button(self.window,text=text,command=function,fg=fg,width=width, height=height,
                         background=bg,image=click_btn,activebackground=activeback,activeforeground=activefore)
                         
        return button
    
    def createLabel(self,labelText=""):
        label=Label(self.window,text=labelText)
        return label 
    
    def createInputField(self,labelText=""):
        entry = Entry(self.window)
        return entry

    def createDirectorySelector(self):
        self.window.withdraw()
        file_path = filedialog.askdirectory()
        return file_path

    def setPosition(self, object, x=0, y=0):
        object.place(x=x, y=y)

    def print(self, text, **kwargs):
        width = kwargs.get("w", None)
        height = kwargs.get("h", None)
        T = Text(self.window, height = height, width = width)
        T.pack()
        T.insert(tk.END, text)

    def run(self):
        self.window.mainloop()

    

        

    

