from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from time import sleep


class RA_Search:

    def __init__(self):

        self.home = webdriver.Chrome()

        self.home.get("http://ryanair.com/ie/en")
        self.home.maximize_window()

        # Ryanair redirects to /es/es, so manual path to /ie/en
        self.home.find_element_by_xpath("//a[@href='/es/es/header/markets']").click()
        self.home.find_element_by_xpath("//a[@href='/ie/en/']").click()

        project_conf = json.load(open("sut/pages_conf.json"))
        self.search_page_conf = project_conf["search"]

        self.adults_num = 1
        self.teens_num = 0
        self.children_num = 0
        self.infants_num = 0

        self.home.find_element(self.search_page_conf["close_cookies"]["by"], self.search_page_conf["close_cookies"]["value"]).click()


    def set_only_go(self):

        self.home.find_element(self.search_page_conf["flight_mode_1way"]["by"], self.search_page_conf["flight_mode_1way"]["value"]).click()


    def set_return_flight(self):

        self.home.find_element(self.search_page_conf["flight_mode_return"]["by"], self.search_page_conf["flight_mode_return"]["value"]).click()


    def set_origin(self, origin):

        #TODO: Support for more than one airport as instant query results
        #TODO: xpath is not language agnostic, is based on a placeholder text
        self.home.find_element(by=self.search_page_conf["airport_depart"]["by"], value=self.search_page_conf["airport_depart"]["value"]).clear()
        self.home.find_element(by=self.search_page_conf["airport_depart"]["by"], value=self.search_page_conf["airport_depart"]["value"]).send_keys(origin)
        self.home.find_element(by=self.search_page_conf["set_airport"]["by"],
                               value=self.search_page_conf["set_airport"]["value"]).click()

    def set_destiny(self, destiny):

        #TODO: Support for more than one airport as instant query results
        #TODO: xpath is not language agnostic, is based on a placeholder text
        self.home.find_element(by=self.search_page_conf["airport_destin"]["by"], value=self.search_page_conf["airport_destin"]["value"]).clear()
        self.home.find_element(by=self.search_page_conf["airport_destin"]["by"], value=self.search_page_conf["airport_destin"]["value"]).send_keys(destiny)
        self.home.find_element(by=self.search_page_conf["set_airport"]["by"],
                               value=self.search_page_conf["set_airport"]["value"]).click()


    def set_go_date(self, go_date):
        """

        :param go_date: datetime class object
        :return:
        """

        self.home.find_element(by=self.search_page_conf["go_date_day"]["by"], value=self.search_page_conf["go_date_day"]["value"]).clear()
        self.home.find_element(by=self.search_page_conf["go_date_day"]["by"],
                               value=self.search_page_conf["go_date_day"]["value"]).send_keys(go_date.day)

        self.home.find_element(by=self.search_page_conf["go_date_month"]["by"],
                               value=self.search_page_conf["go_date_month"]["value"]).clear()
        self.home.find_element(by=self.search_page_conf["go_date_month"]["by"],
                               value=self.search_page_conf["go_date_month"]["value"]).send_keys(go_date.month)

        self.home.find_element(by=self.search_page_conf["go_date_year"]["by"],
                           value=self.search_page_conf["go_date_year"]["value"]).clear()
        self.home.find_element(by=self.search_page_conf["go_date_year"]["by"],
                           value=self.search_page_conf["go_date_year"]["value"]).send_keys(go_date.year)

    def set_return_date(self, return_date):

        self.home.find_element(by=self.search_page_conf["return_date_day"]["by"], value=self.search_page_conf["return_date_day"]["value"]).clear()
        self.home.find_element(by=self.search_page_conf["return_date_day"]["by"],
                               value=self.search_page_conf["return_date_day"]["value"]).send_keys(return_date.day)

        self.home.find_element(by=self.search_page_conf["return_date_month"]["by"],
                               value=self.search_page_conf["return_date_month"]["value"]).clear()
        self.home.find_element(by=self.search_page_conf["return_date_month"]["by"],
                               value=self.search_page_conf["return_date_month"]["value"]).send_keys(return_date.month)

        self.home.find_element(by=self.search_page_conf["return_date_year"]["by"],
                           value=self.search_page_conf["return_date_year"]["value"]).clear()
        self.home.find_element(by=self.search_page_conf["return_date_year"]["by"],
                           value=self.search_page_conf["return_date_year"]["value"]).send_keys(return_date.year)

    def set_adults_num(self, adults_num):
        """

        :param adults_num: int variable
        :return:
        """

        self.home.find_element(by=self.search_page_conf["pax_selector_trigger"]["by"],
                               value=self.search_page_conf["pax_selector_trigger"]["value"]).click()

        for i in range(self.adults_num, adults_num):
            self.home.find_element(by=self.search_page_conf["pax_more_adults"]["by"], value=self.search_page_conf["pax_more_adults"]["value"]).click()

        self.home.find_element(by=self.search_page_conf["pax_selector_trigger"]["by"],
                               value=self.search_page_conf["pax_selector_trigger"]["value"]).click()
        self.adults_num = adults_num

    def set_teens_num(self, teens_num):
        """

        :param teens_num: int variable
        :return:
        """

        self.home.find_element(by=self.search_page_conf["pax_selector_trigger"]["by"],
                               value=self.search_page_conf["pax_selector_trigger"]["value"]).click()

        for i in range(self.teens_num, teens_num):
            self.home.find_element(by=self.search_page_conf["pax_more_teens"]["by"], value=self.search_page_conf["pax_more_teens"]["value"]).click()

        self.home.find_element(by=self.search_page_conf["pax_selector_trigger"]["by"],
                               value=self.search_page_conf["pax_selector_trigger"]["value"]).click()
        self.teens_num = teens_num


    def set_children_num(self, children_num):
        """

        :param children_num: int variable
        :return:
        """

        self.home.find_element(by=self.search_page_conf["pax_selector_trigger"]["by"],
                               value=self.search_page_conf["pax_selector_trigger"]["value"]).send_keys(Keys.NULL)

        self.home.find_element(by=self.search_page_conf["pax_selector_trigger"]["by"],
                               value=self.search_page_conf["pax_selector_trigger"]["value"]).click()

        for i in range(self.children_num, children_num):
            self.home.find_element(by=self.search_page_conf["pax_more_children"]["by"], value=self.search_page_conf["pax_more_children"]["value"]).click()

        self.home.find_element(by=self.search_page_conf["pax_selector_trigger"]["by"],
                               value=self.search_page_conf["pax_selector_trigger"]["value"]).click()
        self.children_num = children_num


    def set_infants_num(self, infants_num):
        """

        :param infants_num: int variable
        :return:
        """

        self.home.find_element(by=self.search_page_conf["pax_selector_trigger"]["by"],
                               value=self.search_page_conf["pax_selector_trigger"]["value"]).click()

        for i in range(self.infants_num, infants_num):
            self.home.find_element(by=self.search_page_conf["pax_more_infants"]["by"], value=self.search_page_conf["pax_more_infants"]["value"]).click()
            if i == self.infants_num:
                self.home.find_element(by=self.search_page_conf["pax_infants_alert"]["by"],
                                   value=self.search_page_conf["pax_infants_alert"]["value"]).click()
                self.home.switch_to.default_content()
                # Explicit wait: Chrome returns "Element not clickable" after alert comfirmation
                sleep(3)


        self.home.find_element(by=self.search_page_conf["pax_selector_trigger"]["by"],
                               value=self.search_page_conf["pax_selector_trigger"]["value"]).click()
        self.infants_num = infants_num


    def next_step(self):

        self.home.find_element(by=self.search_page_conf["next_page"]["by"],
                               value=self.search_page_conf["next_page"]["value"]).click()

        return self.home




