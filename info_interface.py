import tkinter as tk
from tkinter import messagebox

def display_info_notes(initial_notes, total_notes, notes_read, language):

    root = tk.Tk()
    root.title("SAP Note Scanner")

    window_weight = 350
    window_height = 230

    weight = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    pos_x = (weight // 2) - (window_weight // 2)
    pos_y = (height // 2) - (window_height // 2)

    root.geometry(f"{window_weight}x{window_height}+{pos_x}+{pos_y}")

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

    # Config spacing tags
    text_widget.tag_configure("space", spacing1=5, spacing2=5, spacing3=5)
    
    text_widget.insert(tk.END, f"{language["scanner_result"]}\n", "space")
    text_widget.insert(tk.END, f"{language["root_notes"]} {initial_notes}\n", "space")
    text_widget.insert(tk.END, f"{language["total_notes"]} {total_notes}\n", "space")
    text_widget.insert(tk.END, f"{language["read_notes"]} {notes_read}", "space")

    text_widget.config(state="disabled", wrap="word", yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    text_widget.pack(pady=20)

    root.mainloop()