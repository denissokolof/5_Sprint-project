from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from locators import *

#Регистрация
class TestRegistration:

    #Успешная_регистрация
    def test_successful_registrarion(self, random_email):

        driver = webdriver.Chrome()

        driver.get("https://stellarburgers.nomoreparties.site/register")

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(placeholder_email))

        name = "Denis"
        password = "123456"

        driver.find_element(*name_input).send_keys(name)

        driver.find_element(*email_input).send_keys(random_email)

        driver.find_element(*password_input).send_keys(password)
        
        driver.find_element(*registration_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(login_header))
        
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        
        driver.quit()
    
    #Ошибка_при_регистрации_с_паролем_меньше_шести_символов
    def test_registrarion_with_incorrect_password_less_six(self, random_email):

        driver = webdriver.Chrome()

        name = "Denis"
        password = "12345"

        driver.get("https://stellarburgers.nomoreparties.site/register")

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(placeholder_email))

        driver.find_element(*name_input).send_keys(name)

        driver.find_element(*email_input).send_keys(random_email)

        driver.find_element(*password_input).send_keys(password)
        
        driver.find_element(*registration_button).click()

        password_error = driver.find_element(*password_message).text

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/register" and password_error == "Некорректный пароль"

        driver.quit()
