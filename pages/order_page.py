import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Переход к оформлению заказа')
    def go_to_order(self, order_btn):
        self.scroll_to_element(order_btn)
        self.wait_load_element(order_btn)
        self.click_on_element(order_btn)

    @allure.step('Ожидание загрузки страницы Для кого самокат')
    def wait_order_page(self):
        self.wait_load_element(OrderPageLocators.header_owner)

    @allure.step('Заполнить форму Для кого самокат')
    def owner_data_input(self, owner):
        self.key_to_input(OrderPageLocators.name_field, owner["first_name"])
        self.key_to_input(OrderPageLocators.last_name_field, owner["last_name"])
        self.key_to_input(OrderPageLocators.address_field, owner["address"])
        self.key_to_input(OrderPageLocators.metro_field, owner["metro"])
        self.click_on_element(OrderPageLocators.metro_dropdown)
        self.key_to_input(OrderPageLocators.phone_field, owner["phone"])

    @allure.step('Нажать кнопку Далее в окне Для кого самокат')
    def click_next(self):
        self.click_on_element(OrderPageLocators.next_btn)

    @allure.step('Ожидание загрузки страницы Про аренду')
    def wait_about_rent_page(self):
        self.wait_load_element(OrderPageLocators.about_rent)

    @allure.step('Заполнить форму Про аренду')
    def about_rent_data_input(self, owner):
        self.key_to_input(OrderPageLocators.when_field, owner["rent_date"])
        self.click_on_element(OrderPageLocators.about_rent)
        self.click_on_element(OrderPageLocators.rent_period_field)
        self.click_on_element(owner["rent_duration"])
        self.click_on_element(owner["scooter_color"])

    @allure.step('Нажать кнопку Заказать в окне Про аренду')
    def click_order(self):
        self.click_on_element(OrderPageLocators.order_btn)

    @allure.step('Нажать кнопку Да в окне Хотите оформить заказ')
    def click_confirm(self):
        self.click_on_element(OrderPageLocators.yes_btn)

    @allure.step('Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа')
    def check_confirm_window(self):
        return self.element_is_displaying(OrderPageLocators.order_accepted)