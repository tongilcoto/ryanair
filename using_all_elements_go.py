from sut.cSearch import RA_Search
from sut.cTimetable import RA_Timetable
from sut.cExtras import RA_Extras
from sut.cPay import RA_Pay
from selenium.webdriver.common.keys import Keys
from configparser import ConfigParser
from datetime import datetime
from datetime import timedelta
from time import sleep

search = RA_Search()

search.set_only_go()

search.set_origin("Dublin")
search.set_destiny("Berlin" + Keys.SPACE + "Schönefeld")

defaults = ConfigParser()
defaults.read("defaults.ini")

go_date = eval(defaults["search"]["startDate"])

search.set_go_date(go_date)

search.set_adults_num(2)

#search.set_teens_num(3)

search.set_children_num(1)

#search.set_infants_num(2)

timetable = RA_Timetable(search.next_step(), return_flight=False)

go_flights = timetable.get_available_flights_for("go_flights")

print(go_flights)

timetable.set_flight_time_for("go_flights", int(defaults["timetable"]["go_flight_sel"]))

timetable.set_tariff(defaults["timetable"]["go_flight_tariff"])

extras = RA_Extras(timetable.next_step(2,0,1,0))

pay = RA_Pay(extras.next_step(defaults["extras"]["seat_sel"]), 3)

pay.login(defaults["login"]["login_social"], defaults["login"]["google_email"], defaults["login"]["google_password"])

pay.fill_passenger(defaults["pay"]["ap1_firstName"], defaults["pay"]["ap1_lastName"], defaults["pay"]["ap1_title"])

pay.fill_passenger(defaults["pay"]["ap2_firstName"], defaults["pay"]["ap2_lastName"], defaults["pay"]["ap2_title"])

pay.fill_passenger(defaults["pay"]["cp1_firstName"], defaults["pay"]["cp1_lastName"])

pay.fill_phone(defaults["pay"]["phoneCountry"], defaults["pay"]["phoneNumber"])

pay.fill_card(defaults["pay"]["cardNumber"], defaults["pay"]["cardCompanyCode"], defaults["pay"]["expiryMonth"],
              defaults["pay"]["expiryYear"], defaults["pay"]["securityCode"], defaults["pay"]["cardHolderName"])

pay.fill_billingAddress(defaults["pay"]["billingAddress"], defaults["pay"]["billingCity"], defaults["pay"]["billingPostCode"])

pay.pay_flights()

print ("You got error:", pay.pay_declined_error())

