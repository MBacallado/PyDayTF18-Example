import time
from appium.webdriver.common.touch_action import TouchAction

class Chrome:

    def __init__(self, driver):
        self.driver = driver

    def run_app(self):
        self.__first_activity()
        self.__second_activity()
        self.__third_activity()
        self.__fourth_activity()
        self.__fifth_activity()
        """Method that executes the methods for navigates between activities inside the app"""

    def __first_activity(self):
        time.sleep(5)
        self.driver.get_driver().find_element_by_class_name("android.widget.Button").click()
        print("first activity passed")

    def __second_activity(self):
        time.sleep(5)
        self.driver.get_driver().find_element_by_id("com.android.chrome:id/positive_button").click()
        print("second activity passed")

    def __third_activity(self):
        time.sleep(5)
        self.driver.get_driver().find_element_by_id("com.android.chrome:id/search_box_text").click()
        print("third activity passed")

    def __fourth_activity(self):
        time.sleep(5)
        self.driver.get_driver().find_element_by_id("com.android.chrome:id/url_bar").click()
        time.sleep(5)
        self.driver.get_driver().find_element_by_id("com.android.chrome:id/url_bar").send_keys("http://manuelbacallado.com" +"\n")
        time.sleep(5)
        print("fourth activity passed")

    def __fifth_activity(self):
        actions = TouchAction(self.driver)
        time.sleep(10)
        self.driver.get_driver().find_element_by_xpath("//android.view.View[@index='3']//android.view.View[@index='0']").click()
        time.sleep(10)
        self.driver.get_driver().find_element_by_xpath("//android.view.View[@text='Sobre mí']").click()
        time.sleep(15)
        self.driver.get_driver().find_element_by_xpath("//android.view.View[@index='3']//android.view.View[@index='0']").click()
        time.sleep(10)
        self.driver.get_driver().find_element_by_xpath("//android.view.View[@text='Portfolio']").click()
        time.sleep(15)
        self.driver.get_driver().find_element_by_xpath("//android.view.View[@index='3']//android.view.View[@index='0']").click()
        time.sleep(10)
        self.driver.get_driver().find_element_by_xpath("//android.view.View[@text='Inicio']").click()
        print("fifth activity passed")
