import json
import pandas as pd

def save_excel():
    with open("notes_scanner.json", "r", encoding="utf-8") as file:
        notes_data = json.load(file)

    rows = []

    for note, info in notes_data.items():
        prerequisites = info["prerequisites"]

        if prerequisites == {'Sem pré-requisitos': {}}:
            rows.append([
                note,  # Main note (first line only)
                info["title"],  # Main note title
                info["url"],  # Main Note URL
                "",  # Software component
                "",  # from_version
                "",  # to_version
                "Sem pré-requisitos",  # pre_note
                "",  # Prerequisite title
                ""  # Component
            ])
            
        else:

            first_row = True  # Controls the display of the note only on the first line

            for software_component, versions in prerequisites.items():
                for from_version, to_versions in versions.items():
                    for to_version, pre_notes in to_versions.items():
                        for pre_note, details in pre_notes.items():
                            rows.append([
                                note if first_row else "",  # Main note (first line only)
                                info["title"] if first_row else "",  # Main note title
                                info["url"] if first_row else "",  # Main Note URL
                                software_component,  # Software component
                                from_version,  # from_version
                                to_version,  # to_version
                                pre_note,  # pre_note
                                details.get("title", ""),  # Prerequisite title
                                details.get("component", "")  # Component
                            ])
                            first_row = False  # After the first line, leave the main note fields empty.

    df = pd.DataFrame(rows, columns=["Nota", "Título", "URL", "Componente de software","Versão de", "Versão para", "Nota pré-requisito", "Título", "Componente"])

    # Creating an Excel writer with XlsxWriter
    with pd.ExcelWriter("Notas_SAP.xlsx", engine="xlsxwriter") as writer:
        df.to_excel(writer, sheet_name="Notas SAP", index=False)

        worksheet = writer.sheets["Notas SAP"]
        for i, col in enumerate(df.columns):
            max_len = max(df[col].apply(len).max(), len(col)) + 2  # Getting the maximum column size
            worksheet.set_column(i, i, max_len)