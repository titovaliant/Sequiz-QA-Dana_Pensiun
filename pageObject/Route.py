from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class sourceURL:
    textbox_penghasilan='calc_type3'
    textbox_inflasi= "//input[@id='inflasiInput']"
    textbox_usia_kini= "#usiaCurrentInput"
    textbox_usia_pensiun= "#usiaPensiunInput"
    textbox_gaya_rasio= "#ratioInput"
    textbox_lama_pensiun= "#pensiunInput"
    textbox_suku_bunga=   "#bungaDepositoInput"

    def __init__(self,driver):
        self.driver = driver

# #=========================================================================================
# # TESTCASE VALID KEYWORD
# #=========================================================================================

    def gotoDanaPensiun_Page(self):
        self.driver.find_element(By.CSS_SELECTOR, ".block__nav .dropdown-item:nth-child(1) > a").click()
        self.driver.find_element(By.LINK_TEXT, "Dana Pensiun").click()

    def gotoKalkulatorKeuangan_Page(self):
        self.driver.find_element(By.CSS_SELECTOR, ".jcf-select-opener").click()
        s=self.driver.find_element(By.XPATH, "//div[@class='jcf-select-drop-content']/span")
        s.click()
        self.driver.find_element(By.CSS_SELECTOR, ".button-area:nth-child(1) > .button").click()

    def DanaPensiun_Page(self):
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".block__nav .dropdown-item:nth-child(1) > a").click()
        self.driver.find_element(By.LINK_TEXT, "Dana Pensiun").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".jcf-select-opener").click()
        self.driver.find_element(By.XPATH, "//div[@class='jcf-select-drop-content']/span").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".button-area:nth-child(1) > .button").click()
  
    def setDataPersonal(self, penghasilan, inflasi):
        self.driver.find_element(By.NAME, (self.textbox_penghasilan)).clear()
        self.driver.find_element(By.NAME, (self.textbox_penghasilan)).send_keys(penghasilan)
        self.driver.find_element(By.XPATH, (self.textbox_inflasi)).clear()
        self.driver.find_element(By.XPATH, (self.textbox_inflasi)).send_keys(inflasi)
        time.sleep(1)

    def setUmurAnda(self,UsiaKini, UsiaPensiun):
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_usia_kini)).clear()
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_usia_kini)).send_keys(UsiaKini)
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_usia_pensiun)).clear()
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_usia_pensiun)).send_keys(UsiaPensiun)
        time.sleep(1)

    def setGayaRasio(self,GayaRasio):
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_gaya_rasio)).clear()
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_gaya_rasio)).send_keys(GayaRasio)
        time.sleep(1)
    
    def setPenghasilanAnda(self,LamaPensiun,SukuBunga):
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_lama_pensiun)).clear()
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_lama_pensiun)).send_keys(LamaPensiun)
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_suku_bunga)).clear()
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_suku_bunga)).send_keys(SukuBunga)
        time.sleep(1)   
        
    def Button_Data_Personal(self):
        self.driver.find_element(By.XPATH,'//button[normalize-space()="Selanjutnya"]').click()

    def Button_Umur_Anda(self):
        self.driver.find_element(By.CSS_SELECTOR, "div[class='button-area text-left button-area--step2'] button[type='button']").click()

    def Button_Gaya_Rasio(self):
        self.driver.find_element(By.CSS_SELECTOR, "#financial-pensiun-step3").click()

    def Button_Penghasilan_Anda(self):
        self.driver.find_element(By.CSS_SELECTOR, "#financial-pensiun-step4").click()
    
    def Button_Hitung_Ulang(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Hitung Ulang']").click()

    def Button_Dapatkan_Hasil(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Dapatkan Hasil']").click()

    def FinalResult_DanaPensiun(self,penghasilan,inflasi,UsiaKini,UsiaPensiun,GayaRasio,LamaPensiun,SukuBunga):
        self.driver.find_element(By.CSS_SELECTOR, ".block__nav .dropdown-item:nth-child(1) > a").click()
        self.driver.find_element(By.LINK_TEXT, "Dana Pensiun").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".jcf-select-opener").click()
        self.driver.find_element(By.XPATH, "//div[@class='jcf-select-drop-content']/span").click()
        
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".button-area:nth-child(1) > .button").click()

        time.sleep(2)
        self.driver.find_element(By.NAME, (self.textbox_penghasilan)).send_keys(penghasilan)
        self.driver.find_element(By.XPATH, (self.textbox_inflasi)).clear()
        self.driver.find_element(By.XPATH, (self.textbox_inflasi)).send_keys(inflasi)
        self.driver.find_element(By.XPATH,'//button[normalize-space()="Selanjutnya"]').click()

        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_usia_kini)).clear()
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_usia_kini)).send_keys(UsiaKini)
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_usia_pensiun)).clear()
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_usia_pensiun)).send_keys(UsiaPensiun)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "div[class='button-area text-left button-area--step2'] button[type='button']").click()
        
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_gaya_rasio)).clear()
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_gaya_rasio)).send_keys(GayaRasio)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#financial-pensiun-step3").click()
        
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_lama_pensiun)).clear()
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_lama_pensiun)).send_keys(LamaPensiun)
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_suku_bunga)).clear()
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_suku_bunga)).send_keys(SukuBunga)
        time.sleep(1) 
        self.driver.find_element(By.CSS_SELECTOR, "#financial-pensiun-step4").click()

    def form_Dapatkan_Hasil(self, email, phone, address):
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "phone").send_keys(phone)
        self.driver.find_element(By.ID, "address").send_keys(address)
        self.driver.find_element(By.XPATH, "//select[@id='province']").click()
        dropdown = self.driver.find_element(By.NAME, "province")
        dropdown.find_element(By.XPATH, "//option[. = 'JAWA BARAT']").click()
        self.driver.find_element(By.XPATH, "//select[@id='city']").click()
        dropdown = self.driver.find_element(By.NAME, "city")
        dropdown.find_element(By.XPATH, "//option[. = 'BANDUNG']").click()
        self.driver.find_element(By.ID, "bersedia").click()
        self.driver.find_element(By.ID, "save-financial").click()
        time.sleep(3)


# #=========================================================================================
# # TESTCASE INVALID KEYWORD
# #=========================================================================================

    def setGayaRasio_invalid(self):
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_gaya_rasio)).clear()
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_gaya_rasio)).send_keys(0)

    def setGayaRasio_invalid2(self):
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_gaya_rasio)).clear()
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_gaya_rasio)).send_keys(12500)

    def setPenghasilanAnda_invalid(self):
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_lama_pensiun)).clear()
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_lama_pensiun)).send_keys(2)