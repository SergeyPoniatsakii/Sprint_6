from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка Все привыкли к куки
    ok_cookie_btn = (By.XPATH, "//button[@class='App_CookieButton__3cvqF']")
    # Кнопка заказать верхняя
    order_header_btn = (By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")
    # Кнопка заказать нижняя
    order_faq_btn = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']")
    # Логотип Самокат
    scooter_logo = (By.XPATH, "//img[@alt='Scooter']")
    # Логотип Яндекс
    yandex_logo = (By.XPATH, "//img[@alt='Yandex']")
    # Заголовок Самокат на пару дней
    page_scooter = (By.XPATH, "//div[@class='Home_Header__iJKdX']")
    # Секция FAQ
    faq_section = (By.XPATH, "//div[@class='Home_FAQ__3uVm4']")
    # Дзен лого
    page_dzen = (By.XPATH, "//a[@class='dzen-layout--desktop-base-header__logoLink-2h']")
    # Вопросы
    questions = list(map(lambda x: (By.ID, f'accordion__heading-{x}'), range(8)))
    # Ответы
    answers = list(map(lambda x: (By.ID, f'accordion__panel-{x}'), range(8)))
