from loggin import Loggin
from ventana2 import SessionWindow

if __name__ == "__main__":
    import customtkinter as ctk
    root = ctk.CTk()
    root.withdraw()
    SessionWindow(root)
    root.mainloop()