from pages.main_page import MainPage

def test_landing_content(main_page: MainPage, base_url):
    main_page.open(base_url)
    
    assert main_page.title == "The Internet"
    assert main_page.fork_me_icon().is_visible()
    assert main_page.all_links().count() == 46
