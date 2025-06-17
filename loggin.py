import customtkinter as ctk
from tkinter import messagebox
import playsound
from ventana2 import SessionWindow  # importamos la segunda ventana

# Tooltip mejorado
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

class Loggin:
    def validarUsuario(self, event=None):
        usuario = self.txtUsuario.get()
        if not usuario:
            self.txtUsuario.configure(fg_color="#ffffff", text_color="#22223b")
        elif usuario.islower() and len(usuario) >= 5:
            self.txtUsuario.configure(fg_color="#ffffff", text_color="#22223b")
        else:
            self.txtUsuario.configure(fg_color="#ffe5e5", text_color="#22223b")
            playsound.playsound(r'LOGIN\sounds\coin.mp3')
        self.verificarCampos()

    def validarPassword(self, event=None):
        password = self.txtPassword.get()
        if not password:
            self.txtPassword.configure(fg_color="#ffffff", text_color="#22223b")
        elif password.isdigit() and len(password) >= 5:
            self.txtPassword.configure(fg_color="#ffffff", text_color="#22223b")
        else:
            self.txtPassword.configure(fg_color="#ffe5e5", text_color="#22223b")
            playsound.playsound(r'LOGIN\sounds\coin.mp3')
        self.verificarCampos()

    def verificarCampos(self):
        usuario = self.txtUsuario.get()
        password = self.txtPassword.get()

        usuario_valido = usuario.islower() and len(usuario) >= 5
        password_valido = password.isdigit() and len(password) >= 5

        if usuario_valido and password_valido:
            if self.btnIngresar.cget("state") != "normal":
                self.btnIngresar.configure(state="normal", fg_color="#3a86ff", text_color="#fff")
        else:
            if self.btnIngresar.cget("state") != "disabled":
                self.btnIngresar.configure(state="disabled", fg_color="#e0e1dd", text_color="#b0b0b0")

    def mostrarAyuda(self, event=None):
        messagebox.showinfo("Ayuda", "Ingrese nombre de usuario y contraseña asignados.\nUsuario: letras minúsculas.\nContraseña: solo números.")

    def verCaracteres(self, event):
        self.txtPassword.configure(show='' if not self.bandera else '•')
        self.bandera = not self.bandera

    def abrirventana(self):
        self.ventana.withdraw()
        SessionWindow(self.ventana)

    def registrarUsuario(self):
        usuario = self.entryLoginUsuario.get()
        password = self.entryLoginPassword.get()
        # Aquí puedes conectar con tu base de datos o lógica de registro
        if not usuario or not password:
            messagebox.showerror("Error", "Por favor, ingrese usuario y contraseña.")
        else:
            # Aquí puedes validar y registrar el usuario
            messagebox.showinfo("Registro", f"Usuario {usuario} registrado (esto es solo un ejemplo).")
        def cerrar_todo(self):
            self.ventana.destroy()

    def __init__(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.ventana = ctk.CTk()
        self.ventana.resizable(0,0)
        self.ventana.title("Loggin")
        self.ventana.geometry("500x600")
        self.ventana.configure(fg_color="#f4f6fb")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_todo)

        self.bandera = False
        self.usuarios_registrados = {}

        # Frame centrado
        self.frame = ctk.CTkFrame(self.ventana, fg_color="#ffffff", corner_radius=16, width=420, height=520)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Título minimalista
        self.lblTitulo = ctk.CTkLabel(
            self.frame, 
            text="LUZ VERDE - LUZ ROJA", 
            font=("Segoe UI", 28, "bold"),
            text_color="#22223b",
            fg_color="#ffffff",
            width=400, height=60
        )
        self.lblTitulo.pack(pady=(30, 20))

        # Botón Ayuda minimalista
        self.btnAyuda = ctk.CTkButton(
            self.frame, text="?", width=40, height=40, 
            fg_color="#e0e1dd", text_color="#22223b", 
            hover_color="#bfc0c0", font=("Segoe UI", 18, "bold"),
            command=self.mostrarAyuda
        )
        self.btnAyuda.pack(pady=(0, 10))
        Tooltip(self.btnAyuda, "Ayuda")

        # Usuario
        self.lblUsuario = ctk.CTkLabel(
            self.frame, text="Usuario", font=("Segoe UI", 18, "bold"),
            text_color="#22223b", fg_color="#ffffff", width=200, height=35
        )
        self.lblUsuario.pack(pady=(10, 0))

        self.txtUsuario = ctk.CTkEntry(
            self.frame, placeholder_text="Ej: juanperez", width=260, height=40, font=("Segoe UI", 16),
            fg_color="#f4f6fb", border_width=2, border_color="#e0e1dd", text_color="#22223b"
        )
        self.txtUsuario.pack(pady=10)
        Tooltip(self.txtUsuario, "Solo letras minúsculas, min 5 caracteres.")
        self.txtUsuario.bind("<KeyRelease>", self.validarUsuario)

        # Contraseña
        self.lblPassword = ctk.CTkLabel(
            self.frame, text="Contraseña", font=("Segoe UI", 18, "bold"),
            text_color="#22223b", fg_color="#ffffff", width=200, height=35
        )
        self.lblPassword.pack(pady=(10, 0))

        self.txtPassword = ctk.CTkEntry(
            self.frame, placeholder_text="Solo números, min 5 caracteres.", show="•",
            width=260, height=40, font=("Segoe UI", 16),
            fg_color="#f4f6fb", border_width=2, border_color="#e0e1dd", text_color="#22223b"
        )
        self.txtPassword.pack(pady=10)
        Tooltip(self.txtPassword, "Solo números, min 5 caracteres.")
        self.txtPassword.bind("<KeyRelease>", self.validarPassword)

        # Botón Ver
        self.btnVer = ctk.CTkButton(
            self.frame, text="👁", width=35, height=35, fg_color="#e0e1dd", text_color="#22223b", hover_color="#bfc0c0"
        )
        self.btnVer.pack(pady=(0, 10))
        self.btnVer.bind("<Enter>", self.verCaracteres)
        self.btnVer.bind("<Leave>", self.verCaracteres)

        # Botón Registrarse
        self.btnIngresar = ctk.CTkButton(
            self.frame, text="Registrarse", font=("Segoe UI", 16, "bold"),
            state="disabled", fg_color="#e0e1dd", text_color="#b0b0b0", hover_color="#3a86ff", width=180, height=40,
            command=self.registrarUsuario
        )
        self.btnIngresar.pack(pady=10)
        Tooltip(self.btnIngresar, "Botón activo cuando usuario y contraseña sean válidos.")

        # Botón Iniciar Sesión
        self.btnIniciarSesion = ctk.CTkButton(
            self.frame, text="Iniciar Sesión", font=("Segoe UI", 16, "bold"),
            command=self.abrirventana, fg_color="#3a86ff", text_color="#fff", hover_color="#22223b", width=180, height=40
        )
        self.btnIniciarSesion.pack(pady=10)
        Tooltip(self.btnIniciarSesion, "Iniciar sesión con un usuario y contraseña ya registrados.")

        self.ventana.mainloop()