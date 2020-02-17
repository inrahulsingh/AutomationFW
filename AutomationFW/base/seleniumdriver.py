from selenium.webdriver.common.by import By
import logging
import utilities.customlogger as cl
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from datetime import date

class SeleniumDriver:
    log = cl.customLogger(logLevel=logging.INFO)

    def __init__(self,driver):
        self.driver = driver

    def getBytype(self,locatortype):
        locator = locatortype.lower()
        if locator == "id":
            return By.ID
        elif locator == "name":
            return By.NAME
        elif locator == "linktext":
            return By.LINK_TEXT
        elif locator == "partiallinktext":
            return By.PARTIAL_LINK_TEXT
        elif locator == "css":
            return By.CSS_SELECTOR
        elif locator == "xpath":
            return By.XPATH
        else:
            self.log.error("Please enter the valid locator " +locatortype)
            return False

    def getWebElement(self, locatorvalue, locatortype="xpath/id"):
        element = None
        try:
            bytype = self.getBytype(locatortype)
            element = self.driver.find_element(bytype, locatorvalue)
            self.log.info("Identified element with locator type "+locatortype+" with locator value "+locatorvalue)
        except Exception as e:
            self.log.error("Element not found "+str(e))
            raise Exception
        return element

    def getWebElements(self, locatorvalue, locatortype="xpath/id"):
        listofelements = []
        try:
            bytype = self.getBytype(locatortype)
            listofelements = self.driver.find_elements(bytype, locatorvalue)
            self.log.info("Identified element with locator type "+locatortype+" with locator value "+locatorvalue)
        except Exception as e:
            self.log.error("Element not found "+str(e))
        return listofelements

    def geturl(self,url):
        self.driver.get(url)
        self.log.info("Entered url "+url)

    def closewindow(self):
        self.log.info("Window closed")
        self.driver.close()

    def quitwindow(self):
        self.log.info("All window closed")
        self.driver.quit()

    def maximizewindow(self):
        self.log.info("Window maximized")
        self.driver.maximize_window()

    def minimizewindow(self):
        self.log.info("Window minimized")
        self.driver.minimize_window()

    def setwindowsizeorposition(self,x,y,alter="size/position"):
        if alter == "size":
            self.driver.set_window_size(x,y)
            self.log.info("Window size set to "+x+" and "+y)
        elif alter == "position":
            self.driver.set_window_position(x,y)
            self.log.info("Window position set to "+x+" and "+y)
        else:
            self.log.error("Please enter valid size or position")

    def browsernatives(self, native="back"):
        if native == "back":
            self.driver.back()
            self.log.info("Clicked on browser native back")
        elif native == "forward":
            self.driver.forward()
            self.log.info("Clicked on browser native forward")
        elif native == "refresh":
            self.driver.refresh()
            self.log.info("Clicked on browser native refresh")
        else:
            self.log.error("Please enter valid native list back/forward/refresh "+native)

    def getsourcecode(self):
        pagesource = self.driver.page_source
        self.log.info("Obtained page source is "+pagesource)
        return pagesource

    def getcurrenturl(self):
        current_uri = self.driver.current_url
        self.log.info("Obtained current URL is "+current_uri)
        return current_uri

    def gettitle(self):
        title = self.driver.title
        self.log.info("Obtained current title is "+title)
        return title

    def click(self,locatorvalue,locatortype):
        try:
            element = self.getWebElement(locatorvalue,locatortype)
            element.click()
            self.log.info("Click on webelement with locatortype "+locatortype+ "locator value "+locatorvalue)
        except Exception as e:
            self.log.error("Unable to click on webelement with locatortype "+locatortype+ "locator value "+locatorvalue+" "+str(e))
            raise Exception

    def senddata(self,locatorvalue,locatortype,data):
        try:
            element = self.getWebElement(locatorvalue,locatortype)
            element.send_keys(data)
            self.log.info("Entered data on webelement with locatortype "+locatortype+ "locator value "+locatorvalue+" "+"data = "+data)
        except Exception as e:
            self.log.error("Unable to enter data on webelement with locatortype " + locatortype + "locator value " + locatorvalue + " " + str(e))
            raise Exception

    def getTest(self,locatorvalue,locatortype):
        text=None
        try:
            element=self.getWebElement(locatorvalue,locatortype)
            text=element.text
            self.log.info("Got text from webelement with locatortype "+locatortype+ "locator value "+locatorvalue+" "+"text = "+text)
        except Exception as e:
            self.log.error("Unable to get text from webelement with locatortype " + locatortype + "locator value " + locatorvalue + " " + str(e))
        return text

    def selectoptionindrpdwn(self,locatorvalue,locatortype,option="India"):
        try:
            element = self.getWebElement(locatorvalue,locatortype)
            sel = Select(element)
            sel.select_by_visible_text(option)
            self.log.info("Selected text from drop down with locatortype "+locatortype+ "locator value "+locatorvalue+" "+"option = "+option)
        except Exception as e:
            self.log.error("Unable to select option from drop down with locatortype " + locatortype + "locator value " + locatorvalue + " " + str(e))

    def deselectoptionindrpdwn(self,locatorvalue,locatortype,option="India"):
        try:
            element = self.getWebElement(locatorvalue,locatortype)
            sel = Select(element)
            sel.deselect_by_visible_text(option)
            self.log.info("Deselected text from drop down with locatortype "+locatortype+ "locator value "+locatorvalue+" "+"option = "+option)
        except Exception as e:
            self.log.error("Unable to deselect option from drop down with locatortype " + locatortype + "locator value " + locatorvalue + " " + str(e))

    def deselectall(self,locatorvalue,locatortype):
        try:
            element = self.getWebElement(locatorvalue,locatortype)
            sel = Select(element)
            sel.deselect_all()
            self.log.info("Deselected all options from drop down with locatortype "+locatortype+ "locator value "+locatorvalue)
        except Exception as e:
            self.log.error("Unable to deselect all options from drop down with locatortype " + locatortype + "locator value " + locatorvalue + " " + str(e))

    def getfirstselectedoption(self,locatorvalue,locatortype):
        text=None
        try:
            element = self.getWebElement(locatorvalue,locatortype)
            sel = Select(element)
            text = sel.first_selected_option.text
            self.log.info("Got first selected option from drop down with locatortype "+locatortype+ "locator value "+locatorvalue+" "+"text = "+text)
        except Exception as e:
            self.log.error("Unable to get first selected option from drop down with locatortype " + locatortype + "locator value " + locatorvalue + " " + str(e))
        return text

    def mousehover(self,locatorvalue,locatortype):
        try:
            act = ActionChains(self.driver)
            element = self.getWebElement(locatorvalue,locatortype)
            act.move_to_element(element).perform()
            self.log.info("Mouse hovered on webelement with locatortype "+locatortype+ "locator value "+locatorvalue)
        except Exception as e:
            self.log.error("Unable to mouse hover on web element with locatortype " + locatortype + "locator value " + locatorvalue + " " + str(e))

    def leftmouseclick(self,locatorvalue,locatortype):
        try:
            act = ActionChains(self.driver)
            element = self.getWebElement(locatorvalue,locatortype)
            act.move_to_element(element).click().perform()
            self.log.info("Mouse hovered on webelement and left clicked with locatortype "+locatortype+ "locator value "+locatorvalue)
        except Exception as e:
            self.log.error("Unable to mouse hover on web element and left click with locatortype " + locatortype + "locator value " + locatorvalue + " " + str(e))

    def scrolltoptobottom(self,x=0,y=1000):
        self.driver.execute_script("window.scrollBy("+str(x)+","+str(y)+");")
        self.log.info("Scrolled the page from top to bottom "+str(x)+" "+str(y))

    def scrollbottomtotop(self,x=0,y=-500):
        self.driver.execute_script("window.scrollBy("+str(x)+","+str(y)+");")
        self.log.info("Scrolled the page from bottom to top "+str(x)+" "+str(y))

    def switchtoframe(self,id=None,index=0):
        try:
            if id is not None:
                self.driver.switch_to.frame(id)
                self.log.info("Switched to the frame with id "+str(id))
            else:
                self.driver.switch_to.frame(index)
                self.log.info("Switched to the frame with index "+str(index))
        except Exception as e:
            self.log.error("Unable to switch to frame "+str(e))

    def switchtoparentframe(self):
        self.driver.switch_to.parent_frame()

    def waitforelementclickable(self,locatorvalue,locatortype,time=60,poll=10):
        try:
            bytype = self.getBytype(locatortype)
            wait = WebDriverWait(self.driver, time, poll_frequency=poll, ignored_exceptions=[NoSuchElementException,ElementNotInteractableException])
            wait.until(EC.element_to_be_clickable((bytype, locatorvalue)))
            self.log.info("Waited for element to be clicked")
        except Exception as e:
            self.log.error("Waited for element to be clicked time= "+str(time)+" but unsuccessful")

    def waitforelementtobevisible(self,locatorvalue,locatortype,time=60,poll=10):
        try:
            bytype = self.getBytype(locatortype)
            wait = WebDriverWait(self.driver, time, poll_frequency=poll, ignored_exceptions=[NoSuchElementException, ElementNotInteractableException])
            wait.until(EC.visibility_of((bytype, locatorvalue)))
            self.log.info("Waited for element to be visible")
        except Exception as e:
            self.log.error("Waited for element to be visible time= "+str(time)+" but unsuccessful")

    def elementisselected(self, locatorvalue, locatortype):
        element = self.getWebElement(locatorvalue, locatortype)
        return element.is_selected()

    def elementisenabled(self, locatorvalue, locatortype):
        element = self.getWebElement(locatorvalue, locatortype)
        return element.is_enabled()

    def elementisdisplayed(self, locatorvalue, locatortype):
        element = self.getWebElement(locatorvalue, locatortype)
        return element.is_displayed()

    def getcurrentwindowid(self):
        currentwindowid = self.driver.current_window_handle
        self.log.info("Obtained current window id")
        return currentwindowid

    def getallwindowids(self):
        allwindowids = self.driver.window_handles
        self.log.info("Obtained all window ids")
        return allwindowids

    def switchtowindow(self,windowid):
        self.driver.switch_to.window(windowid)
        self.log.info("Switched into window with window id "+windowid)

    def switchtoJSpopup(self,action="accept/dismiss"):
        if action == "accept":
            self.driver.switch_to.alert.accept()
            self.log.info("Clicked on OK button")
        elif action == "dismiss":
            self.driver.switch_to.alert.dismiss()
            self.log.info("Clicked on Cancel button")
        else:
            self.log.error("Please provide the valid action")

    def gettextfromJSpopup(self):
        return self.driver.switch_to.alert.text

    def getcurrentdate(self):
        today = date.today()
        currentdate = today.strftime("%d")
        self.log.info("Current date is "+currentdate)
        return currentdate