import pytest
from pages.loginpo import LoginPo
from pages.homepo import HomePo

@pytest.mark.usefixtures("setup","onetimesetup")
class Test_Login:
    @pytest.fixture(autouse=True)
    def classsetup(self):
        self.lp = LoginPo(self.driver)
        self.hp = HomePo(self.driver)
        print("I am in classsetup function executing before test case")

    @pytest.mark.run(order=1)
    def test_validatesuccessfulllogin(self):
        #self.lp.usernametxtbx("admin")
        #self.lp.pwdtxtbx("manager")
        #self.lp.keepmeloggedinchkbx()
        #self.lp.loginbtn()
        self.lp.entercredentials("admin","manager")
        self.hp.logoutbtn()
