import json
import os

def save_data(data):

    file_name_sap_notes = "notes.json"
    file_name_scanner = "notes_scanner.json"

    if os.path.exists(file_name_sap_notes):
        with open(file_name_sap_notes, "r", encoding="utf-8") as json_file:
            try:
                notes_data = json.load(json_file)
            except json.JSONDecodeError:
                notes_data = {}
    else:
        notes_data = {}

    notes_data.update(data)

    with open(file_name_sap_notes, "w", encoding="utf-8") as json_file:
        json.dump(notes_data, json_file, ensure_ascii=False, indent=4)

    with open(file_name_scanner, "w", encoding="utf-8") as json_file_scanner:
        json.dump(data, json_file_scanner, ensure_ascii=False, indent=4)