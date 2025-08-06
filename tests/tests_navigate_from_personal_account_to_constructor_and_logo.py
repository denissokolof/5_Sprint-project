from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from locators import *

#Переход_из_личного_кабинета_через_конструктор_и_логотип

class TestPersonalAccountNavigation:

    def test_navigate_from_personal_account_to_constructor(self):

        driver = webdriver.Chrome()

        driver.get("https://stellarburgers.nomoreparties.site/login")

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(login_header))

        login = "denissokolov1998@yandex.ru"
        password = "denis1998"

        driver.find_element(*email_input).send_keys(login)

        driver.find_element(*password_input).send_keys(password)

        driver.find_element(*login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(account_button))

        driver.find_element(*account_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(exit_button))

        driver.find_element(*constructor_link).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(constructor_heder))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        
        driver.quit()

    
    
    def test_navigate_from_personal_account_to_logo(self):

        driver = webdriver.Chrome()

        driver.get("https://stellarburgers.nomoreparties.site/login")

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(login_header))

        login = "denissokolov1998@yandex.ru"
        password = "denis1998"

        driver.find_element(*email_input).send_keys(login)

        driver.find_element(*password_input).send_keys(password)

        driver.find_element(*login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(account_button))

        driver.find_element(*account_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(exit_button))

        driver.find_element(*logo_link).click() 

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(constructor_heder))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        
        driver.quit()