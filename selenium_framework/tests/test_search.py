from selenium_framework.pages.search_page import SearchPage


def test_search_product(setup):
    driver = setup
    sp = SearchPage(driver)

    sp.open_url("https://demo.nopcommerce.com/")
    sp.search("Laptop")

    results = sp.results()
    assert len(results) > 0
