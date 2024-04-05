import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_server_is_up_and_running(client, live_server):
    """
    GIVEN a live server
    WHEN a GET HTTP request to the home page is made
    THEN the HTTP response should have a bytes string "paralympics" in the data and a status code of 200

    Note: client is used rather than the chrome_driver as the chrome_driver navigates to a page,
    it does not return an HTTP response

    :param live_server: pytest-flask live server running the app as configured by the 'app' fixture in conftest.py
    :param client: pytest-flask test client
    """
    time.sleep(2)
    response = client.get('/')
    assert response.status_code == 200
    assert b"Paralympics" in response.data
