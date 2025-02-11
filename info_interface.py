import tkinter as tk
from tkinter import messagebox

def display_info_notes(notas_iniciais, total_notas, notas_lidas):

    # Criando a janela principal
    root = tk.Tk()
    root.title("SAP Note Scanner")
    
    # Definir tamanho da janela
    largura_janela = 350
    altura_janela = 230

    # Obter tamanho da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Calcular a posição para centralizar
    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)

    # Definir geometria da janela com posição centralizada
    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    root.configure(bg="white")

    text_widget = tk.Text(root, 
                          font=("Arial", 12), 
                          height=10, 
                          width=100, 
                          bg="white", 
                          fg="black", 
                          bd=0, 
                          highlightthickness=0,
                          padx=10, 
                          pady=5)
    
    scrollbar = tk.Scrollbar(root, command=text_widget.yview)

    # Configurar espaçamento entre linhas usando tag personalizada
    text_widget.tag_configure("space", spacing1=5, spacing2=5, spacing3=5)
    
    # Inserir os textos no Text
    text_widget.insert(tk.END, "Resultado do Scanner:\n", "space")
    text_widget.insert(tk.END, f"Notas Raiz: {notas_iniciais}\n", "space")
    text_widget.insert(tk.END, f"Total de notas a serem aplicadas: {total_notas}\n", "space")
    text_widget.insert(tk.END, f"Notas lidas: {notas_lidas}", "space")

    # Tornar o Text somente leitura
    text_widget.config(state="disabled", wrap="word", yscrollcommand=scrollbar.set)

    # Adicionar à janela
    scrollbar.pack(side="right", fill="y")
    text_widget.pack(pady=20)

    # Inicia a interface gráfica e espera até que seja fechada
    root.mainloop()