class HomePage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://fearless.tech/")

    def accept_consent(self):
        self.page.get_by_role("button", name=" Consent").click()

    def open_navigation(self):
        self.page.get_by_role("button", name="Toggle Navigation").click()