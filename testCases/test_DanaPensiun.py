from selenium import webdriver
from pageObject.LoginPage import sourceURL
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
#===============================================================================
# TESTCASE VALID 1 : Landing Page
#===============================================================================

# def test1_Landing_Page(driver):
#         log.info("=== Test_1_Landing_Page ===")
#         check = driver.title
#         # time.sleep(2)
#         if check == "Sequis: Asuransi Jiwa | Asuransi Kesehatan | Investasi di Indonesia - Sequis - Your Better Tomorrow":
#             if "Kebutuhan Apa yang Anda Cari?" in driver.find_element(By.CLASS_NAME, "heading").text :
#                 assert True
#                 log.info("=== Test 1_Landing_Page: PASS")
#         else:
#             log.error("=== Test 1_Landing_Page: FAIL")
#             driver.save_screenshot(".\\Screenshots\\" + "test1_Landing_Page.png")
#             assert False

#===============================================================================
# TESTCASE VALID 2 : Choose Dana Pensiun Option, navigate to Dana Pensiun Page
#===============================================================================

# def test2_Dana_Pensiun_Page(driver):
#         log.info("=== Test_2_Dana_Pensiun_Page ===")
#         # time.sleep(2)
#         driver.find_element(By.CSS_SELECTOR, ".block__nav .dropdown-item:nth-child(1) > a").click()
#         driver.find_element(By.LINK_TEXT, "Dana Pensiun").click()
#         # time.sleep(2)

#         page_title = driver.title
#         page_url = driver.current_url
#         if page_title=='Asuransi Jiwa | Perencanaan Dana Pensiun dari Sequis - Sequis - Your Better Tomorrow':
#             if page_url== 'https://sequis.co.id/id/asuransi-jiwa/individu/dana-pensiun':
#                 assert True
#                 log.info("=== test 2_Dana_Pensiun_Page: PASS")
#         else:
#             log.error("=== test 2_Dana_Pensiun_Page: FAIL")
#             driver.save_screenshot(".\\Screenshots\\" + "test 2_SolutionFinder_Page.png")
#             assert False 

# #=====================================================================================
# # TESTCASE VALID 3 : Choose Dana Pensiun Option, navigate to Kalkulator Keuangan Page
# #=====================================================================================

# def test3_Kalkulator_Keuangan_Page(driver):
#         log.info("=== Test_3_Kalkulator_Keuangan_Page ===")

#         DanaPensiun = sourceURL(driver)
#         DanaPensiun.setDanaPensiun_Page()
#         DanaPensiun.setKalkulatorKeuangan_Page()

#         page_title = driver.title
#         page_url = driver.current_url
#         if page_title=='Kalkulator Keuangan - Sequis - Your Better Tomorrow':
#             if page_url== 'https://sequis.co.id/id/financial-calculator':
#                 assert True
#                 log.info("=== test 3_Kalkulator_Keuangan_Page: PASS")
#         else:
#             log.error("=== test 3_Kalkulator_Keuangan_Page: FAIL")
#             driver.save_screenshot(".\\Screenshots\\" + "test 2_SolutionFinder_Page.png")
#             assert False 

# #=========================================================================================
# # TESTCASE VALID 4 : Kalkulator Keuangan - Data Personal
# #=========================================================================================

# def test4_Data_Personal_Page(driver):
#         log.info("=== Test_4_Data_Personal_Page ===")

#         DanaPensiun = sourceURL(driver)
#         DanaPensiun.setDataPersonal_Page()
#         DanaPensiun.setHitungPenghasilan(penghasilan, inflasi)
#         DanaPensiun.Click_Selanjutnya()

#         check= driver.find_element(By.CSS_SELECTOR, "section[class='body-step body-step--2 current'] h3").text
#         if check=="Silahkan isi data Anda dibawah ini" :
#             assert True
#             log.info("=== test 4_Data_Personal_Page: PASS")
#         else:
#             log.error("=== test 4_Data_Personal_Page: FAIL")
#             driver.save_screenshot(".\\Screenshots\\" + "test 4_Data_Personal_Page.png")
#             assert False 

# #===================================================================================================
# # TESTCASE VALID 5 : Kalkulator Keuangan - Umur Anda
# #===================================================================================================

# def test5_Umur_Anda_Page(driver):
#         log.info("=== Test_5_Umur_Anda_Page ===")

#         DanaPensiun = sourceURL(driver)
#         DanaPensiun.setDataPersonal_Page()
#         DanaPensiun.setHitungPenghasilan(penghasilan, inflasi)
#         DanaPensiun.Click_Selanjutnya()
#         DanaPensiun.setUmurAnda(UsiaKini, UsiaPensiun)
#         DanaPensiun.Click_Selanjutnya2()

#         check= driver.find_element(By.CSS_SELECTOR, "section[class='body-step body-step--3 current'] h3").text
#         if check=="Gaya hidup yang Anda inginkan dihari tua" :
#             assert True
#             log.info("=== test 5_Umur_Anda_Page: PASS")
#         else:
#             log.error("=== test 5_Umur_Anda_Page: FAIL")
#             driver.save_screenshot(".\\Screenshots\\" + "test 5_Umur_Anda_Page.png")
#             assert False  

# #===================================================================================================
# # TESTCASE VALID 6 : Kalkulator Keuangan - Gaya Rasio
# #===================================================================================================

# def test6_Gaya_Rasio_Page(driver):
#         log.info("=== Test_6_Gaya_Rasio_Page ===")

#         DanaPensiun = sourceURL(driver)
#         DanaPensiun.setDataPersonal_Page()
#         DanaPensiun.setHitungPenghasilan(penghasilan, inflasi)
#         DanaPensiun.Click_Selanjutnya()
#         DanaPensiun.setUmurAnda(UsiaKini, UsiaPensiun)
#         DanaPensiun.Click_Selanjutnya2()
#         DanaPensiun.setGayaRasio(GayaRasio)
#         DanaPensiun.Click_Selanjutnya3()

#         check= driver.find_element(By.CSS_SELECTOR, "section[class='body-step body-step--4 current'] h3").text
#         if check=="Jumlah pemasukan saat mencapai usia pensiun yang Anda inginkan" :
#             assert True
#             log.info("=== test 6_Gaya_Rasio_Page: PASS")
#         else:
#             log.error("=== test 6_Gaya_Rasio_Page: FAIL")
#             driver.save_screenshot(".\\Screenshots\\" + "test 6_Gaya_Rasio_Page.png")
#             assert False  

# #===================================================================================================
# # TESTCASE VALID 7 : Kalkulator Keuangan - Penghasilan Anda
# #===================================================================================================

def test7_Penghasilan_Anda_Page(driver):
        log.info("=== Test_7_Penghasilan_Anda_Page ===")

        DanaPensiun = sourceURL(driver)
        DanaPensiun.setDataPersonal_Page()
        DanaPensiun.setHitungPenghasilan(penghasilan, inflasi)
        DanaPensiun.Click_Selanjutnya()
        DanaPensiun.setUmurAnda(UsiaKini, UsiaPensiun)
        DanaPensiun.Click_Selanjutnya2()
        DanaPensiun.setGayaRasio(GayaRasio)
        DanaPensiun.Click_Selanjutnya3()
        DanaPensiun.setPenghasilanAnda(LamaPensiun,SukuBunga)
        DanaPensiun.Click_Selanjutnya3()

        check= driver.find_element(By.CSS_SELECTOR, "div[class='visible-xs'] h2").text
        if check=="Hasil Perhitungan Anda" :
            assert True
            log.info("=== test 7_Penghasilan_Anda_Page: PASS")
        else:
            log.error("=== test 7_Penghasilan_Anda_Page: FAIL")
            driver.save_screenshot(".\\Screenshots\\" + "test 7_Penghasilan_Anda_Page.png")
            assert False  
            