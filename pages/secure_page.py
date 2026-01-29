from pages.base_page import BasePage

class SecurePage(BasePage):
    def logout_btn(self):
        return self.find("a[href='/logout']")

    def header(self):
        return self.find("h2")
        
    def subheader(self):
        return self.find(".subheader")

    def click_logout(self):
        self.logout_btn().click()
