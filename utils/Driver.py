from appium.webdriver.webdriver import webdriver

class Driver:

    def __init__(self, hub, desired_dict):
        """Constructor"""
        self.driver = webdriver.Remote(hub, desired_dict)

    def get_driver(self):
        """Method that returns the webdriver"""
        return self.driver

    def get_elements_by_id(self, text_target, text_compare_to):
        """Method that gets the correct element inside the list by id."""
        for elem in self.driver.find_elements_by_id(text_target):
            if elem.text.__eq__(text_compare_to):
                return elem


    def get_elements_by_class(self, text_target, text_compare_to):
        """Method that gets the correct element inside the list by class_name."""
        for elem in self.driver.find_elements_by_class_name(text_target):
            if elem.text.__eq__(text_compare_to):
                return elem