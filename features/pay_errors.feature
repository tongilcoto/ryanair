Feature: Pay Errors Scenarios

    In order to check web behaviour upon wrong pay data
    As a ordinary web user
    I write down wrong pay data

    Scenario: 1 way flight for 2 adults and 1 child
      Given  I make a booking from "Dublin" to "Berlin Schönefeld" on "04/12/2017" for "2" adults and "1" children
      When I pay for booking with card details "5555 5555 5555 5557", "10/18" and "265"
      Then I should get payment declined message

