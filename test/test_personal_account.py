import pytest
from locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import TestData

@pytest.mark.usefixtures("get_driver")
class TestLoginToPersonalAccount:
    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_of_personal_account(self, get_driver):
        driver = get_driver
        driver.find_element(*locators.MAIN_PAGE_PROFILE_LINK).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_BUTTON))
        driver.find_element(*locators.AUTH_PAGE_LOGIN_FIELD).send_keys(TestData.LOGIN_NAME)
        driver.find_element(*locators.USER_PASSWORD_INPUT).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*locators.AUTH_PAGE_LOGIN_BUTTON).click()
        driver.find_element(*locators.MAIN_PAGE_PROFILE_LINK).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.PROFILE_PAGE_EXIT_BUTTON))
        assert driver.find_element(*locators.PROFILE_PAGE_EXIT_BUTTON).is_displayed()

    # выход через кнопку выйти в Личный кабинете
    def test_logout_of_personal_account(self, get_driver):
        driver = get_driver
        driver.find_element(*locators.MAIN_PAGE_PROFILE_LINK).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_BUTTON))
        driver.find_element(*locators.AUTH_PAGE_LOGIN_FIELD).send_keys(TestData.LOGIN_NAME)
        driver.find_element(*locators.USER_PASSWORD_INPUT).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*locators.AUTH_PAGE_LOGIN_BUTTON).click()
        driver.find_element(*locators.MAIN_PAGE_PROFILE_LINK).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.PROFILE_PAGE_EXIT_BUTTON))
        driver.find_element(*locators.PROFILE_PAGE_EXIT_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.AUTH_PAGE_LOGIN_BUTTON))
        assert driver.find_element(*locators.AUTH_PAGE_LOGIN_BUTTON).is_displayed()

    # переход по клику на «Конструктор»
    def test_personal_account_to_constructor(self, get_driver):
        driver = get_driver
        driver.find_element(*locators.MAIN_PAGE_PROFILE_LINK).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_BUTTON))
        driver.find_element(*locators.AUTH_PAGE_LOGIN_FIELD).send_keys(TestData.LOGIN_NAME)
        driver.find_element(*locators.USER_PASSWORD_INPUT).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*locators.AUTH_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.PROFILE_PAGE_CONSTRUCTOR_LINK))
        driver.find_element(*locators.MAIN_PAGE_PROFILE_LINK).click()
        driver.find_element(*locators.PROFILE_PAGE_CONSTRUCTOR_LINK).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_ORDER_BUTTON))
        assert driver.find_element(*locators.MAIN_PAGE_ORDER_BUTTON).is_displayed()

     # переход по клику на логотип Stellar Burgers
    def test_personal_account_to_logo (self, get_driver):
        driver = get_driver
        driver.find_element(*locators.MAIN_PAGE_PROFILE_LINK).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_BUTTON))
        driver.find_element(*locators.AUTH_PAGE_LOGIN_FIELD).send_keys(TestData.LOGIN_NAME)
        driver.find_element(*locators.USER_PASSWORD_INPUT).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*locators.AUTH_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_PROFILE_LINK))
        driver.find_element(*locators.MAIN_PAGE_PROFILE_LINK).click()
        driver.find_element(*locators.PROFILE_PAGE_LOGO_LINK).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_ORDER_BUTTON))
        assert driver.find_element(*locators.MAIN_PAGE_ORDER_BUTTON).is_displayed()
