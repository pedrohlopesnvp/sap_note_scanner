from login_interface import *
from notes_interface import *
from info_interface import *

# Interface de login
email, senha, id, credentials_ok = get_credentials()

if credentials_ok:

    # Interface de seleção de notas
    notas_iniciais = get_notes()

    print("Notas que serão analisadas:" + str(notas_iniciais))

    try:
        # Inicia o navegador
        from connection_google import *
        from login import *
        from info_notes import *
        import info_notes

        messagebox.showinfo("Login", "Iniciando login...")

        driver.get('https://me.sap.com/home')  # Abre a página alvo
        
        # Tenta fazer o login com os dados inseridos
        try:
            fazer_login(email, senha, id)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha no login: {str(e)}")
            driver.quit()

        espaco = ""

        with open('coleta/todas_pre_notas_Testes.txt', 'w', encoding='utf-8') as arquivo:

            # Inicia coleta e exibição de informações
            get_info_notes(espaco, notas_iniciais, arquivo)

            arquivo.write('\nTotal de notas a serem aplicadas: ' + str(info_notes.total_notas))
            print('\nTotal de notas a serem aplicadas: ' + str(info_notes.total_notas))

            arquivo.write('\nNotas a serem aplicadas: ' + str(info_notes.notas_lidas))
            print('Notas a serem aplicadas: ' + str(info_notes.notas_lidas))

    finally:
        # Fecha o navegador ao finalizar
        driver.quit()

        #Exibe informações na interface gráfica
        display_info_notes(notas_iniciais, str(info_notes.total_notas), str(info_notes.notas_lidas))