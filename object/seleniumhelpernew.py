# In a file named selenium_helper.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from concurrent.futures import ThreadPoolExecutor
from selenium.common.exceptions import TimeoutException
import inspect
import logging
import requests
import asyncio
import aiohttp
import time


class SeleniumHelper1:
    def __init__(self, driver):
        self.driver = driver
        self.executor = ThreadPoolExecutor()

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s :%(message)s"
        )
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def fetch_css_via_js(self, element, css_properties_list):
        """
        Use JavaScript Executor to fetch the computed CSS properties of the element.
        :param element: The WebElement to fetch CSS properties for.
        :param css_properties_list: List of CSS properties to fetch.
        :return: A dictionary of fetched CSS properties.
        """
        js_script = """
        let element = arguments[0];
        let properties = arguments[1];
        let computedStyles = window.getComputedStyle(element);
        let result = {};
        for (let property of properties) {
            result[property] = computedStyles.getPropertyValue(property);
        }
        return result;
        """
        return self.driver.execute_script(js_script, element, css_properties_list)

    async def fetch_css_properties_async(self, element, css_properties_list):
        """
        Asynchronously fetch CSS properties via JavaScript Executor by offloading to a thread pool.
        :param element: Web element
        :param css_properties_list: List of CSS properties to fetch
        :return: Fetched CSS properties as a dictionary
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            self.executor,
            self.fetch_css_via_js,
            element,
            css_properties_list,
        )

    async def fetch_and_check_css_properties(
        self, css_selector, expected_css_properties, css_properties_list
    ):
        """
        Optimized with asyncio: Fetches CSS properties from elements using the given CSS selector
        and checks them against expected values.
        :param css_selector: CSS selector to locate elements
        :param expected_css_properties: Set of expected CSS properties
        :param css_properties_list: List of CSS properties to fetch
        :return: True if the fetched properties match the expected properties, False otherwise
        """
        try:
            # Wait for all elements to be located
            wait = WebDriverWait(self.driver, 20)
            elements = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector))
            )

            if not elements:
                return False

            # To store fetched CSS properties
            for element in elements:
                fetched_css_properties = set()

                # Fetch properties asynchronously using JavaScript Executor
                fetched_props_dict = await self.fetch_css_properties_async(
                    element, css_properties_list
                )

                # Convert the fetched dictionary values into a set for comparison
                fetched_css_properties = set(fetched_props_dict.values())

                # Compare with the expected properties
                if fetched_css_properties != expected_css_properties:
                    return False

            # If all elements match the expected properties
            return True

        except (StaleElementReferenceException, NoSuchElementException) as e:
            print(f"Error occurred: {str(e)}")
            return False
