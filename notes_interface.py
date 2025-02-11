import tkinter as tk
from tkinter import messagebox

notes = []

def get_notes():

    def on_submit():

        global notes

        notes_text = text_notes.get("1.0", tk.END).strip()

        if not notes_text or notes_text == placeholder_text:
            messagebox.showerror("Erro", "Digite alguma(s) nota(s)! Exemplo: 3552901,3552902,3552903")
            return
        
        notes = notes_text.replace(" ", "").split(',')

        root.destroy()  # Fecha a janela após inserir os dados

    def on_focus_in(event):
        if text_notes.get("1.0", tk.END).strip() == placeholder_text:
            text_notes.delete("1.0", tk.END)
            text_notes.config(fg="black")

    def on_focus_out(event):
        if text_notes.get("1.0", tk.END).strip() == "":
            text_notes.insert("1.0", placeholder_text)
            text_notes.config(fg="gray")

    # Criando a janela principal
    root = tk.Tk()
    root.title("SAP Note Scanner")
    
    # Definir tamanho da janela
    largura_janela = 350
    altura_janela = 200

    # Obter tamanho da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Calcular a posição para centralizar
    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)

    # Definir geometria da janela com posição centralizada
    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    # Label e Campo de Entrada
    tk.Label(root, text="Digite as notas que serão analisadas", font=("Arial", 12), pady=10).pack()

    placeholder_text = "3552901,3552902,3552903"
    text_notes = tk.Text(root, height=5, width=40, font=("Arial", 11), fg="gray")
    text_notes.insert("1.0", placeholder_text)

    text_notes.bind("<FocusIn>", on_focus_in)
    text_notes.bind("<FocusOut>", on_focus_out)

    text_notes.pack(pady=5)

    # Botão para enviar os dados
    btn_send = tk.Button(root, text="Enviar", bg="#041444", fg="white", font=("Arial", 12, "bold"), command=on_submit)
    btn_send.pack(pady=10)

    # Inicia a interface gráfica e espera até que seja fechada
    root.mainloop()

    return notes