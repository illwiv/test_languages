from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

class TestCart():
    def test_check_add_to_cart_button(self, browser):
        browser.get(link)
        WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#add_to_basket_form .btn.btn-lg.btn-primary.btn-add-to-basket"))
    )