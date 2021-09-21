from selenium import webdriver
from Config import config
from shutdown import Shutdown
import time


class Browser:

    def Show(self):
        self.run = True
        time_ = 0
        if bool(self.config_['Login']) == True:
            self.Login()
        self.CheckLoad()
        self.driver.get(self.config_['showurl'])
        # 3600 seconds == 1 Houer. It convert houers in seconds
        while self.run == self.run:
            if bool(self.config_['refresh']) == True and time_ > (3600*float(self.config_['refreshtime'])):
                self.Reload()
                time_ = 0
            time.sleep(60)
            time_ += 60
        self.driver.get('about:blank')

    def StopBrowser(self):
        self.driver.close()
        self.driver.quit()

    def GetTitle(self):
        return self.driver.title

    def Shutdown(self):
        Shutdown(self.config_['shutdownurl'])

    def StartBrowser(self):
        op = webdriver.ChromeOptions()
        op.add_argument("--start-maximized")
        op.add_argument("--kiosk")
        pref = {"credentials_enable_serive": False,
                "profile.password_manager_enable": False}
        op.add_experimental_option("prefs", pref)
        op.add_argument("--disable-infobars")
        op.add_experimental_option("excludeSwitches", ['enable-automation'])
        op.add_argument("--disable-web-security")
        op.add_argument("--autoplay-policy=no-user-gesture-required")
        #op.set_capability('acceptInsecureCerts', True)
        # op.add_argument('--ignore-certificate-errors')
        # Enabel this tow lines if you use an unverifiyed certificate
        if self.driverpath == "None":
            self.driver = webdriver.Chrome(
                chrome_options=op)
        else:
            self.driver = webdriver.Chrome(
                chrome_options=op, executable_path=self.driverpath)
        self.driver.get("about:blank")

    def CheckLoad(self):
        try:
            br = self.driver.find_element_by_tag_name('html')
        except:
            time.sleep(2.50)
            self.CheckLoad()

    def AcceptCokkies(self):
        try:
            cookie_fild = self.driver.find_element_by_class_name(
                self.config_['cookie-banner'])
            cookie_fild.click()
        except:
            time.sleep(0.01)

    def Login(self):
        self.driver.get(self.config_['loginurl'])
        time.sleep(2)
        self.CheckLoad()
        if self.GetTitle() == self.config_['Titel-Login']:
            usernamne_fild = self.driver.find_element_by_name(
                self.config_['box-password'])
            usernamne_fild.send_keys(self.config_['username'])
            password_fild = self.driver.find_element_by_name(
                self.config_['box-username'])
            password_fild.send_keys(self.config_['password'])
            password_fild.submit()
            time.sleep(2)
            self.CheckLoad()
            self.run = True
        else:
            print("Cant get loggin page! titel should be: " +
                  self.config_['Titel-Login']+" Titel is: "+self.GetTitle())
            self.StopBrowser()
            exit()

    def Reload(self):
        self.driver.refresh()
        try:
            self.AcceptCokkies()
        except:
            time.sleep(0.01)

    def __init__(self, driverpath="None"):
        # Load config
        # The Sleep Seconds after an aktion
        self.driverpath = driverpath
        self.run = False
        self.waitplus = 2
        self.config_ = config().JsonValues
        self.shutdown = False
        if(self.config_['shutdown'] == "True"):
            self.Shutdown()
            self.shutdown = True
        print("Start Browser")
        self.StartBrowser()
        time.sleep(float(self.config_['boot-delay']))
