import tkinter as tk
from tkinter import ttk
import subprocess

nazwy_wersji = [
    "Home_Core",
    "Home_Core(Country Specific)",
    "Home_Core(Single Language)",
    # Wszystkie inne nazwy wersji...
]

klucze_produktu = [
    "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99",
    "PVMJN-6DFY6-9CCP6-7BKTT-D3WVR",
    # Wszystkie inne klucze produktu...
]

def klikniecie_przycisku(nazwa_wersji, klucz_produktu):
    subprocess.run(["cmd", "/c", f"slmgr.vbs /ipk {klucz_produktu}"])

okno = tk.Tk()
okno.title("Informacje o wersji i kluczu Windows")

# Utwórz ramkę z przewijanym obszarem
ramka = tk.Frame(okno)
ramka.pack(padx=10, pady=10)

# Utwórz przewijany obszar
scrollbar = tk.Scrollbar(ramka)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Utwórz listę rozwijaną w ramce
lista_rozwijana = tk.Listbox(ramka, yscrollcommand=scrollbar.set, height=15, width=80)
scrollbar.config(command=lista_rozwijana.yview)
lista_rozwijana.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Wstaw elementy do listy rozwijanej
for i, (nazwa_wersji, klucz_produktu) in enumerate(zip(nazwy_wersji, klucze_produktu)):
    lista_rozwijana.insert(tk.END, f"{nazwa_wersji}: {klucz_produktu}")

def aktywuj_wybrany():
    # Pobierz indeks wybranego elementu
    indeks = lista_rozwijana.curselection()
    if indeks:
        indeks = int(indeks[0])
        nazwa_wersji, klucz_produktu = nazwy_wersji[indeks], klucze_produktu[indeks]
        klikniecie_przycisku(nazwa_wersji, klucz_produktu)

# Dodaj przycisk "Aktywuj"
przycisk_aktywacji = ttk.Button(okno, text="Aktywuj wybrany klucz", command=aktywuj_wybrany)
przycisk_aktywacji.pack(pady=10)

okno.mainloop()
