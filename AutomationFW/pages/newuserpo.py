from base.seleniumdriver import SeleniumDriver


class NewUserPo(SeleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _firstNameField = "//input[@id='createUserPanel_firstNameField']"
    _lastNameField = "//input[@id='createUserPanel_lastNameField']"
    _emailField = "//input[@id='createUserPanel_emailField']"
    _submitBtn = "//div[@class='components_button submitBtn']"
    _closeBtn = "(//span[text()='Close'])[1]"

    def waitforelement(self):
        self.waitforelementclickable(self._firstNameField,"xpath",60,10)

    def firstNameFieldtxtbx(self,firstname):
        self.senddata(self._firstNameField,"xpath",firstname)

    def lastNameFieldtxtbx(self,lastname):
        self.senddata(self._lastNameField,"xpath",lastname)

    def emailFieldtxtbx(self,email):
        self.senddata(self._emailField,"xpath",email)

    def submitBtn(self):
        self.click(self._submitBtn,"xpath")
    def closeBtn(self):
        self.click(self._closeBtn,"xpath")

    def createnewuser(self,firstname,lastname,email):
        self.waitforelement()
        self.firstNameFieldtxtbx(firstname)
        self.lastNameFieldtxtbx(lastname)
        self.emailFieldtxtbx(email)
        self.submitBtn()
        self.closeBtn()