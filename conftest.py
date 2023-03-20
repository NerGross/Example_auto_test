import pytest
import config
from selenium import webdriver
from TestEnter.pom.enterFixture import EnterFixture
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from base import bd


@pytest.fixture
def get_chrome_options():
    options = ChromeOptions()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    # options.add_argument('--auto-open-devtools-for-tabs')
    options.add_argument('--ash-host-window-bounds=1920x1080')
    options.add_argument('--ignore-certificate-errors')  # игнорировать ошибку сертификата
    options.add_argument('--ignore-ssl-errors')  # игнорировать ошибку ssl
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    PATH = Service(r"C:\chromedriver.exe")
    driver = webdriver.Chrome(service=PATH, options=options)
    return driver


@pytest.fixture(params=config.urls)
def url(request):
    return request.param


@pytest.fixture(scope='function')
def enter_fixture():
    return EnterFixture


@pytest.fixture
def bd_read_fixture(sql):
    with bd.bd_read(sql) as bd1:
        print('SQL result: ', bd1)


@pytest.fixture(scope='function')
def setup(request, get_webdriver, url, enter_fixture, bd_read_fixture):
    driver = get_webdriver
    url = url
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield
    bd_read_fixture(config.sql_script)
    driver.delete_all_cookies()
    driver.quit()
