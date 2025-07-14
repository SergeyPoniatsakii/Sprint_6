from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Для кого самокат
    header_owner = (By.XPATH, "//div[text()='Для кого самокат']")
    # Имя
    name_field = (By.XPATH, "//input[@placeholder='* Имя']")
    # Фамилия
    last_name_field = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # Адрес
    address_field = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # Метро
    metro_field = (By.XPATH, "//input[@placeholder='* Станция метро']")
    # Элемент выпадающего списка метро
    metro_dropdown = (By.XPATH, "//li[@class='select-search__row']")
    # Телефон
    phone_field = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    # Кнопка Далее
    next_btn = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    # Про аренду
    about_rent = (By.XPATH, "//div[text()='Про аренду']")
    # Когда привезти
    when_field = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # Срок аренды
    rent_period_field = (By.XPATH, "//div[text()='* Срок аренды']")
    rent_period_one_day = (By.XPATH, "//div[@class='Dropdown-option' and text() = 'сутки']")
    rent_period_three_days = (By.XPATH, "//div[@class='Dropdown-option' and text() = 'трое суток']")
    # Цвет черный жемчуг
    black_cb = (By.XPATH, "//input[@id = 'black']")
    # Цвет серая безысходность
    gray_cb = (By.XPATH, "//input[@id = 'grey']")
    # Комментарий
    comment_field = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # Кнопка Заказать
    order_btn = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")
    # Кнопка Да /Хотите оформить заказ?
    yes_btn = (By.XPATH, "//button[text()='Да']")
    # Окно Заказ оформлен
    order_accepted = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    # Имя /Статус заказа
    name_status = (By.XPATH, "//div[text()='Имя']/../div[@class='Track_Value__15eEX']")
    # Фамилия /Статус заказа
    surname_status = (By.XPATH, "//div[text()='Фамилия']/../div[@class='Track_Value__15eEX']")
    # Адрес /Статус заказа
    address_status = (By.XPATH, "//div[text()='Адрес']/../div[@class='Track_Value__15eEX']")
    # Метро /Статус заказа
    metro_status = (By.XPATH, "//div[text()='Станция метро']/../div[@class='Track_Value__15eEX']")
    # Телефон /Статус заказа
    cell_status = (By.XPATH, "//div[text()='Телефон']/../div[@class='Track_Value__15eEX']")
    # Дата доставки /Статус заказа
    when_status = (By.XPATH, "//div[text()='Дата доставки']/../div[@class='Track_Value__15eEX']")
    # Срок аренды /Статус заказа
    period_status = (By.XPATH, "//div[text()='Срок аренды']/../div[@class='Track_Value__15eEX']")
    # Цвет /Статус заказа
    colour_status = (By.XPATH, "//div[text()='Цвет']/../div[@class='Track_Value__15eEX']")


