import tkinter as tk
import subprocess

# Wpisz swoje dane
nazwy_wersji = [
    "Home_Core",
    "Home_Core(Country Specific)",
    "Home_Core(Single Language)",
    "Home_Core_N",
    "Professional",
    "Professional_N",
    "Professional_Enterprise",
    "Professional_Workstation",
    "Enterprise",
    "Enterprise_N",
    "Education",
    "Education_N",
    "Enterprise_2015_LTSB",
    "Enterprise 2015_LTSB N",
    "Enterprise_2016_LTSB",
    "Enterprise_2016_LTSB N",
    "Windows_10_Enterprise_N_Eval",
    "Windows_10_Enterprise_S_Eval",
    "Windows_10_Enterprise_S_N_Eval",
    "Windows_10_Enterprise_Eval",
    "Windows_10_Starter",
    "Windows_10_Education_N",
    "Windows_10_Education",
    "Windows_10_Professional",
    "Windows_10_Professional_N",
    "Windows_10_Core",
    "Windows_10_Core_N",
    "Core_Single_Language",
    "Core_Country_Specific",
    "Windows_10_Home",
    "Windows_10_Home_N",
    "Windows_10_Pro",
    "Windows_10_Pro_N",
    "Windows_10_Pro_for_Workstations",
    "Windows_10_Pro_N_for_Workstations",
    "Windows_10_S",
    "Windows_10_Education",
    "Windows_10_Education_N",
    "Windows_10_Pro_Education",
    "Windows_10_Pro_Education_N",
    "Windows_10_Enterprise",
    "Windows_10_Enterprise_S",
    "Windows_10_Enterprise_N",
    "Windows_10_Enterprise_G_N",
    "Windows_10_Enterprise_N_LTSB_2016",
    
]

klucze_produktu = [
    "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99",
    "PVMJN-6DFY6-9CCP6-7BKTT-D3WVR",
    "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH",
    "3KHY7-WNT83-DGQKR-F7HPR-844BM",
    "W269N-WFGWX-YVC9B-4J6C9-T83GX",
    "MH37W-N47XK-V7XM9-C7227-GCQG9",
    "NPPR9-FWDCX-D2C8J-H872K-2YT43",
    "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4",
    "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2",
    "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ",
    "WNMTR-4C88C-JK8YV-HQ7T2-76DF9",
    "2F77B-TNFGY-69QQF-B8YKP-D69TJ",
    "DCPHK-NFMTC-H88MJ-PFHPY-QJ4BJ",
    "QFFDN-GRT3P-VKWWX-X7T3R-8B639",
    "MNXKQ-WY2CT-JWBJ2-T68TQ-YBH2V",
    "7TNX7-H36JG-QFF42-K4JYV-YY482",
    "D3M8K-4YN49-89KYG-4F3DR-TVJW3",
    "VPMWD-PVNRR-79WJ9-VVJQC-3YH2G",
    "D6RD9-D4N8T-RT9QX-YW6YT-FCWWJ",
    "84NGF-MHBT6-FXBX8-QWJK7-DRR8H",
    "YNMGQ-8RYV3-4PGQ3-C8XTP-7CFBY",
    "VK7JG-NPHTM-C97JM-9MPGT-3V66T",
    "2B87N-8KFHP-DKV6R-Y2C8J-PKCKT",
    "YTMG3-N6DKC-DKB77-7M9GH-8HVX7",
    "4CPRK-NM3K3-X6XXQ-RXX86-WXCHW",
    "BT79Q-G7N6G-PGBYW-4YWX6-6F4BT",
    "N2434-X9D7W-8PF6X-8DV9T-8TYMD",
    "YTMG3-N6DKC-DKB77-7M9GH-8HVX7",
    "4CPRK-NM3K3-X6XXQ-RXX86-WXCHW",
    "VK7JG-NPHTM-C97JM-9MPGT-3V66T",
    "2B87N-8KFHP-DKV6R-Y2C8J-PKCKT",
    "DXG7C-N36C4-C4HTG-X4T3X-2YV77",
    "WYPNQ-8C467-V2W6J-TX4WX-WT2RQ",
    "3NF4D-GF9GY-63VKH-QRC3V-7QW8P",
    "YNMGQ-8RYV3-4PGQ3-C8XTP-7CFBY",
    "84NGF-MHBT6-FXBX8-QWJK7-DRR8H",
    "8PTT6-RNW4C-6V7J2-C2D3X-MHBPB",
    "GJTYN-HDMQY-FRR76-HVGC7-QPF8P",
    "XGVPP-NMH47-7TTHJ-W3FW7-8HV2C",
    "NK96Y-D9CD8-W44CQ-R8YTK-DYJWX",
    "WGGHN-J84D6-QYCPR-T7PJ7-X766F",
    "FW7NV-4T673-HF4VX-9X4MM-B4H4T",
    "RW7WN-FMT44-KRGBK-G44WK-QV7YK",
]


def klikniecie_przycisku(nazwa_wersji, klucz_produktu):
    # Uruchom CMD i wpisz komendę
    subprocess.run(["cmd", "/c", f"slmgr.vbs /ipk {klucz_produktu}"])

okno = tk.Tk()
okno.title("Informacje o wersji i kluczu Windows")

# Utwórz tabelę
tabela = tk.Frame(okno)
tabela.pack(padx=10, pady=10)

for i, (nazwa_wersji, klucz_produktu) in enumerate(zip(nazwy_wersji, klucze_produktu)):
    etykieta_wersji = tk.Label(tabela, text=nazwa_wersji, width=30)
    etykieta_wersji.grid(row=i, column=0)

    etykieta_klucza = tk.Label(tabela, text=klucz_produktu, width=30)
    etykieta_klucza.grid(row=i, column=1)

    przycisk = tk.Button(tabela, text="Aktywuj", command=lambda vn=nazwa_wersji, pk=klucz_produktu: klikniecie_przycisku(vn, pk))
    przycisk.grid(row=i, column=2)

okno.mainloop()
