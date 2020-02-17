from selenium import webdriver
import os
import time

class browserlaunch:
    def __init__(self):
        print('I am in init function')

    def chromebrowserlaunch(self):
        driver_location="C:\\Users\\inrah\\PycharmProjects\\Seleniumpractice\\libs\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"]=driver_location
        driver=webdriver.Chrome(executable_path=driver_location)

        driver.get("https://selenium.dev/")
        time.sleep(5)
        driver.close()

    def ffbrowserlaunch(self):
        driver_location="C:\\Users\\inrah\\PycharmProjects\\Seleniumpractice\\libs\\geckodriver.exe"
        os.environ["webdriver.gecko.driver"]=driver_location
        driver=webdriver.Firefox(executable_path=driver_location)

        driver.get("https://selenium.dev/")
        time.sleep(5)
        driver.close()

    def iebrowserlaunch(self):
        driver_location="C:\\Users\\inrah\\PycharmProjects\\Seleniumpractice\\libs\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"]=driver_location
        driver=webdriver.Ie(executable_path=driver_location)

        driver.get("https://selenium.dev/")
        time.sleep(5)
        driver.close()

def main():
    obj1 = browserlaunch()
    obj1.chromebrowserlaunch()

if __name__ == '__main__':
    main()