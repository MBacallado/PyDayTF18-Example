import time

class MirApp:

    def __init__(self, driver):
        """Constructor"""
        self.driver = driver

    def run_app(self, island, municipality, viewpoint):
        """Method that executes the methods for navigates between activities inside the app"""
        self.__first_activity(island)
        self.__second_activity(municipality)
        self.__third_activity(viewpoint)
        self.__fourth_activity(viewpoint)

    def __first_activity(self, island):
        """Method that initiates the activity of the island and navigates through it"""
        time.sleep(5)
        self.driver.get_elements_by_id("islandTextView", island).click()
        print("first activity passed")

    def __second_activity(self, municipality):
        """Method that initiates the activity of the municipalities and navigates through it"""
        time.sleep(5)
        self.driver.get_elements_by_id("municipalityTextView", municipality).click()
        print("second activity passed")

    def __third_activity(self, viewpoint):
        """Method that initiates the activity of the viewpoints and navigates through it"""
        time.sleep(5)
        self.driver.get_driver().find_element_by_id("Más opciones").click()
        self.driver.get_elements_by_id("title", "info app").click()
        time.sleep(5)
        self.driver.get_driver().back()
        time.sleep(2)
        self.driver.get_driver().find_element_by_id("Más opciones").click()
        self.driver.get_elements_by_id("title", "version app").click()
        time.sleep(10)
        self.driver.get_driver().back()
        self.driver.get_elements_by_class("android.widget.TextView", viewpoint).click()
        print("third activity passed")

    def __fourth_activity(self, viewpoint):
        """Method that initiates the activity of the map and navigates through it"""
        time.sleep(5)
        self.driver.get_driver().find_element_by_id(viewpoint + ". ").click()
        self.driver.get_driver().find_element_by_id("Cómo llegar").click()
        time.sleep(5)
        self.driver.get_elements_by_class("android.widget.TextView", "INICIAR").click()
        print("fourth activity passed")