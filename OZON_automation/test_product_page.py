import pytest
from .pages.product_page import TestProductPage

link = "https://www.ozon.ru/product/tabletki-dlya-" \
       "posudomoechnoy-mashiny-synergetic-55-sht-besfosfatnye-v-vodorastvorimoy-plenke-bez-540195799/?sh=Go7S4zmQJg"


@pytest.mark.product
def test_guest_can_see_order_price(browser):
    page = TestProductPage(browser, link)
    page.open()
    page.guest_can_see_order_price()
    page.order_price_equal_basket_price()


def test_guest_can_see_add_button(browser):
    page = TestProductPage(browser, link)
    page.open()
    page.guest_can_see_add_button()


def test_guest_can_see_goods_value_in_header(browser):
    page = TestProductPage(browser, link)
    page.open()
    page.guest_can_see_goods_value_in_header()


def test_guest_can_add_goods_to_basket(browser):
    page = TestProductPage(browser, link)
    page.open()
    page.guest_can_add_goods_to_basket()
