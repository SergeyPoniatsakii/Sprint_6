from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание загрузки главной страницы')
    def wait_main_page(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(MainPageLocators.page_scooter))

    @allure.step('Ожидание загрузки FAQ')
    def wait_faq(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(MainPageLocators.faq_section))

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ожидание загрузки элемента')
    def wait_load_element(self,locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def wait_click_element(self,locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Кликнуть по кнопке Заказать в хедере')
    def order_header_click(self):
        self.wait_load_element(MainPageLocators.order_header_btn)
        self.click_on_element(MainPageLocators.order_header_btn)

    @allure.step('Кликнуть по кнопке Заказать над блоком FAQ')
    def order_faq_click(self):
        self.scroll_to_element(MainPageLocators.order_faq_btn)
        self.wait_load_element(MainPageLocators.order_faq_btn)
        self.click_on_element(MainPageLocators.order_faq_btn)

    @allure.step('Ввод значения в поле')
    def key_to_input(self, locator, key):
        self.driver.find_element(*locator).send_keys(key)

    @allure.step('Получить текст элемента')
    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Получить url страницы')
    def get_page_url(self):
        return self.driver.current_url

    @allure.step('Проверить отображение элемента')
    def element_is_displaying(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Переключиться на другое окно')
    def switch_to(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != self.driver.current_window_handle:
                self.driver.switch_to.window(window)
                break