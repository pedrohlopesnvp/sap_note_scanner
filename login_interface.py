import tkinter as tk
from tkinter import messagebox

# Global variables
email = None
passwd = None
id    = None
credentials_ok = False

def get_credentials(language):

    def on_submit():

        global email, passwd, id, credentials_ok

        email = entry_email.get()
        passwd = entry_passwd.get()
        id = entry_id.get()

        if not email or not passwd or not id:
            messagebox.showerror("Erro", language["all_fields_required"])
            return
        
        credentials_ok = True

        root.destroy()

    root = tk.Tk()
    root.title("SAP Note Scanner")
    
    window_weight = 350
    window_height = 300

    weight = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    pos_x = (weight // 2) - (window_weight // 2)
    pos_y = (height // 2) - (window_height // 2)

    root.geometry(f"{window_weight}x{window_height}+{pos_x}+{pos_y}")
    root.resizable(False, False)

    tk.Label(root, text=language["credentials"], font=("Arial", 12), pady=20).pack()

    tk.Label(root, text=language["email"], font=("Arial", 11)).pack()
    entry_email = tk.Entry(root, width=30, font=("Arial", 11))
    entry_email.pack(pady=5)

    tk.Label(root, text=language["passwd"], font=("Arial", 11)).pack()
    entry_passwd = tk.Entry(root, width=30, show="*", font=("Arial", 11))
    entry_passwd.pack(pady=5)

    tk.Label(root, text=language["id"], font=("Arial", 11)).pack()
    entry_id = tk.Entry(root, width=30, font=("Arial", 11))
    entry_id.pack(pady=5)

    btn_login = tk.Button(root, text="Login", bg="#041444", fg="white", font=("Arial", 12, "bold"), command=on_submit, cursor="hand2")
    btn_login.pack(pady=10)

    root.mainloop()

    return email, passwd, id, credentials_ok