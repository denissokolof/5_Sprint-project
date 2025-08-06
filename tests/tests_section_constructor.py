from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from locators import *

class TestSectionConstructor:

    #Секция_булки
    def test_section_constructor_of_buns(self):

        driver = webdriver.Chrome()

        driver.get("https://stellarburgers.nomoreparties.site/login")

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(login_header))

        login = "denissokolov1998@yandex.ru"
        password = "denis1998"

        driver.find_element(*email_input).send_keys(login)

        driver.find_element(*password_input).send_keys(password)

        driver.find_element(*login_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(constructor_heder))

        active_button =  WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(active_tab))

        assert "Булки" in active_button.text

        driver.quit()





    #Секция_соусы
    def test_section_constructor_of_sauce(self):

        driver = webdriver.Chrome()

        driver.get("https://stellarburgers.nomoreparties.site/login")

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(login_header))

        login = "denissokolov1998@yandex.ru"
        password = "denis1998"

        driver.find_element(*email_input).send_keys(login)

        driver.find_element(*password_input).send_keys(password)

        driver.find_element(*login_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(constructor_heder))

        driver.find_element(*sauces_tab).click()

        active_button =  WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(active_tab))

        assert "Соусы" in active_button.text

        driver.quit()

        

    #Секция_начинки
    def test_section_constructor_of_filling(self):
        driver = webdriver.Chrome()

        driver.get("https://stellarburgers.nomoreparties.site/login")

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(login_header))

        login = "denissokolov1998@yandex.ru"
        password = "denis1998"

        driver.find_element(*email_input).send_keys(login)

        driver.find_element(*password_input).send_keys(password)

        driver.find_element(*login_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(constructor_heder))

        driver.find_element(*filling_tab).click()

        active_button =  WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(active_tab))

        assert "Начинки" in active_button.text

        driver.quit()