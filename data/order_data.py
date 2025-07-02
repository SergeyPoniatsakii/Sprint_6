from datetime import datetime, timedelta
from locators.order_page_locators import OrderPageLocators

test_order = [
    {
        "first_name": "Анфиса",
        "last_name": "Козырева",
        "address": "Угрешская 23",
        "metro": "ду",
        "phone": "89019019011",
        "rent_date": (datetime.now() + timedelta(days=2)).strftime('%d.%m.%Y'),
        "rent_duration": OrderPageLocators.rent_period_one_day,
        "scooter_color": OrderPageLocators.black_cb
    },
    {
        "first_name": "Прохор",
        "last_name": "Громов",
        "address": "Енисейская 10, подъезд 7",
        "metro": "св",
        "phone": "+79039030033",
        "rent_date": (datetime.now() + timedelta(days=5)).strftime('%d.%m.%Y'),
        "rent_duration": OrderPageLocators.rent_period_three_days,
        "scooter_color": OrderPageLocators.gray_cb
    }
]