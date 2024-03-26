import tkinter as tk
from tkinter import ttk
import subprocess
import json

def activate_product(product_key_var):
    product_key = product_key_var.get()
    if product_key:
        subprocess.run(["cmd", "/c", f"slmgr.vbs /ipk {product_key}"])

def create_table(root, versions, product_keys, product_key_var, search_text, scrollbar):
    # Usunięcie poprzedniej tabeli, jeśli istnieje
    for widget in root.winfo_children():
        if isinstance(widget, ttk.Treeview):
            widget.destroy()

    # Utworzenie nowej tabeli
    table = ttk.Treeview(root, columns=("Version", "Product Key"), show="headings")
    table.heading("Version", text="Version")
    table.heading("Product Key", text="Product Key")
    table.pack(fill=tk.BOTH, expand=True)

    if scrollbar is None:
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=table.yview)
        scrollbar.pack(side="right", fill="y")
    else:
        scrollbar.configure(command=table.yview)
    
    table.configure(yscrollcommand=scrollbar.set)

    filtered_versions = [version for version in versions if search_text.lower() in version.lower()]

    for version, product_key in zip(filtered_versions, product_keys):
        table.insert("", "end", values=(version, product_key))

    table.bind("<ButtonRelease-1>", lambda event: on_select(table, product_key_var))

def on_select(table, product_key_var):
    item = table.selection()[0]
    version, product_key = table.item(item, "values")
    product_key_var.set(product_key)

def load_data_from_json(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
    return data

def on_search():
    search_text = search_var.get()
    create_table(root, versions, product_keys, product_key_var, search_text, scrollbar)

def main():
    global root, search_var, versions, product_keys, product_key_var, scrollbar

    root = tk.Tk()
    root.title("Windows Version Activator")

    versions_data = load_data_from_json("versions.json")
    product_keys_data = load_data_from_json("product_keys.json")

    versions, product_keys = versions_data["versions"], product_keys_data["product_keys"]

    product_key_var = tk.StringVar()
    scrollbar = None

    search_frame = tk.Frame(root)
    search_frame.pack(pady=(10, 0))

    search_label = tk.Label(search_frame, text="Search:")
    search_label.pack(side=tk.LEFT)

    search_var = tk.StringVar()
    search_var.trace_add("write", lambda *args: on_search())
    search_entry = ttk.Entry(search_frame, textvariable=search_var)
    search_entry.pack(side=tk.LEFT)

    create_table(root, versions, product_keys, product_key_var, "", scrollbar)

    activate_button = ttk.Button(root, text="Activate", command=lambda: activate_product(product_key_var))
    activate_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
