from locators.main_page_locators import MainPageLocators
import allure
from data.urls import Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step('Кликнуть Ок на сообщение об использовании куки')
    def cookie_ok(self):
        try:
            self.wait_load_element(MainPageLocators.ok_cookie_btn)
            self.click_on_element(MainPageLocators.ok_cookie_btn)
        except:
            pass
    @allure.step('Кликнуть по кнопке заказать')
    def order_btn_click(self, locator):
        if locator == MainPageLocators.order_header_btn:
            self.order_header_click()
        if locator == MainPageLocators.order_faq_btn:
            self.order_faq_click()

    @allure.step('Кликнуть на вопрос в блоке FAQ')
    def faq_click(self, question_num):
        self.wait_main_page()
        self.scroll_to_element(MainPageLocators.questions[question_num])
        self.wait_faq()
        self.wait_click_element(MainPageLocators.questions[question_num])
        self.click_on_element(MainPageLocators.questions[question_num])

    @allure.step('Получить значение Ответ в блоке FAQ')
    def faq_answer_get(self, answer_num):
        self.wait_load_element(MainPageLocators.answers[answer_num])
        return self.get_text_from_element(MainPageLocators.answers[answer_num])

    @allure.step('Кликнуть на логотип Самокат')
    def scooter_click(self):
        self.wait_load_element(MainPageLocators.scooter_logo)
        self.click_on_element(MainPageLocators.scooter_logo)

    @allure.step('Кликнуть на логотип Яндекс')
    def yandex_click(self):
        self.wait_load_element(MainPageLocators.yandex_logo)
        self.click_on_element(MainPageLocators.yandex_logo)

    @allure.step('Проверить url Дзен')
    def dzen_url_check(self):
        return Urls.dzen_page_irl in self.get_page_url()

    @allure.step('Проверить url Самокат')
    def scooter_url_check(self):
        return Urls.main_page_url == self.get_page_url()

    @allure.step('Проверить заголовок Самокат')
    def scooter_header_check(self):
        return self.element_is_displaying(MainPageLocators.page_scooter)

    @allure.step('Проверить логотип Дзен')
    def dzen_logo_check(self):
        return self.element_is_displaying(MainPageLocators.page_dzen)

    @allure.step('Ожидание загрузки логотип Дзен')
    def dzen_logo_wait(self):
        self.wait_load_element(MainPageLocators.page_dzen)
