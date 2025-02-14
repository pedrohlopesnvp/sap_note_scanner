import os
from login_interface import *
from notes_interface import *
from info_interface import *
from select_language import *

# Select language
language = select_language()

# Login Interface
email, passwd, id, credentials_ok = get_credentials(language)

if credentials_ok:

    # Notes selection interface
    initial_notes = get_notes(language)

    print(language["notes_analyzed"] + str(initial_notes))

    try:
        # Start the browser
        from connection_google import *
        from login import *
        from info_notes import *
        import info_notes

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

        with open('scanner/note_scanner.txt', 'w', encoding='utf-8') as file:

            get_info_notes(space, initial_notes, file, language)

            file.write('\n' + language["total_notes"] + str(info_notes.total_notes))

            file.write('\n' + language["notes_to_apply"] + str(info_notes.notes_read))

    finally:
        # Close the browser
        driver.quit()

        # Interface to display the notes
        display_info_notes(initial_notes, str(info_notes.total_notes), str(info_notes.notes_read), language)