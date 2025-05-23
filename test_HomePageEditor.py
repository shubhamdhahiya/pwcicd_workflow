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
    @pytest.mark.run(order=44)
    @pytest.mark.dependency(depends=["test_Meetingsbriefprograme"])
    def test_HomePageEditor(self):  # these are to be verified on the browser-stack
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
                    "#Editorpickssec .et_pb_code_inner article",
                    {
                        "0px",
                        "0px none rgb(148, 148, 148)",
                        "19px",
                        "1px solid rgb(191, 191, 191)",
                        "block",
                    },
                    ["display", "padding-right", "border-right"],
                ),
                (
                    "#Editorpickssec .et_pb_code_inner article .post-content .post-categories",
                    {
                        "5px",
                        "uppercase",
                        "rgba(1, 121, 217, 1)",
                        "18px",
                        "600",
                        "14px",
                        "Elza",
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
                    "#Editorpickssec .editorBlog .post-media a.entry-featured-image-url img",
                    {"183px"},
                    ["height"],
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

            selectors = [
                "#Editorpickssec .editorBlog h2.entry-title a",
                ".et_pb_post_extra .post-categories",
                "#Editorpickssec .editorBlog .post-media a",
            ]

            log.info("Verifying links for multiple selectors")
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")

        elif window_size["width"] > 752 and window_size["width"] < 981:

            log.info("start")

            selectors_and_properties = [
                (
                    "#Editorpickssec .et_pb_code_inner article",
                    {"713.412px", "block"},
                    ["display", "width"],
                ),
                (
                    "#Editorpickssec .et_pb_code_inner article .post-content .post-categories",
                    {
                        "5px",
                        "uppercase",
                        "rgba(1, 121, 217, 1)",
                        "18px",
                        "600",
                        "14px",
                        "Elza",
                        "0.35px",
                    },
                    [
                        "margin-bottom",
                        "text-transform",
                        "color",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                        "letter-spacing",
                    ],
                ),
                (
                    "#Editorpickssec .editorBlog .post-media a.entry-featured-image-url img",
                    {"200px"},
                    ["height"],
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

            selectors = [
                "#Editorpickssec .editorBlog h2.entry-title a",
                ".et_pb_post_extra .post-categories",
                "#Editorpickssec .editorBlog .post-media a",
            ]

            log.info("Verifying links for multiple selectors")
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")

        elif window_size["width"] < 753:

            log.info("start")

            selectors_and_properties = [
                (
                    "#Editorpickssec .et_pb_code_inner article",
                    {"372.19px", "block", "32px", "10px"},
                    ["display", "width", "padding-bottom", "padding-top"],
                ),
                (
                    "#Editorpickssec .et_pb_code_inner article .post-content .post-categories",
                    {
                        "5px",
                        "uppercase",
                        "rgba(1, 121, 217, 1)",
                        "18px",
                        "600",
                        "14px",
                        "Elza",
                        "0.35px",
                    },
                    [
                        "margin-bottom",
                        "text-transform",
                        "color",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                        "letter-spacing",
                    ],
                ),
                (
                    "#Editorpickssec .editorBlog .post-media a.entry-featured-image-url img",
                    {"200px"},
                    ["height"],
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

            selectors = [
                "#Editorpickssec .editorBlog h2.entry-title a",
                ".et_pb_post_extra .post-categories",
                "#Editorpickssec .editorBlog .post-media a",
            ]

            log.info("Verifying links for multiple selectors")
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")
