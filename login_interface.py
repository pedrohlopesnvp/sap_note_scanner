import tkinter as tk
from tkinter import messagebox

# Variáveis globais para armazenar as credenciais
email = None
senha = None
id    = None
credentials_ok = False

def get_credentials():

    def on_submit():

        global email, senha, id, credentials_ok

        email = entry_email.get()
        senha = entry_senha.get()
        id = entry_id.get()

        if not email or not senha or not id:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        credentials_ok = True

        root.destroy()  # Fecha a janela após inserir os dados

    # Criando a janela principal
    root = tk.Tk()
    root.title("SAP Note Scanner")
    
    # Definir tamanho da janela
    largura_janela = 350
    altura_janela = 300

    # Obter tamanho da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Calcular a posição para centralizar
    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)

    # Definir geometria da janela com posição centralizada
    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    # Labels e Campos de Entrada
    tk.Label(root, text="Digite as credenciais do seu login SAP", font=("Arial", 12), pady=20).pack()

    tk.Label(root, text="Digite o seu e-mail:", font=("Arial", 11)).pack()
    entry_email = tk.Entry(root, width=30, font=("Arial", 11))
    entry_email.pack(pady=5)

    tk.Label(root, text="Digite sua senha:", font=("Arial", 11)).pack()
    entry_senha = tk.Entry(root, width=30, show="*", font=("Arial", 11))
    entry_senha.pack(pady=5)

    tk.Label(root, text="Digite seu user ID:", font=("Arial", 11)).pack()
    entry_id = tk.Entry(root, width=30, font=("Arial", 11))
    entry_id.pack(pady=5)

    # Botão para enviar os dados
    btn_login = tk.Button(root, text="Login", bg="#041444", fg="white", font=("Arial", 12, "bold"), command=on_submit)
    btn_login.pack(pady=10)

    # Inicia a interface gráfica e espera até que seja fechada
    root.mainloop()

    return email, senha, id, credentials_ok