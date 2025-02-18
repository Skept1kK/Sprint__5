import pytest
from locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helper import create_random_email,create_random_password,create_random_username

@pytest.mark.usefixtures("get_driver")
class TestRegistration:

    # Регистрация аккаунта с заданными валидными данными
    def test_registration_new_account(self, get_driver):
        username=create_random_username()
        password=create_random_password()
        login=create_random_email()
        driver = get_driver
        driver.find_element(*locators.MAIN_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_BUTTON))
        driver.find_element(*locators.REG_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.USER_NAME_INPUT))
        driver.find_element(*locators.USER_NAME_INPUT).send_keys(username)
        driver.find_element(*locators.USER_EMAIL_INPUT).send_keys(login)
        driver.find_element(*locators.USER_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*locators.REG_BUTTON_SABMIT).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_BUTTON))
        assert driver.find_element(*locators.AUTH_PAGE_LOGIN_BUTTON).is_displayed()

        # Регистрация аккаунта c валидным количеством знаков в пароле
    @pytest.mark.parametrize('try_pass', ['325697', '3256978', '325697885854'])
    def test_registration_valid_password(self, get_driver, try_pass):
        username = create_random_username()
        login = create_random_email()
        driver = get_driver
        driver.find_element(*locators.MAIN_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_BUTTON))
        driver.find_element(*locators.REG_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.USER_NAME_INPUT))
        driver.find_element(*locators.USER_NAME_INPUT).send_keys(username)
        driver.find_element(*locators.USER_EMAIL_INPUT).send_keys(login)
        driver.find_element(*locators.USER_PASSWORD_INPUT).send_keys(try_pass)
        driver.find_element(*locators.REG_BUTTON_SABMIT).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_BUTTON))
        assert driver.find_element(*locators.AUTH_PAGE_LOGIN_BUTTON).is_displayed()

        # Регистрация аккаунта c невалидным количеством знаков в пароле
    @pytest.mark.parametrize('wrong_pass', ['52', '526', '1'])
    def test_registration_wrong_password(self, get_driver, wrong_pass):
        username = create_random_username()
        login = create_random_email()
        driver = get_driver
        driver.find_element(*locators.MAIN_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_BUTTON))
        driver.find_element(*locators.REG_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.USER_NAME_INPUT))
        driver.find_element(*locators.USER_NAME_INPUT).send_keys(username)
        driver.find_element(*locators.USER_EMAIL_INPUT).send_keys(login)
        driver.find_element(*locators.USER_PASSWORD_INPUT).send_keys(wrong_pass)
        driver.find_element(*locators.REG_BUTTON_SABMIT).click()
        assert driver.find_element(*locators.REG_PAGE_ERROR_MESSAGE).text == 'Некорректный пароль'