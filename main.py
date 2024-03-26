import tkinter as tk
from tkinter import ttk
import subprocess
import json

def button_click(version_var, product_key_var):
    version = version_var.get()
    product_key = product_key_var.get()
    if version and product_key:
        subprocess.run(["cmd", "/c", f"slmgr.vbs /ipk {product_key}"])

def create_table(root, versions, product_keys, version_var, product_key_var):
    table = tk.Frame(root, bg="white")
    table.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(table, bg="white")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(table, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    inner_frame = tk.Frame(canvas, bg="white")
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    for i, (version, product_key) in enumerate(zip(versions, product_keys)):
        label_version = tk.Label(inner_frame, text=version, bg="white", fg="black", width=30)
        label_version.grid(row=i, column=0)

        label_key = tk.Label(inner_frame, text=product_key, bg="white", fg="black", width=30)
        label_key.grid(row=i, column=1)

        button = ttk.Button(inner_frame, text="Select", command=lambda v=version, pk=product_key: select_version(v, pk, version_var, product_key_var))
        button.grid(row=i, column=2)

def select_version(version, product_key, version_var, product_key_var):
    version_var.set(version)
    product_key_var.set(product_key)

def main():
    okno = tk.Tk()
    okno.title("Windows Version Activator")
    okno.configure(bg="white")

    versions_data = load_data_from_json("versions.json")
    product_keys_data = load_data_from_json("product_keys.json")

    versions, product_keys = versions_data["versions"], product_keys_data["product_keys"]

    version_var = tk.StringVar()
    product_key_var = tk.StringVar()

    create_table(okno, versions, product_keys, version_var, product_key_var)

    button_frame = tk.Frame(okno, bg="white")
    button_frame.pack(pady=10)

    activate_button = ttk.Button(button_frame, text="Activate", command=lambda: button_click(version_var, product_key_var))
    activate_button.pack()

    okno.mainloop()

if __name__ == "__main__":
    main()
