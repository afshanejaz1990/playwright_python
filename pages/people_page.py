class PeoplePage:
    def __init__(self, page):
        self.page = page

    def verify_people_link_in_menu(self):
        menu = self.page.get_by_role("dialog")
        people_link = menu.get_by_role("link", name="People: our secret sauce.")
        return people_link.is_visible()