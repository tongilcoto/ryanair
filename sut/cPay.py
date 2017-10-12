from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sut.cLogin import RA_Login
import json
from time import sleep

class RA_Pay:

    def __init__(self, extras_wd, passengrs_num):

        self.pay = extras_wd

        project_conf = json.load(open("sut/pages_conf.json"))
        self.pay_page_conf = project_conf["pay"]

        self.passengrs = []
        self.passengrs_num = passengrs_num

    def login(self, social, user, password):

        wait = WebDriverWait(self.pay, 10)


        wait.until(EC.element_to_be_clickable((self.pay_page_conf["login"]["by"], self.pay_page_conf["login"]["value"])))
        self.pay.find_element(self.pay_page_conf["login"]["by"], self.pay_page_conf["login"]["value"]).click()

        print ("After clicking Login:", self.pay.window_handles)

        get_login = RA_Login(self.pay)
        get_login.get_logged(social, user, password)

        print ("After entering password:", self.pay.window_handles)


    def fill_passenger(self, first, last, title=None):

        wait = WebDriverWait(self.pay, 10)

        if self.passengrs_num > 1:
            if self.passengrs_num == []:
                i = 0
            else:
                i =  len(self.passengrs)
            self.passengrs.append(True)

            self.pay.switch_to_default_content()

            if title:
                title_xp = self.pay_page_conf["passengers"]["value"] + \
                           "[{j}]".format(j=i+1) + \
                           self.pay_page_conf["title"]["value"].format(title=title)

                wait.until(EC.element_to_be_clickable((self.pay_page_conf["passengers"]["by"], title_xp)))
                sleep(5)
                self.pay.find_element(self.pay_page_conf["passengers"]["by"], title_xp).click()
                #Explicit wait. lets the change take effect
                sleep(2)

            fn_xp = self.pay_page_conf["passengers"]["value"] + \
                           "[{j}]".format(j=i+1) + \
                           self.pay_page_conf["firstName"]["value"]

            wait.until(EC.visibility_of_element_located((self.pay_page_conf["passengers"]["by"], fn_xp)))

            #self.pay.find_element(self.pay_page_conf["passengers"]["by"], fn_xp).clear()
            self.pay.find_element(self.pay_page_conf["passengers"]["by"], fn_xp).send_keys(first)
            # Explicit wait. lets the change take effect
            sleep(2)

            ln_xp = self.pay_page_conf["passengers"]["value"] + \
                    "[{j}]".format(j=i + 1) + \
                    self.pay_page_conf["lastName"]["value"]

            wait.until(EC.visibility_of_element_located((self.pay_page_conf["passengers"]["by"], ln_xp)))
            #self.pay.find_element(self.pay_page_conf["passengers"]["by"], ln_xp).clear()
            self.pay.find_element(self.pay_page_conf["passengers"]["by"], ln_xp).send_keys(last)
            # Explicit wait. lets the change take effect
            sleep(2)


        else:

            if title:
                title_xp = self.pay_page_conf["passengers"]["value"] + self.pay_page_conf["title"]["value"].format(title=title)

                wait.until(EC.element_to_be_clickable((self.pay_page_conf["passengers"]["by"], title_xp)))
                self.pay.find_element(self.pay_page_conf["passengers"]["by"], title_xp).click()
                #Explicit wait. lets the change take effect
                sleep(2)

            fn_xp = self.pay_page_conf["passengers"]["value"] + self.pay_page_conf["firstName"]["value"]

            wait.until(EC.visibility_of_element_located((self.pay_page_conf["passengers"]["by"], fn_xp)))

            #self.pay.find_element(self.pay_page_conf["passengers"]["by"], fn_xp).clear()
            self.pay.find_element(self.pay_page_conf["passengers"]["by"], fn_xp).send_keys(first)
            # Explicit wait. lets the change take effect
            sleep(2)

            ln_xp = self.pay_page_conf["passengers"]["value"] + self.pay_page_conf["lastName"]["value"]

            wait.until(EC.visibility_of_element_located((self.pay_page_conf["passengers"]["by"], ln_xp)))
            #self.pay.find_element(self.pay_page_conf["passengers"]["by"], ln_xp).clear()
            self.pay.find_element(self.pay_page_conf["passengers"]["by"], ln_xp).send_keys(last)
            # Explicit wait. lets the change take effect
            sleep(2)

    def fill_phone(self, country, number):

        wait = WebDriverWait(self.pay, 10)
        wait.until(EC.visibility_of_element_located((self.pay_page_conf["phoneCountry"]["by"], self.pay_page_conf["phoneCountry"]["value"].format(phCnt=country))))
        self.pay.find_element(self.pay_page_conf["phoneCountry"]["by"], self.pay_page_conf["phoneCountry"]["value"].format(phCnt=country)).click()
        # Explicit wait. lets the change take effect
        sleep(2)

        wait.until(EC.visibility_of_element_located((self.pay_page_conf["phoneNumber"]["by"], self.pay_page_conf["phoneNumber"]["value"])))
        self.pay.find_element(self.pay_page_conf["phoneNumber"]["by"], self.pay_page_conf["phoneNumber"]["value"].format(phCnt=country)).send_keys(number)
        # Explicit wait. lets the change take effect
        sleep(2)


    def fill_card(self, number, company, month, year, security, name):

        wait = WebDriverWait(self.pay, 10)
        wait.until(EC.visibility_of_element_located((self.pay_page_conf["cardNumber"]["by"], self.pay_page_conf["cardNumber"]["value"])))
        self.pay.find_element(self.pay_page_conf["cardNumber"]["by"], self.pay_page_conf["cardNumber"]["value"]).send_keys(number)
        # Explicit wait. lets the change take effect
        sleep(2)

        wait.until(EC.visibility_of_element_located((self.pay_page_conf["cardCompany"]["by"], self.pay_page_conf["cardCompany"]["value"])))
        self.pay.find_element(self.pay_page_conf["cardCompany"]["by"], self.pay_page_conf["cardCompany"]["value"]).click()
        # Explicit wait. lets the change take effect
        sleep(2)

        wait.until(EC.visibility_of_element_located((self.pay_page_conf["expiryMonth"]["by"], self.pay_page_conf["expiryMonth"]["value"].format(month=month))))
        self.pay.find_element(self.pay_page_conf["expiryMonth"]["by"], self.pay_page_conf["expiryMonth"]["value"].format(month=month)).click()
        # Explicit wait. lets the change take effect
        sleep(2)

        wait.until(EC.visibility_of_element_located((self.pay_page_conf["expiryYear"]["by"], self.pay_page_conf["expiryYear"]["value"].format(year=year))))
        self.pay.find_element(self.pay_page_conf["expiryYear"]["by"], self.pay_page_conf["expiryYear"]["value"].format(year=year)).click()
        # Explicit wait. lets the change take effect
        sleep(2)

        wait.until(EC.visibility_of_element_located((self.pay_page_conf["securityCode"]["by"], self.pay_page_conf["securityCode"]["value"])))
        self.pay.find_element(self.pay_page_conf["securityCode"]["by"], self.pay_page_conf["securityCode"]["value"]).send_keys(security)
        # Explicit wait. lets the change take effect
        sleep(2)

        wait.until(EC.visibility_of_element_located((self.pay_page_conf["cardHolderName"]["by"], self.pay_page_conf["cardHolderName"]["value"])))
        self.pay.find_element(self.pay_page_conf["cardHolderName"]["by"], self.pay_page_conf["cardHolderName"]["value"]).send_keys(name)
        # Explicit wait. lets the change take effect
        sleep(2)


    def fill_billingAddress(self, address, city, postcd, country=None):

        wait = WebDriverWait(self.pay, 10)

        wait.until(EC.visibility_of_element_located((self.pay_page_conf["billingAddress"]["by"], self.pay_page_conf["billingAddress"]["value"])))
        self.pay.find_element(self.pay_page_conf["billingAddress"]["by"], self.pay_page_conf["billingAddress"]["value"]).send_keys(address)
        # Explicit wait. lets the change take effect
        sleep(2)

        wait.until(EC.visibility_of_element_located((self.pay_page_conf["billingCity"]["by"], self.pay_page_conf["billingCity"]["value"])))
        self.pay.find_element(self.pay_page_conf["billingCity"]["by"], self.pay_page_conf["billingCity"]["value"]).send_keys(city)
        # Explicit wait. lets the change take effect
        sleep(2)

        wait.until(EC.visibility_of_element_located((self.pay_page_conf["billingPostCode"]["by"], self.pay_page_conf["billingPostCode"]["value"])))
        self.pay.find_element(self.pay_page_conf["billingPostCode"]["by"], self.pay_page_conf["billingPostCode"]["value"]).send_keys(postcd)
        # Explicit wait. lets the change take effect
        sleep(2)

        if country:

            wait.until(EC.visibility_of_element_located(
                (self.pay_page_conf["billingCity"]["by"], self.pay_page_conf["billingCity"]["value"].format(country=country))))
            self.pay.find_element(self.pay_page_conf["billingCity"]["by"],
                                  self.pay_page_conf["billingCity"]["value"].format(country=country)).click()
            # Explicit wait. lets the change take effect
            sleep(2)


    def pay_flights(self):

        wait = WebDriverWait(self.pay, 10)

        wait.until(EC.presence_of_element_located((self.pay_page_conf["accept_checkbox"]["by"], self.pay_page_conf["accept_checkbox"]["value"])))
        self.pay.find_element(self.pay_page_conf["accept_checkbox"]["by"], self.pay_page_conf["accept_checkbox"]["value"]).click()

        wait.until(EC.visibility_of_element_located(
            (self.pay_page_conf["next_page"]["by"], self.pay_page_conf["next_page"]["value"])))
        self.pay.find_element(self.pay_page_conf["next_page"]["by"],
                              self.pay_page_conf["next_page"]["value"]).click()


    def pay_declined_error(self):

        wait = WebDriverWait(self.pay, 30)

        try:
            wait.until(EC.presence_of_element_located((self.pay_page_conf["payError_Declined"]["by"], self.pay_page_conf["payError_Declined"]["value"])))

        except TimeoutException:

            return 0

        return 1



