from connection_google import *

def get_info_notes(notes, language, notes_data, notes_read):
    try:
        for note in notes:
            if note in notes_read:
                # Jump to the next note
                continue

            # Mark the note as read (usando append em vez de add)
            if note not in notes_read:  # Evita duplicatas
                notes_read.append(note)

            url = f'https://me.sap.com/notes/{note}/{language["idiom"]}'

            driver.get(url)

            h2_element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

            title = f'{language["note"]}{h2_element.text}'

            note_info = {
                note: {
                    "title": h2_element.text,
                    "url": url,
                    "prerequisites": {}
                }
            }

            try:
                # Search for the prerequisites of the note
                rows = WebDriverWait(driver, 4).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr[data-sap-ui^="__item23-__table2-"]'))
                )
            except Exception as e:
                rows = []

            pre_notes = []

            if not rows:
                note_info[note]["prerequisites"][language["without_prerequisites"]] = {}
                notes_data.update(note_info)
                continue
            else:
                pre_notes = []
                for row in rows:
                    software_component = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2) span').text
                    from_version = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3) span').text
                    to_version = row.find_element(By.CSS_SELECTOR, 'td:nth-child(4) span').text
                    pre_note = row.find_element(By.CSS_SELECTOR, 'td:nth-child(5) span').text
                    title = row.find_element(By.CSS_SELECTOR, 'td:nth-child(6) span').text
                    component = row.find_element(By.CSS_SELECTOR, 'td:nth-child(7) span').text

                    note_info[note]["prerequisites"].setdefault(software_component, {})
                    note_info[note]["prerequisites"][software_component].setdefault(from_version, {})
                    note_info[note]["prerequisites"][software_component][from_version].setdefault(to_version, {})

                    note_info[note]["prerequisites"][software_component][from_version][to_version][pre_note] = {
                        "title": title,
                        "component": component
                    }

                    if pre_note not in pre_notes:
                        pre_notes.append(pre_note)

            notes_data.update(note_info)

            get_info_notes(pre_notes, language, notes_data, notes_read)

    except Exception as e:
        print(language["error_to_get_notes"] + str(e))
        return