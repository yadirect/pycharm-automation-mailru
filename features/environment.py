from selenium import webdriver

def before_scenario(context, scenario):
    if 'web' in context.tags:
        driver = webdriver.Chrome("features/drivers/chromedriver.exe")
        driver.implicitly_wait(4)
        driver.maximize_window()
        driver.set_page_load_timeout(30)

def after_scenario(context, scenario):
    if 'web' in context.tags:
        driver.quit()