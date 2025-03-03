import json
import os

def check_notes(initial_notes, notes_in_json):
    notes_json = "notes.json"
    collected_notes = []  # List to collect notes in order
    
    if os.path.exists(notes_json):
        with open(notes_json, "r", encoding="utf-8") as json_file:
            try:
                notes_data = json.load(json_file)

                # Helper function to collect prerequisites recursively
                def get_prerequisites(note_id, data, collected_notes):
                    if note_id not in data:
                        return
                    
                    # Adds the current note to the list if it is not already present
                    if note_id not in collected_notes:
                        collected_notes.append(note_id)
                    
                    # Check prerequisites
                    prereqs = data[note_id].get("prerequisites", {})
                    for system in prereqs:
                        if system == "Sem pré-requisitos":
                            continue
                        for release in prereqs[system]:
                            for sp in prereqs[system][release]:
                                for prereq_id in prereqs[system][release][sp]:
                                    if prereq_id not in collected_notes:
                                        get_prerequisites(prereq_id, data, collected_notes)
                
                # Process the initial notes and check which ones are in the JSON
                missing_notes = []
                all_found = True    # Flag to check if all were found
                
                # First, process the notes from initial_notes
                for note in initial_notes:
                    if note in notes_data:
                        get_prerequisites(note, notes_data, collected_notes)
                    else:
                        missing_notes.append(note)
                        all_found = False
                
                # Update initial_notes with missing notes, if any
                if not all_found:
                    initial_notes[:] = missing_notes  # Modify the original list
                    notes_in_json = False
                else:
                    notes_in_json = True
                
                # Creates filtered_notes_data in the order of collected_notes
                filtered_notes_data = {}
                for note in collected_notes:
                    if note in notes_data:
                        filtered_notes_data[note] = notes_data[note]
                
            except json.JSONDecodeError:
                notes_data = {}
                filtered_notes_data = {}
                collected_notes = []
                notes_in_json = False
                initial_notes[:] = initial_notes  # Keep as is in case of error
    else:
        notes_data = {}
        filtered_notes_data = {}
        collected_notes = []
        notes_in_json = False
        initial_notes[:] = initial_notes  # Keep as is in case of error

    return notes_in_json, filtered_notes_data, collected_notes