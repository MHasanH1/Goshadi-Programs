import subprocess
import tkinter as tk
from tkinter import *
import ctypes
import subprocess

def clear_dns_windows():
  try:
    subprocess.run(
      ["netsh", "interface", "ip", "set", "dns", interface_name, "static", "none"],
      check=True
    )
    print(f"DNS servers for {interface_name} cleared")
  except subprocess.CalledProcessError as e:
    print(f"Failed to clear DNS: {e}")

def set_dns_windows():
  interface_name = "Wi-Fi"
  if (_403online.get() == 1):
    primary_dns = "10.202.10.202"
    secondary_dns = "10.202.10.102"
  elif (ciscoOpenDNS.get() == 1):
    primary_dns = "208.67.222.222"
    secondary_dns = "208.67.220.220"
  elif (empty.get() == 1):
     clear_dns_windows()
     return

  try:
    subprocess.run(
        ["netsh", "interface", "ip", "set", "dns", interface_name, "static", primary_dns],
        check=True
    )
    subprocess.run(
        ["netsh", "interface", "ip", "add", "dns", interface_name, secondary_dns, "index=2"],
        check=True
    )
    print(f"Primary DNS server for {interface_name} set to {primary_dns}")
    print(f"Secondary DNS server for {interface_name} set to {secondary_dns}")
  except subprocess.CalledProcessError as e:
    print(f"Failed to set DNS: {e}")

window = tk.Tk()

w = 200
h = 150

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))

interface_name = "Wi-Fi"
primary_dns = ""
secondary_dns = ""

tk.Label(
  text='select dns to set: '
).pack()

_403online = IntVar()
tk.Checkbutton(
  variable = _403online,
  text = "403 online"
).pack()

ciscoOpenDNS = IntVar()
tk.Checkbutton(
  variable = ciscoOpenDNS,
  text = "Cisco Open DNS"
).pack()

empty = IntVar()
tk.Checkbutton(
  variable = empty,
  text = "empty"
).pack()

tk.Button(
  window,
  text="submit",
  fg="white",
  bg="black",
  command=set_dns_windows
).pack()

window.mainloop()

input("Press enter to continue...")