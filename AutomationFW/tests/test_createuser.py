import pytest
from pages.loginpo import LoginPo
from pages.homepo import HomePo
from pages.newuserpo import NewUserPo

@pytest.mark.usefixtures("setup","onetimesetup")
class Test_CreateUser:
    @pytest.fixture(autouse=True)
    def classsetup(self):
        self.lp = LoginPo(self.driver)
        self.hp = HomePo(self.driver)
        self.nup = NewUserPo(self.driver)


    @pytest.mark.run(order=1)
    def test_createusersuccessfully(self):
        self.lp.entercredentials("admin","manager")
        self.hp.usersbtn()
        self.hp.newuserbtn()
        self.nup.createnewuser("SomeFirstName","SomeLastName","somelastname@gmail.com")
        self.hp.logoutbtn()
