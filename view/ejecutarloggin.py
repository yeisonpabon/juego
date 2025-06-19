import customtkinter as ctk
from view.ventana2 import SessionWindow

def main():
    root = ctk.CTk()
    SessionWindow(root)
    root.mainloop()