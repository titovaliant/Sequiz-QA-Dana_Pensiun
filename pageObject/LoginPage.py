from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class sourceURL:
    textbox_penghasilan='calc_type3'
    textbox_inflasi= "//input[@id='inflasiInput']"
    # textbox_username_id='input_email'
    # textbox_password_id='input_password'
    # button_login_id='submit_login'
    # link_logout_linktext='Log out'
    # classname_eye_password= 'MuiIconButton-label'
    # forgot_linktext= 'btn_to-forgot-password'
    # facebook_login= "login_facebook"

    def __init__(self,driver):
        self.driver = driver

    def setDanaPensiun_Page(self):
        self.driver.find_element(By.CSS_SELECTOR, ".block__nav .dropdown-item:nth-child(1) > a").click()
        self.driver.find_element(By.LINK_TEXT, "Dana Pensiun").click()

    def setKalkulatorKeuangan_Page(self):
        self.driver.find_element(By.CSS_SELECTOR, ".jcf-select-opener").click()
        self.driver.find_element(By.NAME, "type").send_keys(Keys.DOWN)
        self.driver.find_element(By.CSS_SELECTOR, ".button-area:nth-child(1) > .button").click()

    def setDataPersonal_Page(self):
        self.driver.find_element(By.CSS_SELECTOR, ".block__nav .dropdown-item:nth-child(1) > a").click()
        self.driver.find_element(By.LINK_TEXT, "Dana Pensiun").click()
        self.driver.find_element(By.CSS_SELECTOR, ".jcf-select-opener").click()
        self.driver.find_element(By.NAME, "type").send_keys(Keys.DOWN)
        self.driver.find_element(By.CSS_SELECTOR, ".button-area:nth-child(1) > .button").click()
  
    def setHitungPenghasilan(self, penghasilan, inflasi):
        self.driver.find_element(By.CSS_SELECTOR, ".jcf-select-opener").click()
        self.driver.find_element(By.NAME, "type").send_keys(Keys.DOWN)
        self.driver.find_element(By.NAME, "type").send_keys(Keys.ENTER)
        self.driver.find_element(By.NAME, (self.textbox_penghasilan)).clear()
        self.driver.find_element(By.NAME, (self.textbox_penghasilan)).send_keys(penghasilan)
        self.driver.find_element(By.XPATH, (self.textbox_inflasi)).clear()
        self.driver.find_element(By.XPATH, (self.textbox_inflasi)).send_keys(inflasi)
    
    def setUmurAnda(self,UsiaKini, UsiaPensiun):
        self.driver.find_element(By.CSS_SELECTOR, "#usiaCurrentInput").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#usiaCurrentInput").send_keys(UsiaKini)
        self.driver.find_element(By.CSS_SELECTOR, "#usiaPensiunInput").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#usiaPensiunInput").send_keys(UsiaPensiun)
        
    def Click_Selanjutnya(self):
        self.driver.find_element(By.XPATH, "//button[@type='button'][normalize-space()='Selanjutnya']").click()

    def Click_Selanjutnya2(self):
        self.driver.find_element(By.XPATH, "//div[@class='button-area text-left button-area--step2']//button[@type='button'][normalize-space()='Selanjutnya']").click()

    def Click_Selanjutnya3(self):
        self.driver.find_element(By.XPATH, "//button[@id='financial-pensiun-step3']").click()

    def setGayaRasio(self,GayaRasio):
        self.driver.find_element(By.CSS_SELECTOR, "#ratioInput").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#ratioInput").send_keys(GayaRasio)

    def setPenghasilanAnda(self,LamaPensiun,SukuBunga):
        self.driver.find_element(By.CSS_SELECTOR, "#pensiunInput").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#pensiunInput").send_keys(LamaPensiun)
        self.driver.find_element(By.CSS_SELECTOR, "#bungaDepositoInput").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#bungaDepositoInput").send_keys(SukuBunga)

    def Click_Selanjutnya3(self):
        self.driver.find_element(By.CSS_SELECTOR, "#financial-pensiun-step4").click()
