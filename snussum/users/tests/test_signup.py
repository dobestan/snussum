from django.test import LiveServerTestCase

from selenium import webdriver


class SignUpTest(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        self.selenium.maximize_window()

    def test_signup(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/signup"))
