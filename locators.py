from selenium.webdriver.common.by import By

class locators:

# Форма регистрации
  REG_FORM = (By.XPATH, ".//form")  # Форма регистрации
  USER_NAME_INPUT = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")   # Поле ввода имени
  USER_EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")  # Поле ввода логина
  USER_PASSWORD_INPUT = (By.XPATH, ".//input[@type='password' and @name='Пароль']")  # Поле ввода пароля
  REG_BUTTON = (By.XPATH, '//a[text() = "Зарегистрироваться"]')  # Кнопка "Зарегистрироваться"
  REG_BUTTON_SABMIT = (By.XPATH, '//button[text() = "Зарегистрироваться"]')
  REG_PAGE_LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")  # Ссылка "Войти" на странице регистрации
  REG_PAGE_ERROR_MESSAGE = (By.XPATH, ".//p[contains(@class, 'input__error')]")
  # Главная страница
  MAIN_PAGE_BODY = (By.XPATH, ".//body")  # Раздел body на главной странице
  MAIN_PAGE_MAIN_SECTION = (By.XPATH, ".//body//main")  # Раздел main на главной странице
  # Кнопка "Войти в аккаунт"/"Оформить заказ" на Главной странице
  MAIN_PAGE_LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной странице
  MAIN_PAGE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ" на главной странице
  MAIN_PAGE_ANY_BUTTON = (By.XPATH, ".//body//main//button")  # Кнопка "Войти в аккаунт"/"Оформить заказ" на главной странице
  # Ссылка на Личный кабинет на Главной странице
  MAIN_PAGE_PROFILE_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']")  # Ссылка "Личный Кабинет" на главной странице
  # Личный кабинет
  PROFILE_PAGE_LOGO_LINK = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')  # Ссылка на Лого на странице Личный кабинет
  PROFILE_PAGE_CONSTRUCTOR_LINK = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")  # Ссылка на Конструктор на странице Личный кабинет
  PROFILE_PAGE_SAVE_BUTTON = (By.XPATH, ".//button[contains(text(), 'Сохранить')]")  # Кнопка "Сохранить" на странице Личный кабинет
  PROFILE_PAGE_EXIT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Выход')]")  # Кнопка "Выход" на странице Личный кабинет
  # Форма авторизации
  AUTH_PAGE_LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Войти" на странице авторизации
  AUTH_PAGE_LOGIN_FIELD = (By.XPATH, ".//input[@name='name']")  # Поле ввода логина
  AUTH_PAGE_PASSWORD_FIELD = (By.XPATH, ".//input[@name='Пароль']")  # Поле ввода пароля
  AUTH_FORM = (By.XPATH, ".//form")  # Форма ввода на странице авторизации
  # Форма восстановления пароля
  RECOVER_PAGE_BUTTON= (By.XPATH, '//a[text() = "Восстановить пароль"]')  # Кнопка "Восстановить" на странице восстановления пароля
  RECOVER_PAGE_LINK = (By.XPATH, ".//a[text()='Войти']")
  # Раздел Конструктор
  MAIN_PAGE_ROLLS_TAB = (By.XPATH, ".//span[text()='Булки']/parent::*")  # Вкладка Булки
  MAIN_PAGE_ROLLS_CLASS = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']")
  MAIN_PAGE_SOUCES_TAB = (By.XPATH, ".//span[text()='Соусы']/parent::*")  # Вкладка Соусы
  MAIN_PAGE_SOUCES_CLASS = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']")
  MAIN_PAGE_FILLINGS_TAB = (By.XPATH, ".//span[text()='Начинки']/parent::*")  # Вкладка Начинки
  MAIN_PAGE_FILLINGS_CLASS = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']")

