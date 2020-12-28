import pytest
import os
from selenium import webdriver
from pathlib import Path

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture()
def setup(request):
    # Before executing the testcase
    browser_name=request.config.getoption("browser_name")
    driversPath=Path.joinpath(Path(os.getcwd()).parent, "drivers")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=Path.joinpath(driversPath, "chromedriver.exe"))
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path=Path.joinpath(driversPath, "edgedriver.exe"))
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    
    # yield is used for splitting the commands that are
    # executed before and after the testcase execution
    yield
    
    #After executing the testcase
    driver.close()