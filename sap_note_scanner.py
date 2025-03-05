import os
from login_interface import *
from notes_interface import *
from info_interface import *
from select_language import *
from check_notes import *
from save_data import *
from save_excel import *
from connection_google import *
from login import *
from info_notes import *

#TODO Enfeitar excel (Filtros, cores, mais informações)

# Select language
language = select_language()

# Notes selection interface
initial_notes = get_notes(language)

retry          = False
notes_in_json  = False
login_ok       = True
scanner_ok     = True
credentials_ok = True

root_notes = initial_notes.copy()

notes_in_json, notes_data, notes_read = check_notes(initial_notes, notes_in_json)

if not notes_in_json:

    messagebox.showwarning(f"{language["warning"]}", language["scan_notes"]+f"{str(initial_notes)}")

    retry = True

    while retry:

        # Login Interface
        email, passwd, id, credentials_ok = get_credentials(language)

        if credentials_ok:

            try:

                messagebox.showinfo("Login", language["login"])
                driver = start_driver()
                driver.get('https://me.sap.com/home')
                
                try:
                    fazer_login(email, passwd, id, driver)
                    login_ok = True
                except Exception as e:
                    login_ok = False
                    messagebox.showwarning(f"{language["warning"]}", language["error_login"] + f"{str(e)}")
                    retry = messagebox.askyesno(f"{language["try_again"]}", f"{language["try_login_again"]}")
                    driver.quit()
                    if not retry:
                        break
                    continue

                try:
                    first_note = True
                    get_info_notes(initial_notes, language, notes_data, notes_read, driver, first_note)
                    scanner_ok = True
                except Exception as e:
                    scanner_ok = False
                    messagebox.showwarning(f"{language["warning"]}", language["error_reading"] + f"{str(e)}")
                    retry = messagebox.askyesno(f"{language["try_again"]}", f"{language["try_notes_again"]}")
                    driver.quit()
                    if not retry:
                        break
                    continue

                # If you got here, everything went well.
                retry = False

            finally:
                if not retry:
                    driver.quit()

if credentials_ok and not retry and login_ok and scanner_ok and root_notes != []:

    save_data(notes_data)

    total_notes = len(notes_read)

    save_excel(root_notes, total_notes, notes_read, language)

    # Interface to display notes
    display_info_notes(root_notes, total_notes, notes_read, language)