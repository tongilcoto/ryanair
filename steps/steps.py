import logging
from behave import given, when, then, use_step_matcher
from selenium.webdriver.common.keys import Keys
from sut.cSearch import RA_Search
from sut.cTimetable import RA_Timetable
from sut.cExtras import RA_Extras
from sut.cPay import RA_Pay
from datetime import datetime

use_step_matcher("re")
@given('I make a booking from "(?P<dep_airport>[\w ]+)" to "(?P<dest_airport>[\w ]+)" on "(?P<dep_date>[\d/]{10})"(?P<ret_data> till "(?P<ret_date>[\d/]{10})")? for "(?P<adults>\d+)" adults(?P<teen_data> and "(?P<teens>\d+)" teen(?P<s1>s)?)?(?P<child_data> and "(?P<children>\d+)" child(?P<s2>ren)?)?(?P<infant_data> and "(?P<infants>\d+)" infant(?P<s3>s)?)?')
def step_search(context, dep_airport, dest_airport, dep_date, ret_data, ret_date, adults, teen_data, teens, s1, child_data, children, s2, infant_data, infants, s3):

    search = RA_Search()

    # Leveraging return_flight as default
    if not ret_date:
        search.set_only_go()

    # Current web version does not allow searches by airport code (3 letters), airports must be used with names
    airport = dep_airport.replace(' ', Keys.SPACE)
    search.set_origin(airport)
    airport = dest_airport.replace(' ', Keys.SPACE)
    search.set_destiny(airport)

    search.set_go_date(datetime(int(dep_date[6:10]), int(dep_date[3:5]), int(dep_date[0:2])))

    if ret_date:
        search.set_go_date(datetime(int(ret_date[6:10]), int(ret_date[3:5]), int(ret_date[0:2])))

    search.set_adults_num(int(adults))

    if teen_data:
        search.set_teens_num(int(teens))
    else:
        teens = '0'

    if child_data:
        search.set_children_num(int(children))
    else:
        children = '0'

    if infant_data:
        search.set_infants_num(int(infants))
    else:
        infants = '0'

    timetable = RA_Timetable(search.next_step(), return_flight=False)

    # Getting number of go flights
    go_flights = timetable.get_available_flights_for("go_flights")

    # This test uses a conf value to choose one of the flights
    timetable.set_flight_time_for("go_flights", int(context.config["timetable"]["go_flight_sel"]))

    # This test uses a conf value to choose one of the tariffs for the chosen flight
    timetable.set_tariff(context.config["timetable"]["go_flight_tariff"])

    if ret_date:
        # Getting number of return flights
        return_flights = timetable.get_available_flights_for("return_flights")

        # This test uses a conf value to choose one of the flights
        timetable.set_flight_time_for("return_flights", int(context.config["timetable"]["return_flight_sel"]))

        # This test uses a conf value to choose one of the tariffs for the chosen flight
        timetable.set_tariff(context.config["timetable"]["return_flight_tariff"])

    context.extras = RA_Extras(timetable.next_step(int(adults), int(teens), int(children), int(infants)))
    context.adults = int(adults)
    context.teens = int(teens)
    context.children = int(children)
    context.infants = int(infants)


@when('I pay for booking with card details "(?P<cardnum>[0-9 ]{16,19})", "(?P<expdate>[\d/]{5})" and "(?P<seccode>[0-9]{3})"')
def step_pay(context, cardnum, expdate, seccode):

    pay_cardnum = cardnum.replace(' ', '')
    exp_month = expdate[0:2]
    exp_year = "20" + expdate[3:5]
    passengrs = context.adults + context.teens + context.children + context.infants
    context.pay = RA_Pay(context.extras.next_step(context.config["extras"]["seat_sel"]), passengrs)

    context.pay.login(context.config["login"]["login_social"], context.config["login"]["google_email"],
              context.config["login"]["google_password"])

    # Be aware of having enough passenger data at conf file
    for i in range (context.adults):

        title = "ap{}_title".format(i+1)
        firstName = "ap{}_firstName".format(i+1)
        lastName = "ap{}_lastName".format(i+1)
        context.pay.fill_passenger(context.config["pay"][firstName], context.config["pay"][lastName], context.config["pay"][title])

    for i in range (context.teens):

        title = "tp{}_title".format(i+1)
        firstName = "tp{}_firstName".format(i+1)
        lastName = "tp{}_lastName".format(i+1)
        context.pay.fill_passenger(context.config["pay"][firstName], context.config["pay"][lastName], context.config["pay"][title])

    for i in range (context.children):

        firstName = "cp{}_firstName".format(i+1)
        lastName = "cp{}_lastName".format(i+1)
        context.pay.fill_passenger(context.config["pay"][firstName], context.config["pay"][lastName])

    for i in range (context.infants):

        firstName = "ip{}_firstName".format(i+1)
        lastName = "ip{}_lastName".format(i+1)
        context.pay.fill_passenger(context.config["pay"][firstName], context.config["pay"][lastName])

    context.pay.fill_phone(context.config["pay"]["phoneCountry"], context.config["pay"]["phoneNumber"])

    context.pay.fill_card(context.config["pay"]["cardNumber"], context.config["pay"]["cardCompanyCode"], context.config["pay"]["expiryMonth"],
                  context.config["pay"]["expiryYear"], context.config["pay"]["securityCode"], context.config["pay"]["cardHolderName"])

    context.pay.fill_billingAddress(context.config["pay"]["billingAddress"], context.config["pay"]["billingCity"],
                            context.config["pay"]["billingPostCode"])

    context.pay.pay_flights()

@then('I should get payment declined message')
def step_got_error(context):

    assert context.pay.pay_declined_error() > 0