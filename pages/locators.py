from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')

    # SING_IN_MAIL = (By.ID, "id_login-username")
    # SING_IN_PASSWORD = (By.ID, "id_login-password")
    # SING_UP_MAIL = (By.ID, "id_registration-email")
    # SING_UP_PASSWORD = (By.ID, "id_registration-password1")
    # SING_UP_REPEAT_PASSWORD = (By.ID, "id_registration-password2")