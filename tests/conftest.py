import pytest
from selenium import webdriver
from data.urls import Urls

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.main_page_url)
    yield driver
    driver.quit()