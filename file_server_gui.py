import os
import subprocess
import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk
import socket

def start_server(folder_path):
    global server_process
    command = f'python -m http.server 8000 --directory "{folder_path}"'
    server_process = subprocess.Popen(command, shell=True)

def stop_server():
    if server_process:
        server_process.terminate()
        status_label.config(text="Server stopped")
    else:
        status_label.config(text="Server not running")

def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    folder_label.config(text=f"Selected Folder: {folder_path}")
    
def run_server():
    if folder_path:
            start_server(folder_path)
            status_label.config(text=f"Server running for {folder_path}")
            show_qr_code()

def show_qr_code():
    hostname = socket.gethostname()
    # getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    server_address = f"http://{ip_address}:8000"
    qr = qrcode.make(server_address)
    qr = qr.resize((200, 200))
    qr_image = ImageTk.PhotoImage(qr)
    qr_label.config(image=qr_image)
    qr_label.image = qr_image



# Create the main window
root = tk.Tk()
root.title("Simple File Server")
root.geometry("350x350")  # Set window size

# Selected Folder Label
folder_label = tk.Label(root, text="Selected Folder: None")
folder_label.pack()

# Select Folder Button
select_folder_button = tk.Button(root, text="Select Folder", command=select_folder)
select_folder_button.pack()

# Run Server Button
run_server_button = tk.Button(root, text="Run Server", command=lambda: run_server())
run_server_button.pack()

# Status Label
status_label = tk.Label(root, text="Server not running")
status_label.pack()

# QR Code Label
qr_label = tk.Label(root)
qr_label.pack()

# Stop Server Button
stop_server_button = tk.Button(root, text="Stop Server", command=stop_server)
stop_server_button.pack()

# Run the main loop
root.mainloop()