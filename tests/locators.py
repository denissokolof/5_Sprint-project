from selenium.webdriver.common.by import By

#Локаторы страницы логина

login_header = (By.XPATH, "//main/div/h2[text()='Вход']")  #Заголовок "Вход" на странице логина

email_input = (By.XPATH, "//div[label[contains(text(), 'Email')]]//input") #Поле для ввода "Email"

password_input = (By.XPATH, "//div[label[contains(text(), 'Пароль')]]//input") #Поле для ввода "Пароль"

login_button = (By.XPATH, "//form/button[text()='Войти']") #Кнопка "Войти" при входе в аккаунт

#Локаторы страницы регистрации

name_input = (By.XPATH, "//div[label[contains(text(), 'Имя')]]//input") #Поле для ввода "Имя"

registration_button = (By.XPATH, "//button[text()='Зарегистрироваться']") #Кнопка "Зарегистрироваться" при входе в аккаунт

password_message = (By.XPATH, "//div/p[@class='input__error text_type_main-default']") #Ошибка при некорректном пароле

placeholder_email = (By.XPATH, "//div[label[contains(text(), 'Email')]]") #Плейсхолдер Email

enter_button = (By.XPATH, "//div/p/a[text()='Войти']") #Кнопка "Войти" в аккаунт

#Локаторы главной страницы

constructor_heder = (By.XPATH, "//main/section/h1[text()='Соберите бургер']")  #Заголовок на главной странице

accaunt_button = (By.XPATH, "//div/button[text()='Войти в аккаунт']") #Кнопка "Войти в аккаунт" на главной странице

sauces_tab = (By.XPATH, "//div/span[text()='Соусы']") #Кнопка "Соусы"

filling_tab = (By.XPATH, "//div/span[text()='Начинки']") #Кнопка "Начинка"

account_button = (By.XPATH, "//nav/a/p[text()='Личный Кабинет']") #кнопка "Личный кабинет" в хедере

active_tab = (By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']//span") #Выбранный раздел булки-соусы-начинки

logo_link = (By.XPATH, "//nav/div[@class='AppHeader_header__logo__2D0X2']") #кнопка лого в хедере

constructor_link =(By.XPATH, "//li/a/p[text()='Конструктор']") #кнопка конструктор в хедере

#Локаторы личного кабинета

exit_button = (By.XPATH, "//ul/li/button[text()='Выход']") #кнопка "Выход" в личном кабинете

#Локаторы раздела "Восстановление пароля"

header_recover_password = (By.XPATH, "//div/h2[text()='Восстановление пароля']") #заголовок раздела "Восстановление пароля"
