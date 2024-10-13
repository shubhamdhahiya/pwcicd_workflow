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
    @pytest.mark.run(order=37)
    @pytest.mark.dependency(depends=["test_prePodcastui"])
    def test_Podcastui(self):
        wait = WebDriverWait(self.driver, 20)
        name = self.driver.name

        log = self.getLogger()
        log.info(name)
        helper = SeleniumHelper(self.driver)

        window_size = self.driver.get_window_size()
        if window_size["width"] > 980:

            self.driver.get("https://www.physiciansweekly.com/podcast/")
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
                    "#et-boc .breadcrumb #crumbs",
                    {
                        "elza, sans-serif",
                        "rgba(55, 55, 55, 1)",
                        "20px",
                        "normal",
                        "24px",
                        "uppercase",
                        "700",
                    },
                    [
                        "text-transform",
                        "line-height",
                        "font-size",
                        "color",
                        "font-weight",
                        "font-style",
                        "font-family",
                    ],
                ),
                (
                    "#crumbs .current",
                    {".02em", "500"},
                    ["letter-spacing", "font-weight"],
                ),
                (".breadcrumb", {"10px 0"}, ["margin"]),
                (
                    "span.published",
                    {
                        "28px",
                        "uppercase",
                        "rgba(1, 121, 217, 1)",
                        "none",
                        "0px",
                        "elza",
                        "elza, sans-serif",
                        "500",
                        "14px",
                        "0.35px",
                        "700",
                        "normal",
                    },
                    [
                        "text-transform",
                        "letter-spacing",
                        "line-height",
                        "font-style",
                        "font-family",
                        "font-weight",
                        "font-size",
                        "color",
                        "margin",
                    ],
                ),
                (
                    "h2",
                    {
                        "36px",
                        "24px",
                        "392.031px",
                        "620.094px",
                        "elza, sans-serif",
                        "28px",
                        "flex",
                        "600",
                        "30px",
                        "700",
                        "39px",
                        "rgba(21, 44, 108, 1)",
                        "normal",
                        "0px",
                        "0px 0px 20px",
                        "Elza",
                        "890.859px",
                        "0px 0px 25px",
                        "block",
                    },
                    [
                        "padding",
                        "width",
                        "display",
                        "line-height",
                        "font-style",
                        "font-family",
                        "font-weight",
                        "font-size",
                        "color",
                    ],
                ),
                (
                    ".post-data p",
                    {
                        "17px",
                        "10px 0px 0px",
                        "0px 0px 10px",
                        "700",
                        "rgba(255, 255, 255, 1)",
                        "10px",
                        "23.4px",
                        "Elza",
                        "18px",
                        "10px 0px",
                        "none",
                        "400",
                        "rgba(21, 44, 108, 1)",
                        "22px",
                        "14px",
                        "0px",
                        "block",
                    },
                    [
                        "line-height",
                        "color",
                        "font-size",
                        "font-weight",
                        "font-family",
                        "padding-bottom",
                        "display",
                        "margin-bottom",
                        "margin",
                    ],
                ),
                (
                    ".et_pb_section div[class*=et_pb_row_]",
                    {
                        "40px 71.5px 0px",
                        "57px 0px 0px",
                        "7px 20px 43px",
                        "40px 51.5px 0px",
                        "0px 10px",
                        "0px 71.5px",
                        "55px 0px",
                        "65px 71.5px 40px",
                        "30px 20px 40px",
                        "1230px",
                        "30px 0px 0px",
                        "1280px",
                        "0px 51.5px",
                        "400",
                        "65px auto 40px",
                        "100%",
                        "20px 71.5px 0px",
                        "0px",
                    },
                    [
                        "width",
                        "padding",
                        "margin",
                        "font-weight",
                        "max-width",
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

        elif window_size["width"] > 752 and window_size["width"] < 981:

            log.info("start")

            self.driver.get("https://www.physiciansweekly.com/podcast/")
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
                    "#et-boc .breadcrumb #crumbs",
                    {
                        "elza, sans-serif",
                        "rgba(55, 55, 55, 1)",
                        "20px",
                        "normal",
                        "24px",
                        "uppercase",
                        "700",
                    },
                    [
                        "text-transform",
                        "line-height",
                        "font-size",
                        "color",
                        "font-weight",
                        "font-style",
                        "font-family",
                    ],
                ),
                (
                    "#crumbs .current",
                    {".02em", "500"},
                    ["letter-spacing", "font-weight"],
                ),
                (".breadcrumb", {"10px 0"}, ["margin"]),
                (
                    "span.published",
                    {
                        "28px",
                        "uppercase",
                        "rgba(1, 121, 217, 1)",
                        "none",
                        "0px",
                        "elza",
                        "elza, sans-serif",
                        "500",
                        "14px",
                        "0.35px",
                        "700",
                        "normal",
                    },
                    [
                        "text-transform",
                        "letter-spacing",
                        "line-height",
                        "font-style",
                        "font-family",
                        "font-weight",
                        "font-size",
                        "color",
                        "margin",
                    ],
                ),
                (
                    "h2",
                    {
                        "36px",
                        "24px",
                        "392.031px",
                        "620.094px",
                        "elza, sans-serif",
                        "28px",
                        "flex",
                        "600",
                        "30px",
                        "700",
                        "39px",
                        "rgba(21, 44, 108, 1)",
                        "normal",
                        "0px",
                        "0px 0px 20px",
                        "Elza",
                        "890.859px",
                        "0px 0px 25px",
                        "block",
                    },
                    [
                        "padding",
                        "width",
                        "display",
                        "line-height",
                        "font-style",
                        "font-family",
                        "font-weight",
                        "font-size",
                        "color",
                    ],
                ),
                (
                    ".post-data p",
                    {
                        "17px",
                        "10px 0px 0px",
                        "0px 0px 10px",
                        "700",
                        "rgba(255, 255, 255, 1)",
                        "10px",
                        "23.4px",
                        "Elza",
                        "18px",
                        "10px 0px",
                        "none",
                        "400",
                        "rgba(21, 44, 108, 1)",
                        "22px",
                        "14px",
                        "0px",
                        "block",
                    },
                    [
                        "line-height",
                        "color",
                        "font-size",
                        "font-weight",
                        "font-family",
                        "padding-bottom",
                        "display",
                        "margin-bottom",
                        "margin",
                    ],
                ),
                (
                    ".et_pb_section div[class*=et_pb_row_]",
                    {
                        "30px 0px 0px",
                        "0px 0px -26px",
                        "20px 20px 0px",
                        "0px 20px",
                        "40px 0px 0px",
                        "4px",
                        "0px",
                        "5px 4px 5px 0px",
                        "713.412px",
                        "65px 0px 40px",
                        "753.412px",
                        "400",
                        "30px 20px 40px",
                        "55px 0px",
                        "0px 10px",
                        "57px 0px 0px",
                        "0px -4px 0px 0px",
                        "65px auto 40px",
                        "7px 20px 20px",
                        "20px 0px 0px",
                        "100%",
                        "1280px",
                    },
                    [
                        "width",
                        "padding",
                        "margin",
                        "font-weight",
                        "max-width",
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

        elif window_size["width"] < 753:

            self.driver.get("https://www.physiciansweekly.com/podcast/")
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
                    "#et-boc .breadcrumb #crumbs",
                    {
                        "elza, sans-serif",
                        "rgba(55, 55, 55, 1)",
                        "20px",
                        "normal",
                        "24px",
                        "uppercase",
                        "700",
                    },
                    [
                        "text-transform",
                        "line-height",
                        "font-size",
                        "color",
                        "font-weight",
                        "font-style",
                        "font-family",
                    ],
                ),
                (
                    "#crumbs .current",
                    {".02em", "500"},
                    ["letter-spacing", "font-weight"],
                ),
                (".breadcrumb", {"10px 0"}, ["margin"]),
                (
                    "span.published",
                    {
                        "28px",
                        "uppercase",
                        "rgba(1, 121, 217, 1)",
                        "none",
                        "0px",
                        "elza",
                        "elza, sans-serif",
                        "500",
                        "14px",
                        "0.35px",
                        "700",
                        "normal",
                    },
                    [
                        "text-transform",
                        "letter-spacing",
                        "line-height",
                        "font-style",
                        "font-family",
                        "font-weight",
                        "font-size",
                        "color",
                        "margin",
                    ],
                ),
                (
                    "h2",
                    {
                        "36px",
                        "24px",
                        "392.031px",
                        "620.094px",
                        "elza, sans-serif",
                        "28px",
                        "flex",
                        "600",
                        "30px",
                        "700",
                        "39px",
                        "rgba(21, 44, 108, 1)",
                        "normal",
                        "0px",
                        "0px 0px 20px",
                        "Elza",
                        "890.859px",
                        "0px 0px 25px",
                        "block",
                    },
                    [
                        "padding",
                        "width",
                        "display",
                        "line-height",
                        "font-style",
                        "font-family",
                        "font-weight",
                        "font-size",
                        "color",
                    ],
                ),
                (
                    ".post-data p",
                    {
                        "17px",
                        "10px 0px 0px",
                        "0px 0px 10px",
                        "700",
                        "rgba(255, 255, 255, 1)",
                        "10px",
                        "23.4px",
                        "Elza",
                        "18px",
                        "10px 0px",
                        "none",
                        "400",
                        "rgba(21, 44, 108, 1)",
                        "22px",
                        "14px",
                        "0px",
                        "block",
                    },
                    [
                        "line-height",
                        "color",
                        "font-size",
                        "font-weight",
                        "font-family",
                        "padding-bottom",
                        "display",
                        "margin-bottom",
                        "margin",
                    ],
                ),
                (
                    ".et_pb_section div[class*=et_pb_row_]",
                    {
                        "7px 20px 20px",
                        "1280px",
                        "65px 0px 40px",
                        "412.19px",
                        "65px auto 40px",
                        "4px",
                        "0px 20px",
                        "30px 20px 40px",
                        "372.19px",
                        "0px -4px 0px 0px",
                        "20px 0px 0px",
                        "0px 10px",
                        "20px 20px 0px",
                        "57px 0px 0px",
                        "0px",
                        "5px 4px 5px 0px",
                        "30px 0px 0px",
                        "100%",
                        "20px 0px",
                        "0px 0px -22px",
                        "400",
                    },
                    [
                        "width",
                        "padding",
                        "margin",
                        "font-weight",
                        "max-width",
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
