from base.seleniumdriver import SeleniumDriver


class HomePo(SeleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    _logoutlink = "logoutLink"
    _usersbtn = "//div[@id='container_users']"
    _newuserbtn = "//div[contains(text(),'New User')]"
    _testuser = "//span[contains(text(),'SomeLastName, SomeFirstName')]"



    def logoutbtn(self):
        self.click(self._logoutlink,"id")

    def usersbtn(self):
        self.click(self._usersbtn,"xpath")

    def newuserbtn(self):
        self.click(self._newuserbtn,"xpath")

    def testuserbtn(self):
        self.click(self._testuser,"xpath")