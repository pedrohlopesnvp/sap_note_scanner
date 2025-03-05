from connection_google import *

def close_banner(driver):
    try:
        consent_button = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.ID, 'truste-consent-button'))
        )
        consent_button.click()
    except:
        print("No consent banner found or already closed.")

def fazer_login(email, passwd, id, driver):

    # Wait until the username field is present
    username_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, 'j_username'))
    )

    username_field.send_keys(email)  # Set the email

    # Locate and click the login button
    login_button = driver.find_element(By.ID, 'logOnFormSubmit')
    login_button.click()

    close_banner(driver)

    # Wait until the password field is present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'password')))

    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(passwd)  # Set the password

    # Locate and click the login button
    pass_button = driver.find_element(By.CLASS_NAME, 'uid-login-as__submit-button') 
    pass_button.click()

    close_banner(driver)

    # Wait until the id field is present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, id)))

    # Locate and click the id button
    logar_s = driver.find_element(By.ID, id) 
    logar_s.click()

    close_banner(driver)
    
    # Wait until the page is loaded
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'sapUiBody')))