from behave import *

import time


use_step_matcher("re")


@given('I open a browser and navigate to "restore" page')
def step_impl(context):
    driver = webdriver.Chrome("features/drivers/chromedriver.exe")
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.set_page_load_timeout(30)
    driver.get("https://e.mail.ru/password/restore/")


@when('I insert an "email"')
def step_impl(context):
    email_field = driver.find_element_by_id("loginFormEmail")
    email_field.clear()
    email_field.send_keys("##aaaaaaa01")



@step('I click on "restore" button')
def step_impl(context):
    next_button = driver.find_element_by_xpath("/html/body/div[10]/div[1]/div/div[1]/div/div[1]/form/div[3]/div/div/button/span")
    next_button.click()



@then('The "email does not exist" message should be displayed')
def step_impl(context):
    time.sleep(2)
    assert "Указанный ящик не существует" in driver.page_source
    driver.quit()

