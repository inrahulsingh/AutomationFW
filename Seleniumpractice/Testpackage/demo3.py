from selenium import webdriver
import os
import time

class browserlaunch:
    def __init__(self):
        print('I am in init function')
        driver_location_chrome = "C:\\Users\\inrah\\PycharmProjects\\Seleniumpractice\\libs\\chromedriver.exe"
        driver_location_ff = "C:\\Users\\inrah\\PycharmProjects\\Seleniumpractice\\libs\\geckodriver.exe"
        driver_location_ie = "C:\\Users\\inrah\\PycharmProjects\\Seleniumpractice\\libs\\IEDriverServer.exe"
        os.environ["webdriver.chrome.driver"] = driver_location_chrome
        os.environ["webdriver.gecko.driver"] = driver_location_ff
        os.environ["webdriver.ie.driver"] = driver_location_ie
        self.driver=webdriver.Chrome(executable_path=driver_location_chrome)
        #self.driver=webdriver.Firefox(executable_path=driver_location_ff)
        #self.driver=webdriver.Ie(executable_path=driver_location_ie)

    def anybrowserlaunch(self):
        self.driver.get("https://selenium.dev/")
        time.sleep(2)
        self.driver.maximize_window()
        #self.driver.minimize_window()
        #time.sleep(2)
        #self.driver.set_window_size(100,200)
        #time.sleep(2)
        #self.driver.set_window_position(150,250)
        #time.sleep(2)
        #self.driver.back()
        #time.sleep(2)
        #self.driver.forward()
        #time.sleep(2)
        #self.driver.refresh()
        time.sleep(2)
        pagesource=self.driver.page_source
        print("Obtained page source is " + pagesource)
        url=self.driver.current_url
        print("Obtained current URL on the page is " + url)
        title=self.driver.title
        print("Obtained current title on the page is " + title)
        time.sleep(2)

        self.driver.close()

def main():
    obj1 = browserlaunch()
    obj1.anybrowserlaunch()

if __name__ == '__main__':
    main()