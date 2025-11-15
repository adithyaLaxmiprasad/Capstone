import allure
from selenium_framework.pages.home_page import HomePage
from selenium_framework.pages.search_results_page import SearchResultsPage
from selenium_framework.pages.product_page import ProductPage
from selenium_framework.pages.cart_page import CartPage
from selenium_framework.pages.checkout_page import CheckoutPage
from selenium_framework.pages.order_confirmation_page import OrderConfirmationPage

@allure.title("Complete Checkout Flow")
def test_complete_checkout(setup):
    driver = setup

    home = HomePage(driver)
    results = SearchResultsPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    confirm = OrderConfirmationPage(driver)

    home.open_url("https://demo.nopcommerce.com/")
    home.search_product("Laptop")

    results.open_first_product()
    product.add_to_cart()

    cart.open_cart()
    checkout.begin_checkout()
    checkout.login_checkout()
    checkout.complete_checkout_steps()

    # NEW — Stop test as soon as Thank-You page loads
    assert confirm.wait_for_thankyou_page()
