from behave import *

import time

from selenium import webdriver

use_step_matcher("re")


@given('I open a browser and navigate to "restore" page')
def step_impl(context):
    path = "features/drivers/chromedriver.exe"
    driver = webdriver.Chrome(path)

    url = "https://e.mail.ru/password/restore/"
    driver.get(url)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    raise NotImplementedError(u'STEP: Given I open a browser and navigate to "restore" page')


@when('I insert an "email"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I insert an "email"')


@step('I click on "restore" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I click on "restore" button')


@then('The "email does not exist" message should be displayed')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then The "email does not exist" message should be displayed')