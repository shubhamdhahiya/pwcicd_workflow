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
    @pytest.mark.run(order=38)
    @pytest.mark.dependency(depends=["test_Podcastui"])
    def test_Specialities(self):
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
            self.driver.get("https://www.physiciansweekly.com/specialties/")
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
                    {"0.4px", "500"},
                    ["letter-spacing", "font-weight"],
                ),
                (".breadcrumb", {"10px 0px"}, ["margin"]),
                (
                    "#specialties-columns nav.et-menu-nav .et-menu li",
                    {
                        "404.688px",
                        "inline-block",
                        "1px solid rgb(191, 191, 191)",
                        "0px 0px 12px",
                    },
                    [
                        "display",
                        "margin",
                        "padding",
                        "border-bottom",
                        "width",
                    ],
                ),
                (
                    "#menu-specialties-1 li",
                    {
                        "inline-block",
                        "0px 0px 12px",
                        "404.688px",
                        "1px solid rgb(191, 191, 191)",
                    },
                    [
                        "display",
                        "margin",
                        "padding",
                        "border-bottom",
                        "width",
                    ],
                ),
                (
                    "#menu-specialties-1 li a",
                    {
                        "table-cell",
                        "normal",
                        "rgba(21, 44, 108, 1)",
                        "Elza",
                        "25px",
                        "38px",
                        "600",
                        "0px",
                    },
                    [
                        "padding",
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
                    "h1.is_archive",
                    {
                        "700",
                        "60px",
                        "rgba(21, 44, 108, 1)",
                        "normal",
                        "0.5px",
                        "elza",
                        "0px 0px 20px",
                    },
                    [
                        "font-size",
                        "padding",
                        "color",
                        "line-height",
                        "font-style",
                        "font-family",
                        "font-weight",
                        "font-size",
                        "color",
                        "letter-spacing",
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

            selectors = ["#menu-specialties-1 li a"]
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")

        elif window_size["width"] > 752 and window_size["width"] < 981:

            self.driver.get("https://www.physiciansweekly.com/specialties/")

            log.info("start")

            selectors_and_properties = [
                (
                    "#et-boc .breadcrumb #crumbs",
                    {
                        "elza, sans-serif",
                        "rgba(55, 55, 55, 1)",
                        "14px",
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
                    {"0.28px", "500"},
                    ["letter-spacing", "font-weight"],
                ),
                (".breadcrumb", {"10px 0px"}, ["margin"]),
                (
                    "#specialties-columns nav.et-menu-nav .et-menu li",
                    {
                        "349.647px",
                        "inline-block",
                        "0.941176px solid rgb(191, 191, 191)",
                        "0px 0px 12px",
                    },
                    [
                        "display",
                        "margin",
                        "padding",
                        "border-bottom",
                        "width",
                    ],
                ),
                (
                    "#menu-specialties-1 li",
                    {
                        "inline-block",
                        "0px 0px 12px",
                        "349.647px",
                        "0.941176px solid rgb(191, 191, 191)",
                    },
                    [
                        "display",
                        "margin",
                        "padding",
                        "border-bottom",
                        "width",
                    ],
                ),
                (
                    "#menu-specialties-1 li a",
                    {
                        "0px",
                        "table-cell",
                        "Elza",
                        "rgba(21, 44, 108, 1)",
                        "28px",
                        "normal",
                        "600",
                        "20px",
                    },
                    [
                        "padding",
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
                    "h1.is_archive",
                    {
                        "700",
                        "60px",
                        "rgba(21, 44, 108, 1)",
                        "normal",
                        "0.5px",
                        "elza",
                        "0px 0px 20px",
                    },
                    [
                        "font-size",
                        "padding",
                        "color",
                        "line-height",
                        "font-style",
                        "font-family",
                        "font-weight",
                        "font-size",
                        "color",
                        "letter-spacing",
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

            selectors = ["#menu-specialties-1 li a"]
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")

        elif window_size["width"] < 753:
            self.driver.get("https://www.physiciansweekly.com/specialties/")
            log.info("start")

            selectors_and_properties = [
                (
                    "#et-boc .breadcrumb #crumbs",
                    {
                        "elza, sans-serif",
                        "rgba(55, 55, 55, 1)",
                        "normal",
                        "24px",
                        "uppercase",
                        "700",
                        "14px",
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
                    {"0.28px", "500"},
                    ["letter-spacing", "font-weight"],
                ),
                (".breadcrumb", {"10px 0px"}, ["margin"]),
                (
                    "#specialties-columns nav.et-menu-nav .et-menu li",
                    {
                        "372.19px",
                        "inline-block",
                        "0.761905px solid rgb(191, 191, 191)",
                        "0px 0px 12px",
                    },
                    [
                        "display",
                        "margin",
                        "padding",
                        "border-bottom",
                        "width",
                    ],
                ),
                (
                    "#menu-specialties-1 li",
                    {
                        "inline-block",
                        "0px 0px 12px",
                        "372.19px",
                        "0.761905px solid rgb(191, 191, 191)",
                    },
                    [
                        "display",
                        "margin",
                        "padding",
                        "border-bottom",
                        "width",
                    ],
                ),
                (
                    "#menu-specialties-1 li a",
                    {
                        "Elza",
                        "600",
                        "0px",
                        "28px",
                        "20px",
                        "normal",
                        "rgba(21, 44, 108, 1)",
                        "table-cell",
                    },
                    [
                        "padding",
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
                    "h1.is_archive",
                    {
                        "700",
                        "36px",
                        "rgba(21, 44, 108, 1)",
                        "normal",
                        "0.5px",
                        "elza",
                        "0px 20px 6px",
                    },
                    [
                        "font-size",
                        "padding",
                        "color",
                        "line-height",
                        "font-style",
                        "font-family",
                        "font-weight",
                        "font-size",
                        "color",
                        "letter-spacing",
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

            selectors = ["#menu-specialties-1 li a"]
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")
