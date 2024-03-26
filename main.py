import tkinter as tk
from tkinter import ttk
import subprocess
import json

def button_click(version, product_key, button):
    subprocess.run(["cmd", "/c", f"slmgr.vbs /ipk {product_key}"])
    button.config(bg="blue", fg="white", state="disabled")

def create_table(root, versions, product_keys):
    table = tk.Frame(root, bg="black")
    table.pack(padx=10, pady=10)

    canvas = tk.Canvas(table, bg="black", height=400)  # Ustawienie większej wysokości
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(table, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    inner_frame = tk.Frame(canvas, bg="black")
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    buttons = []

    for i, (version, product_key) in enumerate(zip(versions, product_keys)):
        label_version = tk.Label(inner_frame, text=version, bg="black", fg="white", width=30)
        label_version.grid(row=i, column=0)

        label_key = tk.Label(inner_frame, text=product_key, bg="black", fg="white", width=30)
        label_key.grid(row=i, column=1)

        button = ttk.Button(inner_frame, text="Activate")
        button.grid(row=i, column=2)
        button.bind("<Enter>", lambda event, b=button: b.config(bg="blue", fg="white"))
        button.bind("<Leave>", lambda event, b=button: b.config(bg="white", fg="black"))
        button.config(command=lambda v=version, pk=product_key, btn=button: button_click(v, pk, btn))
        buttons.append(button)

    return buttons

def load_data_from_json(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
    return data

def main():
    okno = tk.Tk()
    okno.title("Windows Version Activator")
    okno.configure(bg="black")

    versions_data = load_data_from_json("versions.json")
    product_keys_data = load_data_from_json("product_keys.json")

    versions, product_keys = versions_data["versions"], product_keys_data["product_keys"]

    buttons = create_table(okno, versions, product_keys)

    okno.mainloop()

if __name__ == "__main__":
    main()
