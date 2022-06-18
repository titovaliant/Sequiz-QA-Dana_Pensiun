from selenium import webdriver
from pageObject.Route import sourceURL
from utilities.readProperties import ReadConfig
from utilities.dataLog import Log_Data
from selenium.webdriver.common.by import By
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
UsiaKini2= ReadConfig.getUsiaKini2()
UsiaPensiun2= ReadConfig.getUsiaPensiun2()

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

#=========================================================================================
# TESTCASE INVALID 1 : Kalkulator Keuangan - Data Personal PAGE - No Penghasilan Input
#=========================================================================================

def test1_INVALID_Data_Personal_Page(driver):
        log.info("=== Test_1_INVALID_Data_Personal_Page ===")

        DanaPensiun = sourceURL(driver)
        DanaPensiun.DanaPensiun_Page()
        DanaPensiun.Button_Data_Personal()
        time.sleep(2)
        
        check= driver.find_element(By.ID, "calc_type3-error").text
        if "Bagian ini wajib diisi." in check :
            assert True
            log.info("=== test 1_INVALID_Data_Personal_Page: PASS")
            driver.save_screenshot(".\\Screenshots/Invalid\\" + "test 1_INVALID_Data_Personal_Page[PASS].png")
        else:
            log.error("=== test 1_INVALID_Data_Personal_Page: FAIL")
            driver.save_screenshot(".\\Screenshots/Invalid\\" + "test 1_INVALID_Data_Personal_Page[FAIL].png")
            assert False 

        
#=========================================================================================
# TESTCASE INVALID 2 : Kalkulator Keuangan - Umur Anda section - Selisih 0 tahun
#=========================================================================================

def test2_INVALID_Umur_Anda_Page(driver):
        log.info("=== Test_2_INVALID_Umur_Anda_Page ===")

        DanaPensiun = sourceURL(driver)
        DanaPensiun.DanaPensiun_Page()
        DanaPensiun.setDataPersonal(penghasilan, inflasi)
        DanaPensiun.Button_Data_Personal()
        time.sleep(2)
        DanaPensiun.Button_Umur_Anda()
        time.sleep(2)

        check= driver.find_element(By.CSS_SELECTOR, "div[class='body-text-2 text-red'] p").text
        if check=="Selisih tahun hingga usia pensiun tidak boleh 0 tahun" :
            assert True
            log.info("=== test 2_INVALID_Umur_Anda_Page: PASS")
            driver.save_screenshot(".\\Screenshots/Invalid\\" + "test 2_INVALID_Umur_Anda_Page[PASS].png")
        else:
            log.error("=== test 2_INVALID_Umur_Anda_Page: FAIL")
            driver.save_screenshot(".\\Screenshots/Invalid\\" + "test 2_INVALID_Umur_Anda_Page[FAIL].png")
            assert False  

#=========================================================================================
# TESTCASE INVALID 3 : Kalkulator Keuangan - Umur Anda section - Usia Pensiun lebih muda
#=========================================================================================

def test3_INVALID_Umur_Pensiun_Page(driver):
        log.info("=== Test_3_INVALID_Umur_Pensiun_Page ===")

        DanaPensiun = sourceURL(driver)
        DanaPensiun.DanaPensiun_Page()
        DanaPensiun.setDataPersonal(penghasilan, inflasi)
        DanaPensiun.Button_Data_Personal()
        time.sleep(2)
        DanaPensiun.setUmurAnda(UsiaKini2, UsiaPensiun2)
        DanaPensiun.Button_Umur_Anda()
        time.sleep(2)
        
        check= driver.find_element(By.CSS_SELECTOR, "div[class='body-text-2 text-red'] p").text
        if check=="Usia pensiun tidak boleh kurang dari usia Anda" :
            assert True
            log.info("=== test 3_INVALID_Umur_Pensiun_Page: PASS")
            driver.save_screenshot(".\\Screenshots/Invalid\\" + "test 3_INVALID_Umur_Pensiun_Page[PASS].png")
        else:
            log.error("=== test 3_INVALID_Umur_Pensiun_Page: FAIL")
            driver.save_screenshot(".\\Screenshots/Invalid\\" + "test 3_INVALID_Umur_Pensiun_Page[FAIL].png")
            assert False 

#=========================================================================================
# TESTCASE INVALID 4 : Kalkulator Keuangan - Gaya Rasio section - Bernilai kurang dari 75
#=========================================================================================

def test4_INVALID_Gaya_Rasio_Page(driver):
        log.info("=== Test_4_INVALID_Gaya_Rasio_Page ===")

        DanaPensiun = sourceURL(driver)
        DanaPensiun.DanaPensiun_Page()
        DanaPensiun.setDataPersonal(penghasilan, inflasi)
        DanaPensiun.Button_Data_Personal()
        DanaPensiun.setUmurAnda(UsiaKini, UsiaPensiun)
        DanaPensiun.Button_Umur_Anda()
        time.sleep(1)
        DanaPensiun.setGayaRasio_invalid()
        time.sleep(2)

        check= driver.find_element(By.CSS_SELECTOR, "#ratioInput-error").text
        if "Mohon mengisi nilai lebih dari" in check:
            assert True
            log.info("=== test 4_INVALID_Gaya_Rasio_Page: PASS")
            driver.save_screenshot(".\\Screenshots/Invalid\\" + "test 4_INVALID_Gaya_Rasio_Page[PASS].png")
        else:
            log.error("=== test 4_INVALID_Gaya_Rasio_Page: FAIL")
            driver.save_screenshot(".\\Screenshots/Invalid\\" + "test 4_INVALID_Gaya_Rasio_Page[FAIL].png")
            assert False 

#=========================================================================================
# TESTCASE INVALID 5 : Kalkulator Keuangan - Gaya Rasio section - Bernilai lebih dari 75
#=========================================================================================

def test5_INVALID_Gaya_Rasio_Page(driver):
        log.info("=== Test_5_INVALID_Gaya_Rasio_Page ===")

        DanaPensiun = sourceURL(driver)
        DanaPensiun.DanaPensiun_Page()
        DanaPensiun.setDataPersonal(penghasilan, inflasi)
        DanaPensiun.Button_Data_Personal()
        DanaPensiun.setUmurAnda(UsiaKini, UsiaPensiun)
        DanaPensiun.Button_Umur_Anda()
        time.sleep(1)
        DanaPensiun.setGayaRasio_invalid2()
        time.sleep(2)

        check= driver.find_element(By.CSS_SELECTOR, "#ratioInput-error").text
        if "Mohon mengisi nilai kurang dari atau sama dengan 125" in check:
            assert True
            log.info("=== test 5_INVALID_Gaya_Rasio_Page: PASS")
            driver.save_screenshot(".\\Screenshots/Invalid\\" + "test 5_INVALID_Gaya_Rasio_Page[PASS].png")
        else:
            log.error("=== test 5_INVALID_Gaya_Rasio_Page: FAIL")
            driver.save_screenshot(".\\Screenshots/Invalid\\" + "test 5_INVALID_Gaya_Rasio_Page[FAIL].png")
            assert False 

#==========================================================================================================
# TESTCASE INVALID 6 : Kalkulator Keuangan - Penghasilan Anda section - Lama Pensiun berniali nol
#==========================================================================================================

def test6_INVALID_Penghasilan_Anda_Page(driver):
        log.info("=== Test_6_INVALID_Penghasilan_Anda_Page ===")

        DanaPensiun = sourceURL(driver)
        DanaPensiun.DanaPensiun_Page()
        DanaPensiun.setDataPersonal(penghasilan, inflasi)
        DanaPensiun.Button_Data_Personal()
        DanaPensiun.setUmurAnda(UsiaKini, UsiaPensiun)
        DanaPensiun.Button_Umur_Anda()
        DanaPensiun.setGayaRasio(GayaRasio)
        DanaPensiun.Button_Gaya_Rasio()
        time.sleep(2)
        DanaPensiun.Button_Penghasilan_Anda()
        time.sleep(2)

        check= driver.find_element(By.CSS_SELECTOR, "div[class='body-text-2 text-red'] p").text
        if check=="Lama pensiun yang di inginkan tidak boleh 0 tahun" :
            assert True
            log.info("=== test 6_INVALID_Penghasilan_Anda_Page: PASS")
            driver.save_screenshot(".\\Screenshots/Invalid\\" + "test 6_INVALID_Penghasilan_Anda_Page[PASS].png")
        else:
            log.error("=== test 6_INVALID_Penghasilan_Anda_Page: FAIL")
            driver.save_screenshot(".\\Screenshots/Invalid\\" + "test 6_INVALID_Penghasilan_Anda_Page[FAIL].png")
            assert False 