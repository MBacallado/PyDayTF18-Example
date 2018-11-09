
class DesiredCapabilities:

    def __init__(self, device, platform_name, device_name, platform_version, app_package, app_activity):
        """"Constructor for storing the Desired Capabilities attributes"""
        self.device = device
        self.platformName = platform_name
        self.deviceName = device_name
        self.platformVersion = platform_version
        self.appPackage = app_package
        self.appActivity = app_activity
