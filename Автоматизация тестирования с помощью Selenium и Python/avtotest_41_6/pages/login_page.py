from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, f"No login substring in the {current_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.should_be_login_url(*LoginPageLocators.LOGIN_FORM), "login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.should_be_login_url(*LoginPageLocators.REGISTER_FORM), "register form is not presented"