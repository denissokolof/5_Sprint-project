from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from locators import *

#Вход_в_личный_аккаунт

class TestAccountEnterPaths:

    #Вход через кнопку "Войти в аккаунт" на главной
    def test_login_main_page(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site")

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(constructor_heder))

        driver.find_element(*accaunt_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(login_header))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


    #Вход через кнопку "Личный кабинет"
    def test_login_personal_account(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/login")

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((login_header)))

        login = "denissokolov1998@yandex.ru"
        password = "denis1998"

        driver.find_element(*email_input).send_keys(login)

        driver.find_element(*password_input).send_keys(password)

        driver.find_element(*login_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(constructor_heder))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


    #Вход через кнопку в форме регистрации
    def test_login_registration_form(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/register")

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(placeholder_email))
        
        driver.find_element(*enter_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(login_header))
        
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


    #Вход через кнопку в форме восстановления пароля
    def test_login_password_recovercy(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(header_recover_password))

        driver.find_element(*enter_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(login_header))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"