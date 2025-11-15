import allure
from selenium_framework.pages.home_page import HomePage
from selenium_framework.pages.search_results_page import SearchResultsPage
from selenium_framework.pages.product_page import ProductPage
from selenium_framework.pages.cart_page import CartPage


@allure.title("Verify Add to Cart Functionality")
@allure.description("Search for a product, open it, add to cart and verify cart count.")
@allure.feature("Shopping Cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_product_to_cart(setup):
    driver = setup

    with allure.step("Open Home Page"):
        home = HomePage(driver)
        home.open_url("https://demo.nopcommerce.com/")

    with allure.step("Search for a Laptop"):
        home.search_product("Laptop")

    with allure.step("Open First Product"):
        results = SearchResultsPage(driver)
        results.open_first_product()

    with allure.step("Add Product to Cart"):
        product = ProductPage(driver)
        product.add_to_cart()

    with allure.step("Open Cart and Verify Item Added"):
        cart = CartPage(driver)
        cart.open_cart()
        count = cart.cart_items_count()
        allure.attach(str(count), name="Cart Count", attachment_type=allure.attachment_type.TEXT)
        assert count > 0, "Cart is empty — product not added!"
