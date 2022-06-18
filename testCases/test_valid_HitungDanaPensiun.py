from selenium import webdriver
from pageObject.Route import sourceURL
from utilities.readProperties import ReadConfig
from utilities.dataLog import Log_Data
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

baseURL = ReadConfig.getBaseURL()
log = Log_Data.custom_logger()
penghasilan = ReadConfig.getPenghasilan()
UsiaKini= ReadConfig.getUsiaKini()
UsiaPensiun= ReadConfig.getUsiaPensiun()
inflasi= ReadConfig.getInflasi()
GayaRasio= ReadConfig.getGayaRasio()
LamaPensiun= ReadConfig.getLamaPensiun()
SukuBunga= ReadConfig.getSukuBunga()
email= ReadConfig.getEmail()
phone= ReadConfig.getPhone()
address= ReadConfig.getAddress()

#==================================================================
#       FIXTURE
#==================================================================
@pytest.fixture()
def driver():
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
        driver.quit()

# #===================================================================================================
# # TESTCASE VALID 1 : Kalkulator Keuangan - Hitung Dana Pensiun
# #===================================================================================================

def test1_VALID_Hitung_DanaPensiun(driver):
        log.info("=== Test_1_VALID_HitungDanaPensiun ===")
        DanaPensiun = sourceURL(driver)

        DanaPensiun.DanaPensiun_Page()
        DanaPensiun.setDataPersonal(penghasilan, inflasi)
        DanaPensiun.Button_Data_Personal()

        DanaPensiun.setUmurAnda(UsiaKini, UsiaPensiun)
        DanaPensiun.Button_Umur_Anda()

        DanaPensiun.setGayaRasio(GayaRasio)
        DanaPensiun.Button_Gaya_Rasio()
        
        DanaPensiun.setPenghasilanAnda(LamaPensiun,SukuBunga)
        DanaPensiun.Button_Penghasilan_Anda()

        time.sleep(5)
        page_url = driver.current_url
        if page_url=="https://sequis.co.id/id/financial-calculator/pensiun-result" :
            assert True
            log.info("=== test 1_VALID_HitungDanaPensiun: PASS")
            driver.save_screenshot(".\\Screenshots/Valid\\" + "test 1_VALID_HitungDanaPensiun [PASS].png")
        else:
            log.error("=== test 1_VALID_HitungDanaPensiun: FAIL")
            driver.save_screenshot(".\\Screenshots/Valid\\" + "test 1_VALID_HitungDanaPensiun [FAIL].png")
            assert False  

# #===================================================================================================
# # TESTCASE VALID 2 : Kalkulator Keuangan - Hitung Dana Pensiun - Hitung Ulang
# #===================================================================================================

def test2_VALID_Hitung_Ulang_DanaPensiun(driver):
        log.info("=== Test_2_VALID_Hitung_Ulang_DanaPensiun ===")
        DanaPensiun = sourceURL(driver)

        DanaPensiun.FinalResult_DanaPensiun(penghasilan,inflasi,UsiaKini,UsiaPensiun,GayaRasio,LamaPensiun,SukuBunga)
        time.sleep(2)
        DanaPensiun.Button_Hitung_Ulang()
        page_url = driver.current_url
        time.sleep(2)
        if page_url=="https://sequis.co.id/id/financial-calculator" :
            assert True
            log.info("=== test 2_VALID_Hitung_Ulang_DanaPensiun: PASS")
            driver.save_screenshot(".\\Screenshots/Valid\\" + "test 2_VALID_Hitung_Ulang_DanaPensiun [PASS].png")
        else:
            log.error("=== test 2_VALID_Hitung_Ulang_DanaPensiun: FAIL")
            driver.save_screenshot(".\\Screenshots/Valid\\" + "test 2_VALID_Hitung_Ulang_DanaPensiun [FAIL].png")
            assert False  

# #===================================================================================================
# # TESTCASE VALID 3 : Kalkulator Keuangan - Hitung Dana Pensiun - Dapatkan Hasil
# #===================================================================================================

def test3_VALID_Dapatkan_Hasil_DanaPensiun(driver):
        log.info("=== Test_3_VALID_Dapatkan_Hasil_DanaPensiun ===")
        DanaPensiun = sourceURL(driver)

        DanaPensiun.FinalResult_DanaPensiun(penghasilan,inflasi,UsiaKini,UsiaPensiun,GayaRasio,LamaPensiun,SukuBunga)
        time.sleep(3)
        DanaPensiun.Button_Dapatkan_Hasil()
        DanaPensiun.form_Dapatkan_Hasil(email,phone,address)
        
        if "Sequis - Financial Calculator" in driver.find_element(By.ID, "exampleModalLabel").text :
            assert True
            log.info("=== test 3_VALID_Dapatkan_Hasil_DanaPensiun: PASS")
            driver.save_screenshot(".\\Screenshots/Valid\\" + "test 3_VALID_Dapatkan_Hasil_DanaPensiun [PASS].png")
        else:
            log.error("=== test 3_VALID_Dapatkan_Hasil_DanaPensiun: FAIL")
            driver.save_screenshot(".\\Screenshots/Valid\\" + "test 3_VALID_Dapatkan_Hasil_DanaPensiun [FAIL].png")
            assert False  