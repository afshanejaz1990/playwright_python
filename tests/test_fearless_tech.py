from pages.home_page import HomePage
from pages.people_page import PeoplePage
from pages.contact_page import ContactPage

def test_fearless_tech_navigation(setup_home_page, page):
    home_page = setup_home_page
    people_page = PeoplePage(page)

    home_page.open_navigation()

    # Verify the "People" link is present in the menu
    assert people_page.verify_people_link_in_menu(), "People link not found in navigation menu"

def test_fearless_contact_form(setup_home_page, page):
    home_page = setup_home_page
    contact_page = ContactPage(page)

    home_page.open_navigation()
    contact_page.navigate_from_menu()
    
    contact_page.fill_contact_form("john", "doe", "test@test.com", "test", "123456789", "test")
    contact_page.select_inquiry_type()
    contact_page.select_how_heard("Google Search")
    contact_page.agree_to_terms()