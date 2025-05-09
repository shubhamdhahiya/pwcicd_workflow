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
    @pytest.mark.run(order=6)
    @pytest.mark.dependency(depends=["test_HomePageDoctorvoice"])
    def test_HomePagespotlightandpeer(self):
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
                    "#home-condition-section #conditionSpotlightsection #conditionSpotlighleftsec",
                    {"32px", "640px", "1px solid rgb(191, 191, 191)"},
                    ["margin-right", "width", "border-right"],
                ),
                (
                    "#conditionSpotlightsection div#conditionSpotlightrightsec div#lightfeaturedsec img",
                    {"604.797px"},
                    ["width"],
                ),
                (
                    "#conditionSpotlightsection div#conditionSpotlighleftsec .conditionSpotlightblogsec .et_pb_blurb_container h4 a",
                    {"30px", "600", "24px", "Elza"},
                    ["line-height", "font-weight", "font-size", "font-family"],
                ),
                (
                    "#lightfeaturedsec h3",
                    {"10px", "rgba(21, 44, 108, 1)", "38px", "700", "32px", "Elza"},
                    [
                        "margin-top",
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

            selectors = ["#home-condition-section #conditionSpotlightsection  a"]

            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")

        elif window_size["width"] > 752 and window_size["width"] < 981:

            log.info("start")

            selectors_and_properties = [
                (
                    "#home-condition-section #conditionSpotlightsection #conditionSpotlighleftsec",
                    {"0px", "713.412px", "0.941176px solid rgb(191, 191, 191)"},
                    ["margin-right", "width", "border-right"],
                ),
                (
                    "#conditionSpotlightsection div#conditionSpotlightrightsec div#lightfeaturedsec img",
                    {"713.412px"},
                    ["width"],
                ),
                (
                    "#conditionSpotlightsection div#conditionSpotlighleftsec .conditionSpotlightblogsec .et_pb_blurb_container h4 a",
                    {"30px", "600", "24px", "Elza"},
                    ["line-height", "font-weight", "font-size", "font-family"],
                ),
                (
                    "#lightfeaturedsec h3",
                    {"10px", "rgba(21, 44, 108, 1)", "38px", "700", "32px", "Elza"},
                    [
                        "margin-top",
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

            selectors = ["#home-condition-section #conditionSpotlightsection  a"]

            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")

        elif window_size["width"] < 753:

            log.info("start")

            selectors_and_properties = [
                (
                    "#home-condition-section #conditionSpotlightsection #conditionSpotlighleftsec",
                    {"0px", "412.19px", "0.761905px solid rgb(191, 191, 191)"},
                    ["margin-right", "width", "border-right"],
                ),
                (
                    "#conditionSpotlightsection div#conditionSpotlightrightsec div#lightfeaturedsec img",
                    {"372.19px"},
                    ["width"],
                ),
                (
                    "#conditionSpotlightsection div#conditionSpotlighleftsec .conditionSpotlightblogsec .et_pb_blurb_container h4 a",
                    {"30px", "600", "24px", "Elza"},
                    ["line-height", "font-weight", "font-size", "font-family"],
                ),
                (
                    "#lightfeaturedsec h3",
                    {"10px", "rgba(21, 44, 108, 1)", "38px", "700", "32px", "Elza"},
                    [
                        "margin-top",
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

            selectors = ["#home-condition-section #conditionSpotlightsection  a"]

            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")
