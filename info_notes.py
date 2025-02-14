from connection_google import *

notes_read = set()
total_notes = 0

def get_info_notes(space, notes, file, language):

    global notes_read
    global total_notes

    try:
        
        for note in notes:
            if note in notes_read:
                # Jump to the next note
                continue

            # Mark the note as read
            notes_read.add(note)

            total_notes += 1
            url = f'https://me.sap.com/notes/{note}/{language["idiom"]}'

            driver.get(url)

            h2_element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

            title = f'{language["note"]}{h2_element.text}'
            file.write(space + title + '\n')

            file.write(space + url + '\n')

            prerequisites = f'{language["pre_notes"]}'
            file.write(space + prerequisites + '\n')

            space = space + " "

            try:
                # Search for the prerequisites of the note
                rows = WebDriverWait(driver, 3).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr[data-sap-ui^="__item23-__table2-"]'))
                )
            except Exception as e:
                rows = []

            pre_notes = []

            if not rows:
                file.write(space + language["without_prerequisites"] + '\n')
                continue
            else:
                pre_notes = []
                for row in rows:
                    note_prerequisites = row.find_element(By.CSS_SELECTOR, 'td:nth-child(5) span')
                    pre_note = note_prerequisites.text

                    if pre_note not in pre_notes:
                        pre_notes.append(pre_note)
                        file.write(space + ' - ' + pre_note + '\n')

            get_info_notes(space, pre_notes, file, language)

    except Exception as e:
        print(language["error_to_get_notes"] + str(e))
        return