# from connection import *
from connection_google import *

def close_banner():
    # Espera o banner de consentimento desaparecer ou ser fechado
    try:
        consent_button = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.ID, 'truste-consent-button'))  # ID do botão de consentimento
        )
        consent_button.click()  # Clica para fechar o banner
    except:
        print("Nenhum banner de consentimento encontrado ou já fechado.")

def fazer_login(email, senha, id):

    # Aguarda até que o campo de nome de usuário esteja presente
    username_field = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.NAME, 'j_username'))
    )

    username_field.send_keys(email)  # Preenche o nome de usuário

    # Localiza e clica no botão de login
    login_button = driver.find_element(By.ID, 'logOnFormSubmit')
    login_button.click()

    close_banner()

    # Aguarda até que o campo senha esteja presenta
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'password')))

    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(senha)  # Preenche a senha

    # Localiza e clica no botão de login
    pass_button = driver.find_element(By.CLASS_NAME, 'uid-login-as__submit-button') 
    pass_button.click()

    close_banner()

    # Aguarda até que a div com id S esteja carregada
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, id)))

    # Localiza e clica no id ID S0026205828
    logar_s = driver.find_element(By.ID, id) 
    logar_s.click()

    close_banner()

    # Aguarda até que o título (H2) esteja aparecendo na tela (garante conteúdo carregado)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'sapUiBody')))