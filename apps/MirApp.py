from desiredCapabilities.DesiredCapabilities import DesiredCapabilities
from utils.Driver import Driver
import time

class MirApp:

    def __init__(self, device, platform_name, device_name, platform_version, app_package, app_activity):
        """Constructor"""
        self.desired = DesiredCapabilities(device, platform_name, device_name, platform_version, app_package,
                                           app_activity)
        print(self.desired.__dict__)

    def run_app(self, hub, island, municipality, viewpoint):
        """Method that executes the methods for navigates between activities inside the app"""
        driver = Driver(hub, self.desired.__dict__)
        """driver = webdriver.Remote(hub, self.desired.__dict__)"""
        self.__first_activity(driver, island)
        self.__second_activity(driver, municipality)
        self.__third_activity(driver, viewpoint)
        self.__fourth_activity(driver, viewpoint)

    def __first_activity(self, driver, island):
        """Method that initiates the activity of the island and navigates through it"""
        time.sleep(5)
        driver.get_elements_by_id("islandTextView", island).click()
        print("first activity passed")

    def __second_activity(self, driver, municipality):
        """Method that initiates the activity of the municipalities and navigates through it"""
        time.sleep(5)
        driver.get_elements_by_id("municipalityTextView", municipality).click()
        print("second activity passed")

    def __third_activity(self, driver, viewpoint):
        """Method that initiates the activity of the viewpoints and navigates through it"""
        time.sleep(5)
        driver.get_driver().find_element_by_id("Más opciones").click()
        driver.get_elements_by_id("title", "info app").click()
        time.sleep(5)
        driver.get_driver().back()
        time.sleep(2)
        driver.get_driver().find_element_by_id("Más opciones").click()
        driver.get_elements_by_id("title", "version app").click()
        time.sleep(10)
        driver.get_driver().back()
        driver.get_elements_by_class("android.widget.TextView", viewpoint).click()
        print("third activity passed")

    def __fourth_activity(self, driver, viewpoint):
        """Method that initiates the activity of the map and navigates through it"""
        time.sleep(5)
        driver.get_driver().find_element_by_id(viewpoint + ". ").click()
        driver.get_driver().find_element_by_id("Cómo llegar").click()
        time.sleep(5)
        driver.get_elements_by_class("android.widget.TextView", "INICIAR").click()
        print("fourth activity passed")