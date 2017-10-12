from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from time import sleep
from sut.cSeatSelection import RA_SeatSelection


class RA_Timetable:

    def __init__(self, search_wd, return_flight=True):

        project_conf = json.load(open("sut/pages_conf.json"))
        self.tt_page_conf = project_conf["timetable"]

        self.timetable = search_wd

        self.return_flight = return_flight


    def get_available_flights_for(self, bound):
        """
        Only available flights. Sold Out flights not included
        bound: go_flights, return_flights
        :return:
        """

        print (bound)
        sleep(5)

        wait = WebDriverWait(self.timetable, 10)

        #wait.until(EC.presence_of_element_located((self.tt_page_conf[bound]["by"], self.tt_page_conf[bound]["value"])))

        elements = len(self.timetable.find_elements(by=self.tt_page_conf[bound]["by"], value=self.tt_page_conf[bound]["value"]))
        
        return int(elements / 2)


    def set_flight_time_for(self, bound, option_num):
        """
        bound: go_flights, return_flights
        :param bound:
        :param option_num:
        :return:
        """

        print (bound, option_num)
        print (self.tt_page_conf[bound]["value"])

        i = option_num * 2 - 1

        wait = WebDriverWait(self.timetable, 10)

        print("bound:", bound, "i:", i)

        #wait.until(EC.presence_of_element_located((self.tt_page_conf[bound]["by"], self.tt_page_conf[bound]["value"])))
        # Explicit wait: Chrome returns "Element not clickable" after outbound tariff selection
        sleep(3)

        elements = self.timetable.find_elements(by=self.tt_page_conf[bound]["by"], value=self.tt_page_conf[bound]["value"])

        print("elements:", len(elements))

        elements[i].click()


    def set_tariff(self, tariff):
        """
        tariff value must match any page conf keys at timetable section
        :param tariff: 
        :return: 
        """
        wait = WebDriverWait(self.timetable, 10)

        wait.until(EC.element_to_be_clickable((self.tt_page_conf[tariff]["by"], self.tt_page_conf[tariff]["value"])))
        # Explicit wait: Chrome returns "Element not clickable" after flight selection
        sleep(3)
        self.timetable.find_element(by=self.tt_page_conf[tariff]["by"], value=self.tt_page_conf[tariff]["value"]).click()


    def next_step(self, adults, teens, children, infants):
        """
        All are int variables
        :param adults:
        :param teens:
        :param children:
        :param infants:
        :return:
        """

        wait = WebDriverWait(self.timetable, 10)

        wait.until(EC.element_to_be_clickable((self.tt_page_conf["next_page"]["by"], self.tt_page_conf["next_page"]["value"])))
        # Explicit wait: Chrome returns "Element not clickable" after tariff selection
        sleep(3)
        self.timetable.find_element(by=self.tt_page_conf["next_page"]["by"],
                               value=self.tt_page_conf["next_page"]["value"]).click()

        if (children > 0 or infants > 0):

            wait.until(EC.element_to_be_clickable(
                (self.tt_page_conf["family_alert"]["by"], self.tt_page_conf["family_alert"]["value"])))
            self.timetable.find_element(by=self.tt_page_conf["family_alert"]["by"],
                                        value=self.tt_page_conf["family_alert"]["value"]).click()
            seat_sel = RA_SeatSelection(self.timetable)
            # go flight seats
            seat_sel.select_seats(children*2 + infants, self.return_flight)
            self.timetable = seat_sel.next_step()

        return self.timetable

