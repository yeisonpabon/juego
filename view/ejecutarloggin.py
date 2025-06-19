from view.loggin import Loggin
from view.ventana2 import SessionWindow

if __name__ == "__main__":
    import customtkinter as ctk
    root = ctk.CTk()
    root.withdraw()
    SessionWindow(root)
    root.mainloop()