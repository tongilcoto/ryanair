from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import random
from time import sleep


class RA_SeatSelection:

    def __init__(self, timetable_wd):

        project_conf = json.load(open("sut/pages_conf.json"))
        self.ss_page_conf = project_conf["seat_selection"]

        self.seatsel = timetable_wd


    def get_seats(self, seats):

        free_seats = self.seatsel.find_elements(by=self.ss_page_conf["free_seats"]["by"], value=self.ss_page_conf["free_seats"]["value"])

        if seats > len(free_seats):

            return 0

        print("free seats:", len(free_seats))
        seat = 0
        for i in range(0,seats):

            #TODO: Getting scroll up working ...
            while free_seats[seat].location["y"] < 200:
                seat = seat + 1

            xpath = "(\"" + self.ss_page_conf["free_seats"]["value"] + "\")[{seat}]".format(seat=seat)
            print (xpath)
            # Humans are no so fast ...
            sleep(5)
            free_seats[seat].click()
            print ("seat clicked")
            seat += 1


    def select_seats(self, seats_num, return_flight):

        wait = WebDriverWait(self.seatsel, 10)

        self.get_seats(seats_num)

        if return_flight:

            wait.until(EC.element_to_be_clickable(
                (self.ss_page_conf["next_page"]["by"], self.ss_page_conf["next_page"]["value"])))
            self.seatsel.find_element(by=self.ss_page_conf["next_page"]["by"],
                                      value=self.ss_page_conf["next_page"]["value"]).click()

            # Explicit wait. waiting for location info
            sleep(5)

            #TODO: Develop same seats rejection flow
            if len(self.seatsel.find_elements(by=self.ss_page_conf["same_seats"]["by"],
                                      value=self.ss_page_conf["same_seats"]["value"])) > 0:
                self.seatsel.find_element(by=self.ss_page_conf["same_seats"]["by"],
                                           value=self.ss_page_conf["same_seats"]["value"]).click()

            else:
                self.get_seats(seats_num)

        wait.until(EC.element_to_be_clickable((self.ss_page_conf["next_page"]["by"], self.ss_page_conf["next_page"]["value"])))
        self.seatsel.find_element(by=self.ss_page_conf["next_page"]["by"], value=self.ss_page_conf["next_page"]["value"]).click()


    def next_step(self):

        wait = WebDriverWait(self.seatsel, 10)

        wait.until(EC.element_to_be_clickable((self.ss_page_conf["confirm_after_selection"]["by"], self.ss_page_conf["confirm_after_selection"]["value"])))
        # Explicit wait.
        sleep(3)
        self.seatsel.find_element(by=self.ss_page_conf["confirm_after_selection"]["by"], value=self.ss_page_conf["confirm_after_selection"]["value"]).click()

        wait.until(EC.element_to_be_clickable((self.ss_page_conf["reject_cabin_bags"]["by"], self.ss_page_conf["reject_cabin_bags"]["value"])))
        # Explicit wait.
        sleep(3)
        self.seatsel.find_element(by=self.ss_page_conf["reject_cabin_bags"]["by"], value=self.ss_page_conf["reject_cabin_bags"]["value"]).click()

        return self.seatsel