import os
from login_interface import *
from notes_interface import *
from info_interface import *
from select_language import *
from check_notes import *
from save_data import *
from save_excel import *

#TODO Exibir mensagem das notas que precisarão ser lidas no site
#TODO Se der qualquer tipo de erro no login ou na leitura, exibir mensagem para tentar novamente
#TODO Enfeitar excel (Filtros, cores, mais informações)

# Select language
language = select_language()

# Notes selection interface
initial_notes, destination = get_notes(language)

notes_in_json = False

root_notes = initial_notes.copy()

notes_in_json, notes_data, notes_read = check_notes(initial_notes, notes_in_json)

if not notes_in_json:
    # Login Interface
    email, passwd, id, credentials_ok = get_credentials(language)

    if credentials_ok:

        try:
            # Start the browser
            from connection_google import *
            from login import *
            from info_notes import *

            messagebox.showinfo("Login", language["login"])

            driver.get('https://me.sap.com/home')
            
            try:
                fazer_login(email, passwd, id)
            except Exception as e:
                messagebox.showerror("Erro", language["error_login"]+f"{str(e)}")
                driver.quit()

            space = ""

            if not os.path.exists('scanner'):
                os.makedirs('scanner')

            get_info_notes(initial_notes, language, notes_data, notes_read)

        finally:
            # Close browser
            driver.quit()

save_data(notes_data)

save_excel()

total_notes = len(notes_read)

# Interface to display notes
display_info_notes(root_notes, total_notes, notes_read, language)