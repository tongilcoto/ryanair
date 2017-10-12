from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

class RA_Login:

    def __init__(self, pay_wd):

        self.login = pay_wd

        project_conf = json.load(open("sut/pages_conf.json"))
        self.log_page_conf = project_conf["login"]


    def get_logged (self, social, user, password):

        wait = WebDriverWait(self.login, 10)
        
        wait.until(EC.element_to_be_clickable((self.log_page_conf[social]["by"], self.log_page_conf[social]["value"])))
        self.login.find_element(self.log_page_conf[social]["by"], self.log_page_conf[social]["value"]).click()

        print ("After clicking Social:", self.login.window_handles)

        new_handle = self.login.window_handles[1]

        self.login.switch_to_window(new_handle)

        email_key = social + "_email"
        password_key = social + "_password"
        wait.until(EC.visibility_of_element_located((self.log_page_conf[email_key]["by"], self.log_page_conf[email_key]["value"])))
        self.login.find_element(self.log_page_conf[email_key]["by"], self.log_page_conf[email_key]["value"]).clear()
        self.login.find_element(self.log_page_conf[email_key]["by"], self.log_page_conf[email_key]["value"]).send_keys(user)

        wait.until(EC.element_to_be_clickable((self.log_page_conf[social + "_email_next_page"]["by"], self.log_page_conf[social + "_email_next_page"]["value"])))
        self.login.find_element(self.log_page_conf[social + "_email_next_page"]["by"], self.log_page_conf[social + "_email_next_page"]["value"]).click()

        wait.until(EC.visibility_of_element_located((self.log_page_conf[password_key]["by"], self.log_page_conf[password_key]["value"])))
        self.login.find_element(self.log_page_conf[password_key]["by"], self.log_page_conf[password_key]["value"]).clear()
        self.login.find_element(self.log_page_conf[password_key]["by"], self.log_page_conf[password_key]["value"]).send_keys(password)

        wait.until(EC.element_to_be_clickable((self.log_page_conf[social + "_password_next_page"]["by"], self.log_page_conf[social + "_password_next_page"]["value"])))
        self.login.find_element(self.log_page_conf[social + "_password_next_page"]["by"], self.log_page_conf[social + "_password_next_page"]["value"]).click()

        self.login.switch_to_window(self.login.window_handles[0])
