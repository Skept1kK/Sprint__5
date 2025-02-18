import pytest
from locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import TestData

@pytest.mark.usefixtures("get_driver")
class TestAuthorization:
    # Вход по кнопке «Войти в аккаунт» на главной
    def test_authorization_by_button_in_main_page(self,get_driver):
        driver = get_driver
        driver.find_element(*locators.MAIN_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_BUTTON))
        driver.find_element(*locators.AUTH_PAGE_LOGIN_FIELD).send_keys(TestData.LOGIN_NAME)
        driver.find_element(*locators.USER_PASSWORD_INPUT).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*locators.AUTH_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_ORDER_BUTTON))
        assert driver.find_element(*locators.MAIN_PAGE_ORDER_BUTTON).is_displayed()

    # Вход через кнопку «Личный кабинет»
    def test_authentication_by_profile(self, get_driver):
        driver = get_driver
        driver.find_element(*locators.MAIN_PAGE_PROFILE_LINK).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_BUTTON))
        driver.find_element(*locators.AUTH_PAGE_LOGIN_FIELD).send_keys(TestData.LOGIN_NAME)
        driver.find_element(*locators.USER_PASSWORD_INPUT).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*locators.AUTH_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_ORDER_BUTTON))
        assert driver.find_element(*locators.MAIN_PAGE_ORDER_BUTTON).is_displayed()

    # Вход через кнопку в форме регистрации
    def test_authentication_by_registration_form(self, get_driver):
        driver = get_driver
        driver.find_element(*locators.MAIN_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_BUTTON))
        driver.find_element(*locators.REG_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_PAGE_LOGIN_LINK))
        driver.find_element(*locators.REG_PAGE_LOGIN_LINK).click()
        driver.find_element(*locators.AUTH_PAGE_LOGIN_FIELD).send_keys(TestData.LOGIN_NAME)
        driver.find_element(*locators.USER_PASSWORD_INPUT).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*locators.AUTH_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_ORDER_BUTTON))
        assert driver.find_element(*locators.MAIN_PAGE_ORDER_BUTTON).is_displayed()

    # Вход через кнопку в форме восстановления пароля
    def test_authentication_by_button_forgot_password_in_auth_form_success(self, get_driver):
        driver = get_driver
        driver.find_element(*locators.MAIN_PAGE_PROFILE_LINK).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_BUTTON))
        driver.find_element(*locators.RECOVER_PAGE_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.RECOVER_PAGE_LINK))
        driver.find_element(*locators.RECOVER_PAGE_LINK).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_BUTTON))
        driver.find_element(*locators.AUTH_PAGE_LOGIN_FIELD).send_keys(TestData.LOGIN_NAME)
        driver.find_element(*locators.USER_PASSWORD_INPUT).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*locators.AUTH_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_ORDER_BUTTON))
        assert driver.find_element(*locators.MAIN_PAGE_ORDER_BUTTON).is_displayed()