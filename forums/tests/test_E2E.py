"""Test E2E by using Selenium."""
from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_binary


class E2E(LiveServerTestCase):

    def setUp(self) -> None:
        """Create an instance browser."""
        self.browser = webdriver.Chrome()

    def test_access_to_ThaiMoung(self):
        """Test that a Chrome driver can get url of """
        url = 'https://thaimoung.herokuapp.com/forums/'
        self.browser.get(url)
        self.assertEqual(url, self.browser.current_url)

    def tearDown(self) -> None:
        self.browser.close()
