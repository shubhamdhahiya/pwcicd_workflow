from utilities.base_class import BaseClass

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from object.seleniumhelper import SeleniumHelper
import requests
import time
import pytest

import asyncio


class Testone(BaseClass):
    @pytest.mark.run(order=5)
    @pytest.mark.dependency(depends=["test_HomePageFeatured"])
    def test_HomePageDoctorvoice(self):
        wait = WebDriverWait(self.driver, 20)
        name = self.driver.name

        log = self.getLogger()
        log.info(name)
        helper = SeleniumHelper(self.driver)

        window_size = self.driver.get_window_size()
        if window_size["width"] > 980:

            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()

            log.info("start")

            selectors_and_properties = [
                (
                    "#doctorVoicesection div#doctorVoiceFeatureblog",
                    {"3%", "55%", "1px solid #bfbfbf", "40px"},
                    ["margin-right", "width", "border-right", "padding-right"],
                ),
                (
                    ".post-categories",
                    {
                        "Elza",
                        "8px",
                        "700",
                        "rgba(1, 121, 217, 1)",
                        "5px",
                        "0px",
                        "600",
                        "uppercase",
                        "18px",
                        "17px",
                        "14px",
                    },
                    [
                        "margin-bottom",
                        "text-transform",
                        "color",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                    ],
                ),
                (
                    "#doctorVoicesection div#doctorVoiceFeatureblog .featuredDoctorpost article .post-media",
                    {"375px", "371.429px"},
                    ["height", "width"],
                ),
                (
                    "#doctorVoicesection div#doctorVioceblogsec article a img",
                    {"cover", "183px", "100%"},
                    ["object-fit", "height"],
                ),
                (
                    "#doctorVoicesection div#doctorVioceblogsec article .post-content h2.entry-title a",
                    {"none", "rgba(21, 44, 108, 1)", "30px", "600", "24px", "Elza"},
                    [
                        "text-transform",
                        "color",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                    ],
                ),
            ]

            for (
                css_selector,
                expected_css_properties,
                css_properties_list,
            ) in selectors_and_properties:
                result = asyncio.run(
                    helper.fetch_and_check_css_properties(
                        css_selector, expected_css_properties, css_properties_list
                    )
                )
            assert (
                result
            ), f"CSS properties do not match the expected values for selector {css_selector}"

            log.info("end")

            selectors = ["#doctorVoicesection a"]
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")

        elif window_size["width"] > 752 and window_size["width"] < 981:

            log.info("start")

            selectors_and_properties = [
                (
                    "#doctorVoicesection div#doctorVoiceFeatureblog",
                    {"0px none rgba(0, 0, 0, 0.5)", "0px", "753.412px"},
                    ["margin-right", "width", "border-right", "padding-right"],
                ),
                (
                    ".post-categories",
                    {
                        "700",
                        "14px",
                        "17px",
                        "rgba(1, 121, 217, 1)",
                        "18px",
                        "Elza",
                        "left",
                        "uppercase",
                        "0.35px",
                        "600",
                    },
                    [
                        "text-transform",
                        "text-align",
                        "letter-spacing",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                        "color",
                    ],
                ),
                (
                    "#doctorVoicesection div#doctorVioceblogsec article a img",
                    {"cover", "200px", "100%"},
                    ["object-fit", "height", "max-width"],
                ),
                (
                    "#doctorVoicesection div#doctorVioceblogsec article .post-content h2.entry-title a",
                    {"none", "rgba(21, 44, 108, 1)", "30px", "600", "24px", "Elza"},
                    [
                        "text-transform",
                        "color",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                    ],
                ),
            ]

            for (
                css_selector,
                expected_css_properties,
                css_properties_list,
            ) in selectors_and_properties:
                result = asyncio.run(
                    helper.fetch_and_check_css_properties(
                        css_selector, expected_css_properties, css_properties_list
                    )
                )
                assert (
                    result
                ), f"CSS properties do not match the expected values for selector {css_selector}"

                log.info("end")

            selectors = ["#doctorVoicesection a"]
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")

        elif window_size["width"] < 753:

            log.info("start")

            selectors_and_properties = [
                (
                    "#doctorVoicesection div#doctorVoiceFeatureblog",
                    {"412.19px", "0.761905px solid rgb(191, 191, 191)", "0px"},
                    ["margin-right", "width", "border-right", "padding-right"],
                ),
                (
                    ".post-categories",
                    {
                        "700",
                        "rgba(1, 121, 217, 1)",
                        "Elza",
                        "left",
                        "14px",
                        "18px",
                        "17px",
                        "600",
                        "uppercase",
                        "0.35px",
                    },
                    [
                        "text-transform",
                        "text-align",
                        "letter-spacing",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                        "color",
                    ],
                ),
                (
                    "#doctorVoicesection div#doctorVoiceFeatureblog .featuredDoctorpost article .post-media",
                    {"375px", "371.429px"},
                    ["height", "width"],
                ),
                (
                    "#doctorVoicesection div#doctorVioceblogsec article a img",
                    {
                        "cover",
                        "200px",
                    },
                    ["object-fit", "height"],
                ),
                (
                    "#doctorVoicesection div#doctorVioceblogsec article .post-content h2.entry-title a",
                    {"none", "rgba(21, 44, 108, 1)", "30px", "600", "24px", "Elza"},
                    [
                        "text-transform",
                        "color",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                    ],
                ),
            ]

            for (
                css_selector,
                expected_css_properties,
                css_properties_list,
            ) in selectors_and_properties:
                result = asyncio.run(
                    helper.fetch_and_check_css_properties(
                        css_selector, expected_css_properties, css_properties_list
                    )
                )
                assert (
                    result
                ), f"CSS properties do not match the expected values for selector {css_selector}"

                log.info("end")
            selectors = ["#doctorVoicesection a"]
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")

            # selectors = ["#doctorVoicesection a"]
            # additional_links = ["https://www.physiciansweekly.com/"]
            # expected_link_count = 8

            # log.info("Verifying links for multiple selectors")
            # helper.verify_links(selectors, additional_links, expected_link_count)
            # log.info("All links verified successfully")
