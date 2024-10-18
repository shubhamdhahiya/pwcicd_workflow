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

    def fetch_all_css_properties_js(self, element):
        """
        Fetch all CSS properties of the given element using JavaScript.
        :param element: Web element
        :return: Dictionary of all CSS properties and their values
        """
        # JavaScript to fetch all computed styles
        js_code = """
            var styles = window.getComputedStyle(arguments[0]);
            var result = {};
            for (var i = 0; i < styles.length; i++) {
                var prop = styles[i];
                result[prop] = styles.getPropertyValue(prop);
            }
            return result;
        """
        return element.parent.execute_script(js_code, element)

    async def fetch_css_properties_async(self, element):
        """
        Asynchronously fetch all CSS properties using a single JS call.
        :param element: Web element
        :return: Dictionary of all CSS properties
        """
        loop = asyncio.get_event_loop()
        executor = ThreadPoolExecutor()
        return await loop.run_in_executor(
            executor, self.fetch_all_css_properties_js, element
        )

    async def fetch_and_check_css_properties(
        self, css_selector, expected_css_properties, css_properties_list
    ):
        """
        Optimized with asyncio: Fetches all CSS properties from elements using the given CSS selector
        and checks them against expected values.
        :param css_selector: CSS selector to locate elements
        :param expected_css_properties: Set of expected CSS properties
        :param css_properties_list: List of CSS properties to fetch and compare
        :return: True if the fetched properties match the expected properties, False otherwise
        """
        wait = WebDriverWait(self.driver, 20)
        elements = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector))
        )

        try:
            fetched_css_properties = set()

            # Create a thread pool executor
            with ThreadPoolExecutor() as executor:
                # Schedule async tasks to fetch all CSS properties for each element
                tasks = [
                    self.fetch_css_properties_async(element) for element in elements
                ]

                # Wait for all tasks to complete and gather results
                results = await asyncio.gather(*tasks)

            # Filter the fetched properties based on the required CSS properties list
            for result in results:
                filtered_properties = {
                    result[prop] for prop in css_properties_list if prop in result
                }
                fetched_css_properties.update(filtered_properties)

                # Early exit if all expected properties are fetched
                if fetched_css_properties == expected_css_properties:
                    return True

            # Final comparison after fetching all properties
            return fetched_css_properties == expected_css_properties

        except (StaleElementReferenceException, NoSuchElementException) as e:
            print(f"Error occurred: {str(e)}")
            return False
