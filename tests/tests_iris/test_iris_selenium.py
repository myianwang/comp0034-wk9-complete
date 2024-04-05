import time

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_server_is_up_and_running(live_server_iris):
    """Check the app is running"""
    # Chrome_driver navigates to the page,
    # whereas requests.get makes an HTTP GET request and returns an HTTP response
    response = requests.get("http://127.0.0.1:5000")
    assert response.status_code == 200
