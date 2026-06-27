from selenium.webdriver.common.by import By


class MainPageLocators:
    #Локаторы главной страницы и хедера (доступны на всех страницах сайта).

    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")  # Ссылка «Личный кабинет» в хедере
    LOGO_LINK = (By.CSS_SELECTOR, "div[class*='AppHeader_header__logo'] a")  # Лого Stellar Burgers в хедере
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/']")  # Ссылка «Конструктор» в хедере
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка «Оформить заказ» — успешный вход


class LoginPageLocators:
    #Локаторы страницы входа (/login).

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")  # Поле Email на странице входа
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")  # Поле Пароль на странице входа
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка «Войти» в форме входа
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка «Зарегистрироваться» на странице входа
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка «Восстановить пароль»


class RegisterPageLocators:
    #Локаторы страницы регистрации (/register).

    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле «Имя» на регистрации
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле Email на регистрации
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле Пароль на регистрации
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка «Зарегистрироваться»
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти» на странице регистрации
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class,'input__error')]")  # Текст ошибки валидации 


class ForgotPasswordPageLocators:
    #Локаторы страницы восстановления пароля (/forgot-password).

    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти» на странице восстановления пароля


class AccountPageLocators:
    #Локаторы личного кабинета (/account).

    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка «Выход» в личном кабинете


class ConstructorPageLocators: 
    #Локаторы страницы конструктора бургеров (/).

    TAB_BUNS = (By.XPATH, "//div[contains(@class,'tab_tab')]//span[text()='Булки']")  # Вкладка «Булки»
    TAB_SAUCES = (By.XPATH, "//div[contains(@class,'tab_tab')]//span[text()='Соусы']")  # Вкладка «Соусы»
    TAB_FILLINGS = (By.XPATH, "//div[contains(@class,'tab_tab')]//span[text()='Начинки']")  # Вкладка «Начинки»

    SECTION_BUNS_HEADER = (By.XPATH, "//h2[text()='Булки']")  # Заголовок секции «Булки»
    SECTION_SAUCES_HEADER = (By.XPATH, "//h2[text()='Соусы']")  # Заголовок секции «Соусы»
    SECTION_FILLINGS_HEADER = (By.XPATH, "//h2[text()='Начинки']")  # Заголовок секции «Начинки»