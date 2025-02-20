import tkinter as tk
from tkinter import messagebox

# Dict with translations for the application
translations = {
    "P": {
        "idiom": "P",
        "login": "Iniciando login...",
        "error_login": "Falha no login: ",
        "notes_analyzed": "Notas que serão analisadas:",
        "total_notes": "Total de notas a serem aplicadas: ",
        "notes_to_apply": "Notas a serem aplicadas: ",
        "create_folder": "Criando a pasta 'scanner'...",
        "all_fields_required": "Todos os campos são obrigatórios!",
        "credentials": "Digite as credenciais do seu login SAP",
        "email": "Digite o seu e-mail:",
        "passwd": "Digite a sua senha:",
        "id": "Digite o seu ID:",
        "note": "Nota: ",
        "pre_notes": "Pré-requisitos da nota:",
        "without_prerequisites": "Sem pré-requisitos",
        "error_to_get_notes": "Erro ao buscar informações das notes: ",
        "notes_to_apply": "Notas a serem aplicadas: ",
        "example": "Digite alguma(s) nota(s)! Exemplo: 3552901,3552902,3552903",
        "type": "Digite as notas que serão analisadas",
        "send": "Enviar",
        "scanner_result": "Resultado do Scanner:",
        "root_notes": "Notas Raiz:",
        "read_notes": "Notas lidas:",
        "save_file": "Salvar Arquivo",
        "cancel": "Cancelar",
        "file_saved": "Arquivo salvo em:",
        "no_file": "Nenhum arquivo foi selecionado.",
        "isnt_possible": "Não foi possível salvar o arquivo:",
        "select_destination": "Escolher destino do Scanner",
    },
    "E": {
        "idiom": "E",
        "login": "Starting login...",
        "error_login": "Login failed: ",
        "notes_analyzed": "Notes to be analyzed:",
        "total_notes": "Total notes to be applied: ",
        "notes_to_apply": "Notes to be applied: ",
        "create_folder": "Creating the 'scanner' folder...",
        "all_fields_required": "All fields are required",
        "credentials": "Enter your SAP login credentials",
        "email": "Enter your e-mail:",
        "passwd": "Enter your password:",
        "id": "Enter your ID:",
        "note": "Note: ",
        "pre_notes": "Prerequisites notes:",
        "without_prerequisites": "Without prerequisites",
        "error_to_get_notes": "Error to get notes information: ",
        "notes_to_apply": "Notes to be applied: ",
        "example": "Enter some note(s)! Example: 3552901,3552902,3552903",
        "type": "Enter the notes to be analyzed",
        "send": "Send",
        "scanner_result": "Scanner Result:",
        "root_notes": "Root Notes:",
        "read_notes": "Read Notes:",
        "save_file": "Save File",
        "cancel": "Cancel",
        "file_saved": "File saved in:",
        "no_file": "No file was selected.",
        "isnt_possible": "It wasn't possible to save the file:",
        "select_destination": "Select Scanner destination",
    },
}

# Interface to select the language
def select_language():
    root = tk.Tk()
    root.title("Select Language")

    largura_janela = 300
    altura_janela = 150

    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)

    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    root.resizable(False, False)

    lang_var = tk.StringVar(value="P")

    label = tk.Label(root, text="Choose the language:", font=("Arial", 11))
    label.pack(pady=10)

    radio_P = tk.Radiobutton(root, text="🇧🇷 Português", variable=lang_var, value="P", font=("Arial", 11), cursor="hand2")
    radio_P.pack()

    radio_E = tk.Radiobutton(root, text="🇺🇸 English", variable=lang_var, value="E", font=("Arial", 11), cursor="hand2")
    radio_E.pack()

    def confirm_language():
        root.selected_language = lang_var.get()
        root.destroy()

    btn_confirm = tk.Button(root, text="Confirm", bg="#041444", fg="white", font=("Arial", 12, "bold"), command=confirm_language)
    btn_confirm.pack(pady=10)

    root.selected_language = "P"  # Standard language
    root.mainloop()

    return translations[root.selected_language]