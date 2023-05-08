import pytest
import config
from selenium import webdriver
from TestEnter.pages.enterFixture import EnterFixture
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from base import bd
from base.valueChoice import ValueChoice


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
def setup(request, get_webdriver, url, enter_fixture):
    driver = get_webdriver
    url = url
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield
    with bd.bd_write(config.sql_clear):
        print('SQL result: clearing')
    driver.delete_all_cookies()
    driver.quit()


# далее общие фикстуры
@pytest.fixture(scope='function')
def enter_fixture():
    return EnterFixture


@pytest.fixture(scope="function")
def value_choice_fixture():
    return ValueChoice
