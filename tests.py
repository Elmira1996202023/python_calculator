from PageObject import SearchHelper


def test_google_search(browser):
    google_main_page = SearchHelper(browser)
    google_main_page.go_to_site()
    google_main_page.enter_word("Калькулятор")
    google_main_page.click_on_the_search_button()
    google_main_page.bar_search_close()
    google_main_page.bar_search_test_one()
    google_main_page.bar_search_new_multiply()
    google_main_page.bar_search_new_two()
    google_main_page.bar_search_new_minus()
    google_main_page.bar_search_new_three()
    google_main_page.bar_search_new_plus()
    google_main_page.bar_search_new_one_one()
    google_main_page.bar_search_new_equally()

