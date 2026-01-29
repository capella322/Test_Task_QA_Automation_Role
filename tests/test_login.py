from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

def test_auth_fail(main_page: MainPage, login_page: LoginPage, base_url):
    main_page.open(base_url)
    main_page.click_auth_link()
    
    login_page.login("wrong_user", "wrong_pass")
    assert "Your username is invalid!" in login_page.error_message()
    
    login_page.login("tomsmith", "wrong_pass")
    assert "is invalid!" in login_page.error_message()

def test_auth_success(login_page: LoginPage, secure_page: SecurePage, base_url):
    login_page.open(f"{base_url}/login")
    
    login_page.login("tomsmith", "SuperSecretPassword!")
    
    assert "secure" in login_page.page.url
    
    assert "Secure Area" in secure_page.header().inner_text()
    assert "Welcome to the Secure Area" in secure_page.subheader().inner_text()
    
    assert secure_page.logout_btn().is_visible()
    
    secure_page.click_logout()
    
    assert "login" in login_page.page.url
    assert "You logged out of the secure area!" in login_page.error_message()
