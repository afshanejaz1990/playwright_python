class ContactPage:
    def __init__(self, page):
        self.page = page

    def navigate_from_menu(self):
        self.page.get_by_role("dialog").get_by_role("link", name="Contact: let's talk.").click()
        return self.verify_contact_page()

    def verify_contact_page(self):
        # Wait for navigation to complete and URL to change
        self.page.wait_for_url("https://fearless.tech/contact")
        return self.page.url == "https://fearless.tech/contact"

    def fill_contact_form(self, first_name, last_name, email, company, phone, message):
        form = self.page.frame_locator("iframe[title=\"Form 0\"]")
        form.get_by_label("First name").fill(first_name)
        form.get_by_label("Last name").fill(last_name)
        form.get_by_label("Email*").fill(email)
        form.get_by_label("Company name").fill(company)
        form.get_by_label("Phone number").fill(phone)
        form.get_by_label("Message*").fill(message)

    def select_inquiry_type(self, type="Other"):
        self.page.frame_locator("iframe[title=\"Form 0\"]").locator("li").filter(has_text=type).click()

    def select_how_heard(self, option):
        self.page.frame_locator("iframe[title=\"Form 0\"]").get_by_label("How did you hear about us?").select_option(option)

    def agree_to_terms(self):
        form = self.page.frame_locator("iframe[title=\"Form 0\"]")
        
        # Check if the terms agreement section is visible
        terms_text = form.get_by_text('By clicking "submit" below,')
        if terms_text.is_visible():
            terms_text.click()
            form.get_by_text("Send me info about").click()
            form.get_by_text("I want to receive occasional").click()
            return True
        else:
            return False