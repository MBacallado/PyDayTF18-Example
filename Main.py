from desiredCapabilities.DesiredCapabilities import DesiredCapabilities
from utils.Driver import Driver
from apps.MirApp import MirApp

def test1():
    desired = DesiredCapabilities("Android", "Android", "Xiaomi", "8.1.0", "com.mbacallado.thirdexampleandroid",
                                  ".activities.MainActivity")
    driver = Driver("http://127.0.0.1:4723/wd/hub", desired.__dict__)
    mir_app_test = MirApp(driver)
    mir_app_test.run_app("Tenerife", "Buenavista del Norte", "Mirador Altos de Baracán")

def main():
    test1()

if __name__ == '__main__':
    main()