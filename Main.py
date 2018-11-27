from apps.MirApp import MirApp

def test1():
    mir_app_test = MirApp("Android", "Android", "Xiaomi", "8.1.0", "com.mbacallado.thirdexampleandroid",
                              ".activities.MainActivity")
    mir_app_test.run_app("http://127.0.0.1:4723/wd/hub", "Tenerife", "Buenavista del Norte", "Mirador Altos de Baracán")

def main():
    test1()

if __name__ == '__main__':
    main()