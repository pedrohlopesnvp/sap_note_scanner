import json
import os

def get_all_notes():
    notes_json = "notes.json"

    if os.path.exists(notes_json):
        with open(notes_json, "r", encoding="utf-8") as json_file:
            try:
                all_notes = json.load(json_file)
            except:
                all_notes = {}
        
        return all_notes

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
                        if system == "void":
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

    all_prereq_notes = set()
    different_notes = []

    def print_nested_notes(data):
        if isinstance(data, dict):
            for key in data:
                if str(key).isdigit() and len(str(key)) > 3:
                    all_prereq_notes.add(key)
                print_nested_notes(data[key])

    if filtered_notes_data:
        print_nested_notes(filtered_notes_data)

    if set(all_prereq_notes) != set(collected_notes):
        # The lists dont have the same notes
        missing = [note for note in all_prereq_notes if note not in collected_notes]
        extra = [note for note in collected_notes if note not in all_prereq_notes]
        
        different_notes = missing + extra
        
        if different_notes:
            # Different or missing notes found
            initial_notes[:] = different_notes
            notes_in_json = False

    return notes_in_json, filtered_notes_data, collected_notes