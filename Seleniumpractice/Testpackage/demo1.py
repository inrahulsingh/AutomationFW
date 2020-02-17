from selenium import webdriver
import os
import time

class browserlaunch:
    def __init__(self):
        print('I am in init function')
    def chromebrowserlaunch(self):
        driver_location="C:\\Users\\inrah\\PycharmProjects\\Seleniumpractice\\libs\\chromedriver.exe"
        #String declaration of chromedriver.exe path
        os.environ["webdriver.chrome.driver"]=driver_location
        #Programatically setting the environment variable name and value
        driver=webdriver.Chrome(executable_path=driver_location)
        #Created instance of webdriver for chrome browser and stored it in driver variable
        driver.get("https://selenium.dev/")
        #Enters the url and waits until the page gets completely loaded
        time.sleep(5)
        #waits for 5 sec
        driver.close()
        #close the browser


def main():
    obj1=browserlaunch()
    obj1.chromebrowserlaunch()

if __name__ == '__main__':
    main()