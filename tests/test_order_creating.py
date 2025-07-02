import allure
import pytest
from data.order_data import test_order
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrderCreating():
    @allure.title("Проверка позитивного сценария оформления заказа")
    @allure.description("Тестирование оформления заказа с двумя наборами тестовых данных, из двух точек входа")
    @pytest.mark.parametrize( "order_button, order_owner",
                                [(MainPageLocators.order_header_btn, test_order[0]),
                                 (MainPageLocators.order_faq_btn, test_order[1])]
    )

    def test_order_pozitive(self, driver, order_button, order_owner):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.cookie_ok()
        main_page.order_btn_click(order_button)
        order_page.wait_order_page()
        order_page.owner_data_input(order_owner)
        order_page.click_next()
        order_page.wait_about_rent_page()
        order_page.about_rent_data_input(order_owner)
        order_page.click_order()
        order_page.click_confirm()
        assert order_page.check_confirm_window()
