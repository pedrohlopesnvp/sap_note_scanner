import json
import pandas as pd
import numpy as np

def save_excel(root_notes, total_notes, notes_read, language):
    with open("notes_scanner.json", "r", encoding="utf-8") as file:
        notes_data = json.load(file)

    # Initial line with root_notes, total_notes e notes_read
    header_info = [
        (f"{language["root_notes"]}", f" {', '.join(map(str, root_notes))}"),
        (f"{language["total_notes"]}", f" {total_notes}"),
        (f"{language["notes_read"]}", f" {', '.join(map(str, notes_read))}")
    ]

    rows = []

    for note, info in notes_data.items():
        prerequisites = info["prerequisites"]

        if prerequisites == {'void': {}}:
            rows.append([
                note,  # Main note (first line only)
                info["title"],  # Main note title
                info["url"],  # Main Note URL
                "",  # Software component
                "",  # from_version
                "",  # to_version
                f"{language["without_prerequisites"]}",  # pre_note
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

    # Creating the DataFrame with the translated columns
    df = pd.DataFrame(rows, columns=[
        f"{language["exc_note"]}",
        f"{language["exc_title"]}",
        f"{language["exc_url"]}",
        f"{language["exc_sc"]}",
        f"{language["exc_fv"]}",
        f"{language["exc_tv"]}",
        f"{language["exc_pre_note"]}",
        f"{language["exc_pre_title"]}",
        f"{language["exc_comp"]}"
    ])

    # Creating Excel with XlsxWriter
    with pd.ExcelWriter("Notas_SAP.xlsx", engine="xlsxwriter") as writer:
        
        worksheet = writer.book.add_worksheet("Notas SAP")
        bold_format = writer.book.add_format({'bold': True})
        normal_format = writer.book.add_format() 

        for col, (title, value) in enumerate(header_info):
            worksheet.write_rich_string(0, col, 
                                        bold_format, title,
                                        normal_format, value)

        df.to_excel(writer, sheet_name="Notas SAP", startrow=2, index=False)

        # Adjust the size of the columns
        worksheet = writer.sheets["Notas SAP"]
        num_cols = len(df.columns)  # Número de colunas no DataFrame
        num_rows = len(df)  # Número de linhas no DataFrame
        worksheet.autofilter(2, 0, 2 + num_rows - 1, num_cols - 1)  # Linha 2 até o fim dos dados

        for i, col in enumerate(df.columns):
            # Calculates maximum column and title length separately
            content_lengths = df[col].astype(str).map(len)
            max_content_len = content_lengths.max() if not content_lengths.empty else 0  # Handles empty case

            try:
                if pd.isna(max_content_len):  # Handles NaN case
                    max_content_len = 0
            except:
                max_content_len = 0

            max_title_len = len(col)
            max_len = max(max_content_len, max_title_len) + 2 
            worksheet.set_column(i, i, max_len)