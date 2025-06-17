import customtkinter as ctk
from tkinter import messagebox
import tkinter as tk

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.tipwindow or not self.text:
            return
        x = self.widget.winfo_rootx()
        y = self.widget.winfo_rooty() - 45
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(
            tw, text=self.text, justify='left',
            background="#22223b", foreground="#fff",
            relief="solid", borderwidth=1,
            font=("Segoe UI", 12), padx=12, pady=7
        )
        label.pack(ipadx=1)

    def hide_tip(self, event=None):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

class SessionWindow:
    def __init__(self, parent):
        self.parent = parent
        self.parent.withdraw() 

        self.parent.update_idletasks()
        x = self.parent.winfo_x()
        y = self.parent.winfo_y()
        width = self.parent.winfo_width()
        height = self.parent.winfo_height()

        self.ventana = ctk.CTkToplevel()
        self.ventana.title("Usuario Registrado")
        self.ventana.resizable(0, 0)
        self.ventana.geometry("500x600")
        self.ventana.configure(fg_color="#f4f6fb")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_todo)

        # Frame centrado
        self.frame = ctk.CTkFrame(self.ventana, fg_color="#ffffff", corner_radius=16, width=420, height=520)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Título
        self.lblTitulo = ctk.CTkLabel(
            self.frame, text="INICIO DE SESIÓN", font=("Segoe UI", 24, "bold"),
            text_color="#22223b", fg_color="#ffffff", width=320, height=50
        )
        self.lblTitulo.pack(pady=(30, 20))

        # Usuario
        self.entryLoginUsuario = ctk.CTkEntry(
            self.frame, placeholder_text="Usuario", width=260, height=40, font=("Segoe UI", 16),
            fg_color="#f4f6fb", border_width=2, border_color="#e0e1dd", text_color="#22223b"
        )
        self.entryLoginUsuario.pack(pady=10)
        Tooltip(self.entryLoginUsuario, "Ingrese su usuario registrado.")

        # Contraseña
        self.entryLoginPassword = ctk.CTkEntry(
            self.frame, placeholder_text="Contraseña", show="•", width=260, height=40, font=("Segoe UI", 16),
            fg_color="#f4f6fb", border_width=2, border_color="#e0e1dd", text_color="#22223b"
        )
        self.entryLoginPassword.pack(pady=10)
        Tooltip(self.entryLoginPassword, "Ingrese su contraseña registrada.")

        # Botón Entrar
        self.btnEntrar = ctk.CTkButton(
            self.frame, text="Entrar", font=("Segoe UI", 16, "bold"),
            fg_color="#3a86ff", text_color="#fff", hover_color="#22223b", width=180, height=40,
            command=self.iniciarSesion
        )
        self.btnEntrar.pack(pady=10)
        Tooltip(self.btnEntrar, "Entrar con usuario y contraseña.")

        # Botón Registrar
        self.btnRegistrar = ctk.CTkButton(
            self.frame, text="Registrar", font=("Segoe UI", 14, "bold"),
            fg_color="#3a86ff", text_color="#fff", hover_color="#22223b", width=180, height=36,
            command=self.registrarUsuario
        )
        self.btnRegistrar.pack(pady=(0, 10))
        Tooltip(self.btnRegistrar, "Registrar un nuevo usuario.")

        # Botón ¿Cómo jugar?
        self.btnComoJugar = ctk.CTkButton(
            self.frame, text="¿Cómo jugar?", font=("Segoe UI", 14, "bold"),
            fg_color="#e0e1dd", text_color="#22223b", hover_color="#bfc0c0", width=180, height=36,
            command=self.mostrarComoJugar
        )
        self.btnComoJugar.pack(pady=(0, 10))
        Tooltip(self.btnComoJugar, "Ver instrucciones del juego.")

        # Botón Ayuda
        self.btnAyuda = ctk.CTkButton(
            self.ventana, text="?", width=40, height=40, fg_color="#e0e1dd", text_color="#22223b",
            hover_color="#bfc0c0", font=("Segoe UI", 18, "bold"), command=self.mostrarAyuda
        )
        self.btnAyuda.place(x=420, y=30)
        Tooltip(self.btnAyuda, "Ayuda")

    def cerrar_todo(self):
        self.ventana.destroy()
        try:
            self.parent.destroy()
        except:
            pass

    def mostrarComoJugar(self):
        messagebox.showinfo(
            "¿Cómo jugar?",
            "Instrucciones básicas:\n\n"
            "- Usa las flechas del teclado para moverte.\n"
            "- Presiona la tecla UP para subir.\n"
            "- Presiona la tecla DOWN para bajar.\n"
            "- Presiona la tecla LEFT para retroceder.\n"
            "- Presiona la tecla RIGHT para avanzar.\n"
            "- Evita los obstáculos ÁRBOLES y las balas rojas.\n"
            "- Para ganar debes cruzar la meta en el tiempo establecido.\n"
        )

    def mostrarAyuda(self):
        messagebox.showinfo(
            "Ayuda",
            "Aquí puedes iniciar sesión.\n"
            "Ingresa tu usuario y contraseña.\n"
            "Si tienes dudas, consulta ¿Cómo jugar?"
        )

    def iniciarSesion(self):
        usuario = self.entryLoginUsuario.get()
        password = self.entryLoginPassword.get()
        # Aquí puedes integrar tu base de datos o lógica de autenticación
        if not usuario or not password:
            messagebox.showerror("Error", "Por favor, ingrese usuario y contraseña.")
        else:
            messagebox.showinfo("Sesión", f"Bienvenido, {usuario} (esto es solo un ejemplo).")
            self.ventana.destroy()
            try:
                self.parent.destroy()  # Cierra la ventana principal también
            except:
                pass
            # Aquí puedes abrir la ventana del juego

    def registrarUsuario(self):
        usuario = self.entryLoginUsuario.get()
        password = self.entryLoginPassword.get()
        # Aquí puedes conectar con tu base de datos o lógica de registro
        if not usuario or not password:
            messagebox.showerror("Error", "Por favor, ingrese usuario y contraseña.")
        else:
            # Aquí puedes validar y registrar el usuario
            messagebox.showinfo("Registro", f"Usuario {usuario} registrado (esto es solo un ejemplo).")