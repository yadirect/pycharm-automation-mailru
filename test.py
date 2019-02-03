import time

from selenium import webdriver

# path = "C:/Users/root/PycharmProjects/pycharm-automation-mailru/features/drivers/chromedriver.exe"
path = "features/drivers/chromedriver.exe"
driver = webdriver.Chrome(path)

url = "https://e.mail.ru/password/restore/"
driver.get(url)

# driver.delete_all_cookies()
driver.implicitly_wait(4)
driver.set_page_load_timeout(30)
driver.maximize_window()


def check_email(email):
    email_field = driver.find_element_by_id("loginFormEmail")
    email_field.clear()
    email_field.send_keys(email)

    next_button = driver.find_element_by_xpath("/html/body/div[10]/div[1]/div/div[1]/div/div[1]/form/div[3]/div/div/button/span")
    next_button.click()

    time.sleep(2)
    assert "Указанный ящик не существует" in driver.page_source

check_email("##aaaaaaa01")
check_email("##bbbbbbbbbb02")
check_email("##ccccccccccccc03")
check_email("##dddddddddddddddd04")

driver.quit()