import tkinter as tk
from tkinter import messagebox
import subprocess
import platform

def ping_address():
    address = entry.get()
    if not address:
        messagebox.showerror("Error", "Please enter an IP address or URL.")
        return

    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "4", address]

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, output)
    except subprocess.CalledProcessError as e:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, e.output)

def clear_entry():
    entry.delete(0, tk.END)

# GUI setup
app = tk.Tk()
app.title("Network Tester")

frame = tk.Frame(app, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter IP address or URL:")
label.grid(row=0, column=0, sticky="w")

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=1, padx=5, pady=5)

ping_button = tk.Button(frame, text="Ping", command=ping_address)
ping_button.grid(row=0, column=2, padx=5, pady=5)

clear_button = tk.Button(frame, text="Clear Entry", command=clear_entry)
clear_button.grid(row=0, column=3, padx=5, pady=5)

text_output = tk.Text(app, height=15, width=70)
text_output.pack(padx=10, pady=10)

signature_label = tk.Label(app, text="Made in Antwerp by Runaque", font=("Arial", 10), fg="slategrey")
signature_label.pack(pady=5)

app.mainloop()
