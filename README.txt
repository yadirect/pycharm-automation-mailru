=======================================
Installation
=======================================

Git
https://git-scm.com/
git --version

Python
https://www.python.org/downloads/

PyCharm Professional
https://www.jetbrains.com/pycharm/

Settings > Project Interpreter
Packages are needed:
pip install behave
pip install selenium    # for Web browser integration
pip install requests    # for REST API calls

xPath Finder
https://chrome.google.com/webstore/detail/xpath-finder/ihnknokegkbpmofmafnkoadfjkhlogph/related

Gherkin Best Practices
https://www.youtube.com/watch?v=nrggIRWK6qo

Selenium
https://www.seleniumhq.org/download/
Third Party Drivers

Google Chrome Driver
>>>  chromedriver.exe

Mozilla GeckoDriver
>>>  geckodriver.exe

=======================================
Project
=======================================

test.pt

/features >> Mark directory as Sources Root

/features/feature-name.feature
  Feature: feature-name
    @feature-name-TAG
    Scenario:
      Given (Precondition) I login as "user1"
      When (Action) I navigate to the "account" page
      And (Action) I click on "sign out" on the "account" page
      Then (Assertion) the "home" page should be displayed
      When (Action) I click on "sign in" on the "home" page
      And (Action) I click on "sign in" on the "sign in" page
      Then (Assertion) the "sign in" page should be displayed
      And (Assertion) the "invalid user error" field should be "visible"

>> Alt + Enter >> Create All step definition

/features/steps/feature-name_steps.py

/features//drivers/chromedriver.exe

=======================================
Run
=======================================

C:\Users\root\PycharmProjects\pycharm-automation-mailru\venv\Scripts\python.exe C:/Users/root/PycharmProjects/pycharm-automation-mailru/test.py

behave -help

To run the framework:
behave

behave features\feature-name.feature

To run the framework with tag:
behave --tags-help

behave --tags @feature-name-TAG

behave --tags @verify