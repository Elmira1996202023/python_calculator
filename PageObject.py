from BaseApp import BasePage
from selenium.webdriver.common.by import By


class GoogleSearchLocators:

    LOCATOR_GOOGLE_SEARCH_FIELD = (By.XPATH, "//input[@title='Поиск']")
    LOCATOR_GOOGLE_SEARCH_BUTTON = (By.CLASS_NAME, "gNO89b")
    LOCATOR_GOOGLE_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_GOOGLE_NAVIGATION = (By.CSS_SELECTOR, "#cwos")
    LOCATOR_GOOGLE_NAVIGATION_BAR_SEARCH = (By.XPATH, "//*[@id='cwos']")
    LOCATOR_GOOGLE_NAVIGATION_BAR_ONE = (By.XPATH, "//div[@role='button'][normalize-space()='1']")
    LOCATOR_GOOGLE_NAVIGATION_BAR_SEARCH_MULTIPLY = (By.XPATH, "//div[@aria-label='умножение']")
    # LOCATOR_GOOGLE_NAVIGATION_BAR_MULTIPLY = (By.XPATH, "//div[@aria-label='умножение']")
    LOCATOR_GOOGLE_NAVIGATION_BAR_SEARCH_TWO = (By.XPATH, "//div[contains(text(),'2')]")
    # LOCATOR_GOOGLE_NAVIGATION_BAR_TWO = (By.XPATH, "//div[contains(text(),'2')]")
    LOCATOR_GOOGLE_NAVIGATION_BAR_SEARCH_MINUS = (By.XPATH, "//div[@aria-label='вычитание']")
    # LOCATOR_GOOGLE_NAVIGATION_BAR_MINUS = (By.XPATH, "//div[@aria-label='вычитание']")
    LOCATOR_GOOGLE_NAVIGATION_BAR_SEARCH_THREE = (By.XPATH, "//div[contains(text(),'3')]")
    # LOCATOR_GOOGLE_NAVIGATION_BAR_THREE = (By.XPATH, "//div[contains(text(),'3')]")
    LOCATOR_GOOGLE_NAVIGATION_BAR_SEARCH_PLUS = (By.XPATH, "//div[@aria-label='сложение']")
    # LOCATOR_GOOGLE_NAVIGATION_BAR_PLUS = (By.XPATH, "//div[@aria-label='сложение']")
    LOCATOR_GOOGLE_NAVIGATION_BAR_SEARCH_ONE_ONE = (By.XPATH, "//div[@role='button'][normalize-space()='1']")
    # LOCATOR_GOOGLE_NAVIGATION_BAR_ONE_ONE = (By.XPATH, "//div[@role='button'][normalize-space()='1']")
    LOCATOR_GOOGLE_NAVIGATION_BAR_SEARCH_EQUALLY = (By.XPATH, "//div[@aria-label='равно']")



class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field


    def click_on_the_search_button(self):
        return self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_SEARCH_BUTTON,time=5).click()


    def navigation_bar(self):
        return self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_NAVIGATION_BAR,time=5)


    def bar_search_close(self):
        return self.find_elements(GoogleSearchLocators.LOCATOR_GOOGLE_NAVIGATION,time=5)


    def bar_search_one(self, word):
        navigation_bar_search = self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_NAVIGATION_BAR_SEARCH)
        navigation_bar_search.click()
        navigation_bar_search.send_keys(word)
        return navigation_bar_search


    def bar_search_test_one(self):
        return self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_NAVIGATION_BAR_ONE,time=5).click()


    def bar_search_new_multiply(self):
        navigation_bar_search = self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_NAVIGATION_BAR_SEARCH_MULTIPLY)
        navigation_bar_search.click()
        navigation_bar_search.send_keys()
        return navigation_bar_search


    def bar_search_new_two(self):
        navigation_bar_search = self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_NAVIGATION_BAR_SEARCH_TWO)
        navigation_bar_search.click()
        navigation_bar_search.send_keys()
        return navigation_bar_search

    def bar_search_test_two(self):
        return self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_NAVIGATION_BAR_SEARCH_TWO,time=5).click()


    def bar_search_new_minus(self):
        navigation_bar_search = self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_NAVIGATION_BAR_SEARCH_MINUS)
        navigation_bar_search.click()
        navigation_bar_search.send_keys()
        return navigation_bar_search


    def bar_search_new_three(self):
        navigation_bar_search = self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_NAVIGATION_BAR_SEARCH_THREE)
        navigation_bar_search.click()
        navigation_bar_search.send_keys()
        return navigation_bar_search


    def bar_search_new_plus(self):
        navigation_bar_search = self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_NAVIGATION_BAR_SEARCH_PLUS)
        navigation_bar_search.click()
        navigation_bar_search.send_keys()
        return navigation_bar_search


    def bar_search_new_one_one(self):
        navigation_bar_search = self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_NAVIGATION_BAR_SEARCH_ONE_ONE)
        navigation_bar_search.click()
        navigation_bar_search.send_keys()
        return navigation_bar_search


    def bar_search_new_equally(self):
        navigation_bar_search = self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_NAVIGATION_BAR_SEARCH_EQUALLY)
        navigation_bar_search.click()
        navigation_bar_search.send_keys()
        return navigation_bar_search