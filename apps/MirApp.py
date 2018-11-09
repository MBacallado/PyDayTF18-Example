from desiredCapabilities.DesiredCapabilities import DesiredCapabilities
from appium.webdriver.webdriver import webdriver
import time

class MirApp:

    def __init__(self, device, platform_name, device_name, platform_version, app_package, app_activity):
        """Constructor"""
        self.desired = DesiredCapabilities(device, platform_name, device_name, platform_version, app_package,
                                           app_activity)
        print(self.desired.__dict__)

    def run_app(self, hub, island, municipality, viewpoint):
        """Method that executes the methods for navigates between activities inside the app"""
        driver = webdriver.Remote(hub, self.desired.__dict__)
        self.__first_activity(driver, island)
        self.__second_activity(driver, municipality)
        self.__third_activity(driver, viewpoint)
        self.__fourth_activity(driver, viewpoint)

    def __first_activity(self, driver, island):
        """Method that initiates the activity of the island and navigates through it"""
        time.sleep(5)
        self.getElement(driver, "id", "islandTextView", island).click()
        print("first activity passed")

    def __second_activity(self, driver, municipality):
        """Method that initiates the activity of the municipalities and navigates through it"""
        time.sleep(5)
        self.getElement(driver, "id", "municipalityTextView", municipality).click()
        print("second activity passed")

    def __third_activity(self, driver, viewpoint):
        """Method that initiates the activity of the viewpoints and navigates through it"""
        time.sleep(5)
        driver.find_element_by_id("Más opciones").click()
        self.getElement(driver, "id", "title", "info app").click()
        time.sleep(5)
        driver.back()
        time.sleep(2)
        driver.find_element_by_id("Más opciones").click()
        self.getElement(driver, "id", "title", "version app").click()
        time.sleep(10)
        driver.back()
        self.getElement(driver, "class name", "android.widget.TextView", viewpoint).click()
        print("third activity passed")

    def __fourth_activity(self, driver, viewpoint):
        """Method that initiates the activity of the map and navigates through it"""
        time.sleep(5)
        driver.find_element_by_id(viewpoint + ". ").click()
        driver.find_element_by_id("Cómo llegar").click()
        time.sleep(5)
        self.getElement(driver, "class name", "android.widget.TextView", "INICIAR").click()
        print("fourth activity passed")

    def getElement(self, driver, find_by, text_target, text_compare_to):
        """Method that runs through the elements and returns the correct one."""
        if find_by.__eq__("id"):
            for elem in driver.find_elements_by_id(text_target):
                if elem.text.__eq__(text_compare_to):
                    return elem
        else:
            for elem in driver.find_elements_by_class_name(text_target):
                if elem.text.__eq__(text_compare_to):
                    return elem