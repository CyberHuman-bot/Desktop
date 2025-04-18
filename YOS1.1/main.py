import os
import shutil

def create_os_structure(base_path):
    os.makedirs(base_path, exist_ok=True)

    # Define folders
    folders = [
        "kernel",
        "boot",
        "drivers",
        "filesystem",
        "apps/browser",
        "apps/internet",
        "config",
        "user_files"
    ]

    # Create folders
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

    print("OS structure created.")

    # Create essential files
    with open(os.path.join(base_path, "kernel/kernel.c"), "w") as f:
        f.write("// Placeholder for kernel code\n")

    with open(os.path.join(base_path, "boot/bootloader.asm"), "w") as f:
        f.write("; Placeholder for bootloader code\n")

    with open(os.path.join(base_path, "drivers/network_driver.c"), "w") as f:
        f.write("// Placeholder for network driver\n")

    with open(os.path.join(base_path, "apps/browser/browser.py"), "w") as f:
        f.write(
            """import tkinter as tk
from tkinter import ttk
import webbrowser

def open_browser():
    root = tk.Tk()
    root.title('YOS Browser')
    
    def load_url():
        url = url_entry.get()
        if not url.startswith('http'):
            url = 'http://' + url
        webbrowser.open(url)

    tk.Label(root, text='Enter URL:').pack(pady=5)
    url_entry = tk.Entry(root, width=50)
    url_entry.pack(pady=5)
    tk.Button(root, text='Go', command=load_url).pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    open_browser()
            """
        )

    with open(os.path.join(base_path, "apps/internet/network.py"), "w") as f:
        f.write("""import socket

# Placeholder for basic internet functionality
def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53))
        return True
    except OSError:
        return False

if __name__ == '__main__':
    if check_internet():
        print("Internet is working.")
    else:
        print("No internet connection.")
        """)

    with open(os.path.join(base_path, "config/system.yf"), "w") as f:
        f.write(
            """# YOS Configuration File
system_name="YOS"
default_browser="apps/browser/browser.py"
default_network_tool="apps/internet/network.py"
"""
        )

    print("Essential files created.")

def zip_os(base_path, output_file):
    shutil.make_archive(output_file, 'zip', base_path)
    print(f"OS zipped into {output_file}.zip")

if __name__ == "__main__":
    # Change base path to your desktop
    base_path = r"C:\Users\Lenovo\Desktop\YOS1.1"
    output_file = base_path  # The zip file will also be created on the desktop

    create_os_structure(base_path)
    zip_os(base_path, output_file)
