import tkinter as tk
from tkinter import ttk
import subprocess
import json

def button_click():
    selected_item = treeview.selection()
    if selected_item:
        version = treeview.item(selected_item, "values")[0]
        product_key = treeview.item(selected_item, "values")[1]
        subprocess.run(["cmd", "/c", f"slmgr.vbs /ipk {product_key}"])

def search(event):
    search_text = search_entry.get().lower()
    for item in treeview.get_children():
        version = treeview.item(item, "values")[0].lower()
        if search_text in version:
            start = version.index(search_text)
            end = start + len(search_text)
            treeview.item(item, tags=("search",))
        else:
            treeview.item(item, tags=(""))

def create_table(root, versions, product_keys):
    global treeview
    treeview = ttk.Treeview(root, columns=("Version", "Product Key"), show="headings")
    treeview.heading("Version", text="Version")
    treeview.heading("Product Key", text="Product Key")
    treeview.pack(fill="both", expand=True)

    for version, product_key in zip(versions, product_keys):
        treeview.insert("", "end", values=(version, product_key))

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    global search_entry
    search_entry = tk.Entry(button_frame)
    search_entry.pack(side="right", padx=10)
    search_entry.bind("<KeyRelease>", search)

    activate_button = ttk.Button(button_frame, text="Activate", command=button_click)
    activate_button.pack(side="right")

def load_data_from_json(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
    return data

def main():
    okno = tk.Tk()
    okno.title("Windows Version Activator")

    versions_data = load_data_from_json("versions.json")
    product_keys_data = load_data_from_json("product_keys.json")

    versions, product_keys = versions_data["versions"], product_keys_data["product_keys"]

    create_table(okno, versions, product_keys)

    okno.mainloop()

if __name__ == "__main__":
    main()
