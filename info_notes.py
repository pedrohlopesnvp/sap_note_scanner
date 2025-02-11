# from connection import *
from connection_google import *

# Conjunto para armazenar notas já lidas
notas_lidas = set()
total_notas = 0

def get_info_notes(espaco, notas, arquivo):

    global notas_lidas
    global total_notas

    try:
        
        for nota in notas:
            print("Notas lidas:  " + str(notas_lidas))
            if nota in notas_lidas:
                print(f"Nota {nota} já foi lida. Pulando...")
                continue

            # Marcar a nota como lida
            notas_lidas.add(nota)

            print("Lendo nota " + nota)
            total_notas += 1
            url = f'https://me.sap.com/notes/{nota}/P'

            driver.get(url)

            h2_element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

            titulo = f'Nota: {h2_element.text}'
            arquivo.write(espaco + titulo + '\n')

            arquivo.write(espaco + url + '\n')

            prerequisites = f'Prerequisites notes:'
            arquivo.write(espaco + prerequisites + '\n')

            espaco = espaco + " "

            try:
                # Busca o tr referente aos prerequisites
                rows = WebDriverWait(driver, 3).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr[data-sap-ui^="__item23-__table2-"]'))
                )
            except Exception as e:
                rows = []

            pre_notes = []

            if not rows:
                print("Não temos prerequisitos da nota " + nota)
                arquivo.write(espaco + 'Sem pre-requisitos' + '\n')
                continue
            else:
                print("Tem prerequisitos da nota " + nota)
                pre_notes = []
                for row in rows:
                    note_prerequisites = row.find_element(By.CSS_SELECTOR, 'td:nth-child(5) span')
                    pre_note = note_prerequisites.text

                    if pre_note not in pre_notes:
                        pre_notes.append(pre_note)
                        arquivo.write(espaco + ' - ' + pre_note + '\n')

            print(pre_notes)

            get_info_notes(espaco, pre_notes, arquivo)

    except Exception as e:
        print("Erro ao buscar informações das notas: " + str(e))
        return