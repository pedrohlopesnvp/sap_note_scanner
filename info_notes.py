from connection_google import *

def check_barriers(driver, note):

    # Barrier 1: Check if it stopped at the home page
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, '__title27-inner'))
        )
        raise Exception("Erro: The site took a long time to load and stopped on the home page")
    except Exception as e:
        if "home page" in str(e):
            raise # Propagate the exception to the outer try

    # Barrier 2: Check if the note exists
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, '__title20-inner'))
        )
        raise Exception(f"Erro: Note {note} does not exist")
    except Exception as e:
        if "does not exist" in str(e):
            raise  # Propagate the exception to the outer try

def get_info_notes(notes, language, notes_data, notes_read, driver, first_note):
    try:
        for note in notes:
            if note in notes_read:
                continue
            else:
                notes_read.append(note)

            url = f'https://me.sap.com/notes/{note}/{language["idiom"]}'
            driver.get(url)

            if first_note:
                check_barriers(driver, note)
                first_note = False

            # Collecting note information
            try:
                h2_element = WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'h2'))
                )

                title = f'{language["note"]}{h2_element.text}'
                note_info = {
                    note: {
                        "title": h2_element.text,
                        "url": url,
                        "prerequisites": {}
                    }
                }

                try:
                    rows = WebDriverWait(driver, 4).until(
                        EC.presence_of_all_elements_located(
                            (By.CSS_SELECTOR, 'tr[data-sap-ui^="__item23-__table2-"]')
                        )
                    )
                except Exception:
                    rows = []

                if not rows:
                    note_info[note]["prerequisites"]["void"] = {}
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
                get_info_notes(pre_notes, language, notes_data, notes_read, driver, first_note)

            except Exception as e:
                print(f"{language["error_collect"]} {note}: {e}")
                continue

    except Exception as e:
        print(language["error_to_get_notes"] + str(e))
        raise  # Ensures that the exception is raised to the caller