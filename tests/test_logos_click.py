import allure
from pages.main_page import MainPage

class TestLogosClick():
    @allure.title("Проверка переходов по клику на логотипы")
    @allure.description("Тестирование перехода на главную страницу Самокат по клику на логотип Самоката")
    def test_scooter_logo_click(selfs, driver):
        main_page = MainPage(driver)
        main_page.cookie_ok()
        main_page.order_header_click()
        main_page.scooter_click()
        assert main_page.scooter_url_check() and main_page.scooter_header_check()
    @allure.title("Проверка переходов по клику на логотипы")
    @allure.description("Тестирование перехода на главную страниц Дзена по клику на логотип Яндекс.")
    def test_yandex_logo_click(selfs, driver):
        main_page = MainPage(driver)
        main_page.cookie_ok()
        main_page.order_header_click()
        main_page.yandex_click()
        main_page.switch_to()
        main_page.dzen_logo_wait()
        assert main_page.dzen_url_check() and main_page.dzen_logo_check()

