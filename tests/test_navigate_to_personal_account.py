from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from locators import *

#Переход_в_личный_кабинет

class TestNavigatePersonalAccount:

    def test_navigate_to_personal_account(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/login")

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(login_header))

        login = "denissokolov1998@yandex.ru"
        password = "denis1998"

        driver.find_element(*email_input).send_keys(login)

        driver.find_element(*password_input).send_keys(password)

        driver.find_element(*login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(account_button))

        driver.find_element(*account_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(exit_button))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"