import tkinter as tk
from tkinter import messagebox, filedialog

notes = []

def get_notes(language):

    def on_submit():

        global notes

        text_notes = text_note.get("1.0", tk.END).strip()

        if not text_notes or text_notes == placeholder_text:
            messagebox.showerror("Erro", language["example"])
            return
        
        notes = text_notes.replace(" ", "").split(',')

        root.destroy()

    def on_focus_in(event):
        if text_note.get("1.0", tk.END).strip() == placeholder_text:
            text_note.delete("1.0", tk.END)
            text_note.config(fg="black")

    def on_focus_out(event):
        if text_note.get("1.0", tk.END).strip() == "":
            text_note.insert("1.0", placeholder_text)
            text_note.config(fg="gray")

    def select_path():

        global destination

        try:
            # Abrir caixa de diálogo para escolher o local e nome do arquivo
            destination = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                initialfile="note_scanner.txt",
                title="Salvar Arquivo"
            )

            if destination:  # Se o usuário escolheu um local
                messagebox.showinfo("Download", f"Arquivo salvo em:\n{destination}")
                return
            else:
                messagebox.showwarning("Cancelado", "Nenhum local foi selecionado.")

        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar o arquivo:\n{str(e)}")

    root = tk.Tk()
    root.title("SAP Note Scanner")

    window_weight = 350
    window_height = 280

    weight = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    pos_x = (weight // 2) - (window_weight // 2)
    pos_y = (height // 2) - (window_height // 2)

    root.geometry(f"{window_weight}x{window_height}+{pos_x}+{pos_y}")
    root.resizable(False, False)

    tk.Label(root, text=language["type"], font=("Arial", 12), pady=10).pack()

    placeholder_text = "3552901,3552902,3552903"
    text_note = tk.Text(root, height=5, width=40, font=("Arial", 11), fg="gray")
    text_note.insert("1.0", placeholder_text)

    text_note.bind("<FocusIn>", on_focus_in)
    text_note.bind("<FocusOut>", on_focus_out)

    text_note.pack(pady=5)

    btn_save = tk.Button(root, text="Escolher destino do Scanner", bg="#041444", fg="white", font=("Arial", 12, "bold"), cursor="hand2",
                         command=select_path)
    btn_save.pack(pady=10)

    btn_send = tk.Button(root, text=language["send"], bg="#041444", fg="white", font=("Arial", 12, "bold"), command=on_submit)
    btn_send.pack(pady=10)

    root.mainloop()

    return notes, destination