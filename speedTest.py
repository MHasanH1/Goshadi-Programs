import speedtest
import tkinter as tk
from tkinter import *

def perform_speed_test():
   print("choosing the best servers...")
   st = speedtest.Speedtest()
   servers = st.get_best_server()

   print("Testing download speed...")
   download_speed = st.download() / 1000000  # Convert to Mbps
   dSpeed.config(text=download_speed)
   print("Testing upload speed...")
   upload_speed = st.upload() / 1000000  # Convert to Mbps
   uSpeed.config(text=upload_speed)
   print("Download Speed: {:.2f} Mbps".format(download_speed))
   print("Upload Speed: {:.2f} Mbps".format(upload_speed))

   return download_speed, upload_speed

window = tk.Tk()
w = 200
h = 150

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))

tk.Button (
   text="Test",
   fg="yellow",
   bg="black",
   command=perform_speed_test
).pack()

download_speed = 0
upload_speed = 0

dSpeed = tk.Label (
   text=download_speed,
   fg="black",
   bg="blue"
)

uSpeed = tk.Label (
   text=upload_speed,
   fg="black",
   bg="green"
)

dSpeed.pack()
uSpeed.pack()

window.mainloop()