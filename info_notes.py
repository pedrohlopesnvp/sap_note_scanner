from connection_google import *

notes_read = set()
total_notes = 0
notes_data = {}

def get_info_notes(space, notes, file, language):

    global notes_read
    global total_notes
    global notes_data

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

            note_info = {
                note: {
                    "title": h2_element.text,
                    "url": url,
                    "prerequisites": {}
                }
            }

            file.write(space + title + '\n')

            file.write(space + url + '\n')

            prerequisites = f'{language["pre_notes"]}'
            file.write(space + prerequisites + '\n')

            space = space + " "

            print(note_info)

            try:
                # Search for the prerequisites of the note
                rows = WebDriverWait(driver, 4).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr[data-sap-ui^="__item23-__table2-"]'))
                )
            except Exception as e:
                rows = []

            pre_notes = []

            if not rows:
                file.write(space + language["without_prerequisites"] + '\n')
                note_info[note]["prerequisites"][language["without_prerequisites"]] = {}
                print(note_info)
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

                    print(f'{software_component} - {from_version} - {to_version} - {pre_note} - {title} - {component}')
                    
                    note_info[note]["prerequisites"][pre_note] = {
                        "software_component": software_component,
                        "from_version": from_version,
                        "to_version": to_version,
                        "title": title,
                        "component": component
                    }

                    if pre_note not in pre_notes:
                        pre_notes.append(pre_note)
                        file.write(space + ' - ' + pre_note + '\n')

            print(note_info)

            notes_data.update(note_info)

            get_info_notes(space, pre_notes, file, language)

    except Exception as e:
        print(language["error_to_get_notes"] + str(e))
        return