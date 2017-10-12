from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from time import sleep

class RA_Extras:

    def __init__(self, timetable_wd):

        self.extras = timetable_wd

        project_conf = json.load(open("sut/pages_conf.json"))
        self.extras_page_conf = project_conf["extras"]


    def next_step(self, seat_sel):
        """
        seat_sel: "reject_seats_selection", "confirm_seats_selection"
        :param seat_sel:
        :return:
        """

        wait=WebDriverWait(self.extras, 10)

        wait.until(EC.element_to_be_clickable((self.extras_page_conf["next_page"]["by"], self.extras_page_conf["next_page"]["value"])))
        #Explicit wait. not clickable
        sleep(3)
        self.extras.find_element(by=self.extras_page_conf["next_page"]["by"], value=self.extras_page_conf["next_page"]["value"]).click()

        print (seat_sel)
        wait.until(EC.element_to_be_clickable((self.extras_page_conf[seat_sel]["by"], self.extras_page_conf[seat_sel]["value"])))
        #Explicit wait. not clickable
        sleep(5)
        self.extras.find_element(by=self.extras_page_conf[seat_sel]["by"], value=self.extras_page_conf[seat_sel]["value"]).click()

        return self.extras




