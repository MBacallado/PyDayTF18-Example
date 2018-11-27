# PyDayTF18-Example
Sample code for PyDayTF18 event

## Example Code

To use appium you need the following instructions:

- Import webdriver

`from appium.webdriver.webdriver import webdriver`

- Create the Desired Capabilities for storing the attributes as **PlatformName**, **DeviceName**, **AppPackage**, etc...

~~~
class DesiredCapabilities:

    def __init__(self, device, platform_name, device_name, platform_version, app_package, app_activity):
        """"Constructor for storing the Desired Capabilities attributes"""
        self.device = device
        self.platformName = platform_name
        self.deviceName = device_name
        self.platformVersion = platform_version
        self.appPackage = app_package
        self.appActivity = app_activity
~~~

- After, in **MirApp.py** constructor
~~~
self.desired = DesiredCapabilities(device, platform_name, device_name, platform_version, app_package,
                                           app_activity)
~~~

- How to obtain the elements for doing click. Two ways: by **id** or by **class_name**

~~~
driver.find_element_by_id(Element).click
~~~

~~~
driver.find_element_by_class_name(Element).click
~~~

## MirApp
MirApp is an application that lists all viewpoints of the Canary Islands and provides the location of all of them.

**Play Store Link** : [MirApp](https://play.google.com/store/apps/details?id=com.mbacallado.thirdexampleandroid)
