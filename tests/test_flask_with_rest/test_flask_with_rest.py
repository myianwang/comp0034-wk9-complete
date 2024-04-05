import json
import time

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_home_page_status_code():
    """
    GIVEN a live server
    WHEN a GET HTTP request to the home page is made
    THEN the HTTP response should have a status code of 200
    """
    url = f'http://127.0.0.1:5000/'
    response = requests.get(url)
    assert response.status_code == 200

