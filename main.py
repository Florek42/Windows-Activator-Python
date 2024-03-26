import tkinter as tk
from tkinter import ttk
import subprocess
import json

def activate_product(product_key_var):
    product_key = product_key_var.get()
    if product_key:
        subprocess.run(["cmd", "/c", f"slmgr.vbs /ipk {product_key}"])

def create_table(root, versions, product_keys, product_key_var):
    table = tk.Frame(root, bg="white")
    table.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Nazwy kolumn
    tk.Label(table, text="Version", bg="white", fg="black", width=30).grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Product Key", bg="white", fg="black", width=30).grid(row=0, column=1, sticky="ew")

    canvas = tk.Canvas(table, bg="white")
    canvas.grid(row=1, columnspan=2, sticky="nsew")

    scrollbar = ttk.Scrollbar(table, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.grid(row=1, column=2, sticky="ns")
    canvas.configure(yscrollcommand=scrollbar.set)

    inner_frame = tk.Frame(canvas, bg="white")
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    for i, (version, product_key) in enumerate(zip(versions, product_keys), start=1):
        tk.Label(inner_frame, text=version, bg="white", fg="black", width=30, anchor="w").grid(row=i, column=0, sticky="ew")
        tk.Label(inner_frame, text=product_key, bg="white", fg="black", width=30, anchor="w").grid(row=i, column=1, sticky="ew")

        # Bindowanie zdarzenia kliknięcia na dany wiersz
        inner_frame.grid_rowconfigure(i, weight=1)
        inner_frame.grid_columnconfigure(0, weight=1)
        inner_frame.grid_columnconfigure(1, weight=1)

        inner_frame.bind("<Button-1>", lambda event, v=version, pk=product_key_var: select_version(v, pk, product_key_var))

    inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def select_version(version, product_key, product_key_var):
    product_key_var.set(product_key)

def load_data_from_json(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
    return data

def main():
    okno = tk.Tk()
    okno.title("Windows Version Activator")
    okno.configure(bg="white")

    versions_data = load_data_from_json("versions.json")
    product_keys_data = load_data_from_json("product_keys.json")

    versions, product_keys = versions_data["versions"], product_keys_data["product_keys"]

    product_key_var = tk.StringVar()

    create_table(okno, versions, product_keys, product_key_var)

    search_frame = tk.Frame(okno, bg="white")
    search_frame.pack(pady=(0, 10))

    search_label = tk.Label(search_frame, text="Search:", bg="white", fg="black")
    search_label.pack(side=tk.LEFT)

    search_var = tk.StringVar()
    search_entry = ttk.Entry(search_frame, textvariable=search_var)
    search_entry.pack(side=tk.LEFT)

    activate_button = ttk.Button(okno, text="Activate", command=lambda: activate_product(product_key_var))
    activate_button.pack()

    okno.mainloop()

if __name__ == "__main__":
    main()
