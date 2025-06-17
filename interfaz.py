import customtkinter as ctk

ctk.set_appearance_mode("light")  # "dark" para modo oscuro
ctk.set_default_color_theme("blue")  # Puedes probar "green", "dark-blue", etc.

class ModernLogin(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login Moderno")
        self.geometry("420x500")
        self.resizable(False, False)
        self.configure(bg="#f7f9fa")

        # Logo circular con sombra
        self.logo_frame = ctk.CTkFrame(self, width=80, height=80, fg_color="#ffffff", corner_radius=40)
        self.logo_frame.place(relx=0.5, rely=0.18, anchor="center")
        self.logo_label = ctk.CTkLabel(self.logo_frame, text="🔒", font=("Segoe UI Emoji", 38))
        self.logo_label.place(relx=0.5, rely=0.5, anchor="center")

        # Título
        self.title_label = ctk.CTkLabel(self, text="Bienvenido", font=("Segoe UI", 26, "bold"), text_color="#22223b")
        self.title_label.place(relx=0.5, rely=0.32, anchor="center")

        # Usuario
        self.user_entry = ctk.CTkEntry(self, placeholder_text="Usuario", width=280, height=42, font=("Segoe UI", 14))
        self.user_entry.place(relx=0.5, rely=0.43, anchor="center")

        # Contraseña
        self.pass_entry = ctk.CTkEntry(self, placeholder_text="Contraseña", show="•", width=280, height=42, font=("Segoe UI", 14))
        self.pass_entry.place(relx=0.5, rely=0.52, anchor="center")

        # Botón de login
        self.login_btn = ctk.CTkButton(self, text="Iniciar sesión", width=220, height=40, font=("Segoe UI", 14, "bold"), corner_radius=20)
        self.login_btn.place(relx=0.5, rely=0.62, anchor="center")

        # Enlace de contraseña
        self.forgot_label = ctk.CTkLabel(self, text="¿Olvidaste tu contraseña?", font=("Segoe UI", 11), text_color="#5bc0be", cursor="hand2")
        self.forgot_label.place(relx=0.5, rely=0.70, anchor="center")

        # Pie de página
        self.footer = ctk.CTkLabel(self, text="© 2025 TuApp", font=("Segoe UI", 9), text_color="#adb5bd")
        self.footer.place(relx=0.5, rely=0.96, anchor="center")

if __name__ == "__main__":
    ModernLogin().mainloop()