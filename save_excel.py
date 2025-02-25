import json
import pandas as pd

def save_excel():
    with open("notes_scanner.json", "r", encoding="utf-8") as file:
        notes_data = json.load(file)

    rows = []

    for note, info in notes_data.items():
        prerequisites = info["prerequisites"]
        first_row = True
        
        for pre_note, details in prerequisites.items():
            rows.append([
                note if first_row else "", 
                info["title"] if first_row else "", 
                info["url"] if first_row else "", 
                pre_note,  
                details.get("software_component", ""),
                details.get("from_version", ""),
                details.get("to_version", ""),
                details.get("title", ""),
                details.get("component", "")
            ])
            first_row = False

    df = pd.DataFrame(rows, columns=["Nota", "Título", "URL", "Pré-requisitos", "Componente de software","Versão de", "Versão para", "Título", "Componente"])

    # Criando um writer do Excel com XlsxWriter
    with pd.ExcelWriter("Notas_SAP.xlsx", engine="xlsxwriter") as writer:
        df.to_excel(writer, sheet_name="Notas SAP", index=False)

        # Obtendo a planilha para ajustes manuais
        worksheet = writer.sheets["Notas SAP"]
        for i, col in enumerate(df.columns):
            max_len = max(df[col].apply(len).max(), len(col)) + 2  # Pegando o tamanho máximo da coluna
            worksheet.set_column(i, i, max_len)  # Ajusta a largura da coluna automaticamente

    # df.to_excel("Notas_SAP.xlsx", index=False)