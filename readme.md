# RYANAIR WEB TEST

## INTRODUCTION

This exercise has been made in order to accomplish QA Automation position tasks

Although only one test have been developed, the page objects architecture allows for multiple tests with just a few modifications using Gherkin language


## Page objects

Ryanair web page has been modeled with 6 classes: RA_Search, RA_Timetable, RA_SeatSelection, RA_Extras, RA_Pay and RA_Login

All these classes emulates every page present at flights booking flow
 
All of them share a configuration file containing the finding keys that Selenium framework uses to find the desired element that have to be managed following test objetives.

This method avoids touching the code upon a found bug. Also it gives a complete overview of the pages object model


## Initial data configuration

With such a a wide range of possibilities as a flight booking flow, this exercise uses a defaults data configuration file, in order to reduce data at the test case definition. Just for example names of all passengers
 
 
## TDD

This exercise uses also TDD in order to integrate all these classes into the test plan.

The more complicated declaration is flight configuration: go or return? so do you need return flight date? how many passengers and their ages?, and then their names, with several flights the selected day which one to choose?, once selected, which tariff to choose?

This exercise uses Python's Behave TDD framework. This framework allows powerful regular expressions that are managed in order to get all these details, although some of them are also supported by defaults values at the configuration file as explained before

The files are distributed through 3 directories
* features: Files containing tests declarations using Gherkin language
* steps: Files containing python code that translate Gherkin language into pages objects language, delivering tests steps implementation
* sut: pages object classes and configuration file

There are also some files at project directory:
* configuration file
* behave's environment.py file
* proof of concept files testing pages objects model

## Notes of interest

- Accesing ryanair.com/ie/en from Spain, ryaniar redirects the url to /es/es. So some more clicks were needed
- Some limitations are writed down all along the code




