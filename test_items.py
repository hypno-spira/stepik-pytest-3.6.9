import pytest
from selenium import webdriver
import time


def test_find_card_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button_card = browser.find_element_by_css_selector(".btn-add-to-basket")

    assert button_card is not None, "button not found"
