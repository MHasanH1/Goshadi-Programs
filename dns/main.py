import ctypes
import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox, ttk

hwnd = ctypes.windll.kernel32.GetConsoleWindow()
if hwnd:
    ctypes.windll.user32.ShowWindow(hwnd, 0)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except AttributeError:
        return False


def elevate():
    executable = sys.executable
    if executable.lower().endswith("python.exe"):
        executable = executable[:-10] + "pythonw.exe"

    params = f'"{os.path.abspath(sys.argv[0])}"'
    if len(sys.argv) > 1:
        params += " " + " ".join(f'"{arg}"' for arg in sys.argv[1:])

    result = ctypes.windll.shell32.ShellExecuteW(
        None, "runas", executable, params, None, 0
    )

    if result > 32:
        sys.exit(0)
    else:
        messagebox.showerror(
            "دسترسی لازم است",
            "برای تغییر تنظیمات DNS به دسترسی ادمین (Administrator) نیاز است.",
        )
        sys.exit(1)


if not is_admin():
    elevate()


DNS_DATA = {
    "رادار (Radar Game)": {
        "primary": "10.202.10.10",
        "secondary": "10.202.10.11",
        "desc": "داخلی؛ مخصوص عبور از تحریم و ثبت سرویس گیمینگ",
    },
    "الکترو (Electro)": {
        "primary": "78.157.42.100",
        "secondary": "78.157.42.101",
        "desc": "داخلی؛ سرعت خوب برای بازی آنلاین",
    },
    "شکن (Shecan)": {
        "primary": "178.22.122.100",
        "secondary": "185.51.200.2",
        "desc": "داخلی؛ مناسب دور زدن تحریم‌ها",
    },
    "بگذر (Begzar)": {
        "primary": "185.55.226.26",
        "secondary": "185.55.225.25",
        "desc": "داخلی؛ عبور از محدودیت‌ها",
    },
    "Quad9": {
        "primary": "9.9.9.9",
        "secondary": "149.112.112.112",
        "desc": "امنیت بالا و کمک به کاهش پینگ در بازی‌های چندنفره",
    },
    "UltraDNS": {
        "primary": "64.6.64.6",
        "secondary": "64.6.65.6",
        "desc": "پایدار و مناسب دانلود بازی",
    },
    "UltraDNS 2": {
        "primary": "156.154.70.2",
        "secondary": "156.154.71.2",
        "desc": "پایدار و مفید در دانلود حجیم",
    },
    "NTT": {
        "primary": "129.250.35.250",
        "secondary": "129.250.35.251",
        "desc": "سرعت دانلود بالا، به‌ویژه برای کاربران ایرانی",
    },
    "OpenDNS / Cisco": {
        "primary": "208.67.222.222",
        "secondary": "208.67.220.220",
        "desc": "بهبود پینگ و سرعت دانلود",
    },
    "Xbox DNS": {
        "primary": "37.220.84.124",
        "secondary": None,
        "desc": "مناسب برای تغییر DNS در ایکس‌باکس",
    },
    "همراه اول (Hamrah-e Aval)": {
        "primary": "208.67.220.200",
        "secondary": "208.67.222.222",
        "desc": "مخصوص اینترنت موبایل",
    },
    "ایرانسل (Irancell)": {
        "primary": "74.82.42.42",
        "secondary": None,
        "desc": "مخصوص اینترنت موبایل",
    },
    "رایتل (Rightel)": {
        "primary": "91.239.100.100",
        "secondary": "89.223.43.71",
        "desc": "مخصوص اینترنت موبایل",
    },
    "Cloudflare (1.1.1.1)": {
        "primary": "1.1.1.1",
        "secondary": "1.0.0.1",
        "desc": "سریع برای وب‌گردی، ولی تأثیر کم روی گیمینگ",
    },
    "Google (8.8.8.8)": {
        "primary": "8.8.8.8",
        "secondary": "8.8.4.4",
        "desc": "مناسب جستجو، اما عموماً برای گیم توصیه نمی‌شود",
    },
    "پاک کردن DNS (Automatic / DHCP)": {
        "primary": None,
        "secondary": None,
        "desc": "تنظیم مجدد DNS به حالت پیش‌فرض و خودکار مودم (DHCP)",
    },
}

INTERFACE_NAME = "Wi-Fi"


def apply_dns():
    selected_name = combo_dns.get()
    if not selected_name or selected_name not in DNS_DATA:
        messagebox.showwarning("خطا", "لطفاً یکی از گزینه‌ها را انتخاب کنید.")
        return

    data = DNS_DATA[selected_name]

    if data["primary"] is None:
        try:
            subprocess.run(
                ["netsh", "interface", "ip", "set", "dns", INTERFACE_NAME, "dhcp"],
                check=True,
                creationflags=subprocess.CREATE_NO_WINDOW,
            )
            messagebox.showinfo("موفقیت", f"تنظیمات DNS کارت شبکه {INTERFACE_NAME} به حالت خودکار (DHCP) بازگردانده شد.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("خطا", f"خطا در بازگردانی تنظیمات DNS:\n{e}")
        return

    try:
        subprocess.run(
            ["netsh", "interface", "ip", "set", "dns", INTERFACE_NAME, "static", data["primary"]],
            check=True,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )

        if data["secondary"] and data["secondary"] != "0.0.0.0":
            subprocess.run(
                ["netsh", "interface", "ip", "add", "dns", INTERFACE_NAME, data["secondary"], "index=2"],
                check=True,
                creationflags=subprocess.CREATE_NO_WINDOW,
            )

        details = f"DNS با موفقیت تنظیم شد:\n\nPrimary: {data['primary']}"
        if data["secondary"] and data["secondary"] != "0.0.0.0":
            details += f"\nSecondary: {data['secondary']}"
        messagebox.showinfo("موفقیت", details)

    except subprocess.CalledProcessError as e:
        messagebox.showerror("خطا", f"خطا در اعمال DNS:\n{e}")


def on_dns_selected(event):
    selected_name = combo_dns.get()
    info = DNS_DATA.get(selected_name, {})
    desc = info.get("desc", "")
    p = info.get("primary") or "Automatic"
    s = info.get("secondary") or "-"
    lbl_details.config(text=f"Primary: {p}\nSecondary: {s}\n\nتوضیحات:\n{desc}")


window = tk.Tk()
window.title("DNS Manager")

w, h = 360, 320
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = int((ws / 2) - (w / 2))
y = int((hs / 2) - (h / 2))
window.geometry(f"{w}x{h}+{x}+{y}")
window.resizable(False, False)

tk.Label(window, text="سرویس DNS مورد نظر را انتخاب کنید:", font=("Segoe UI", 10, "bold")).pack(pady=(12, 5))

combo_dns = ttk.Combobox(window, values=list(DNS_DATA.keys()), state="readonly", width=35, font=("Segoe UI", 9))
combo_dns.current(0)
combo_dns.pack(pady=5)
combo_dns.bind("<<ComboboxSelected>>", on_dns_selected)

lbl_details = tk.Label(
    window,
    text="",
    justify="center",
    wraplength=320,
    font=("Segoe UI", 9),
    bg="#f0f0f0",
    relief="groove",
    padx=10,
    pady=10,
    height=5,
)
lbl_details.pack(fill="x", padx=20, pady=10)

btn_submit = tk.Button(
    window,
    text="اعمال DNS (Apply)",
    bg="#1a73e8",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=apply_dns,
    padx=10,
    pady=4,
    cursor="hand2",
)
btn_submit.pack(pady=10)

on_dns_selected(None)

window.mainloop()