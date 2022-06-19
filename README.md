## Automation-Testing [Sequis - WEB Tester]
Automation Using Selenium Hybrid Framework
(Python, Selenium, PyTest, Page Object Model, HTML Reports)

Prepared by:
**Tito Valiant Muhammad - Tester Engineer Candidate**

### Concepts

1). Built-in Frameworks
    
    pytest-selenium

2). Customized/User defined frameworks

    Hybrid driven framework

## 1. A detailed test cases 
You can see all the Manual Testing Documentation by following this link below:

<a href="https://docs.google.com/spreadsheets/d/1hgLmoNVobe1XqgH3Cte2qNL4rGBdz0infacAozNEuqk/edit?usp=sharing">TestCases-Populix-LoginPage-Tito</a>

## 2. Requirements and Tools

In order to utilise this project you need to have the following installed locally:

* Python
* Chrome and Chromedriver
* Selenium : Selenium Webdriver
    
    On Terminal use this command (inside the Sequis folder):
    ```
    $ pip install selenium
    ```
* Pytest : Python UnitTest framework
    
    On Terminal use this command (inside the Sequis folder):
    ```
    $ pip install -U pytest
    ```
* pytest-html : PyTest HTML Reports
    
    On Terminal use this command (inside the Sequis folder):
    ```
    $ pip install pytest-html
    ```
    ```
    $ pip install pytest-metadata
    ```
* Virtual Env Python:
    
    On Terminal use this command (inside the Sequis folder):
    ```
    $ pip install virtualenv`
    ```
## 3. Reporting

Reports for each module are written into their respective `/Reports` directories after a successful run with HTML Reports format.

Log tests result in a .log report for each feature/testCases in folder `/Logs/testing_data.log`.

In the case of test failures, a screen-shot of the UI at the point of failure is embedded into the report in folder `/Screenshots`.

## 4. Usage/How to Run

The project is broken into separate Folder and Package.

### all testCases/Modules:
To run all modules, navigate to `/testCases` directory and run:

`$ pytest  -v --html=Reports\report_ALL_TestCases.html testCases --self-contained-html`

*NOTE*: They will also generate a security risks HTML report in `Reports\report_ALL_TestCases.html`

### valid test:
To run Valid Login tests only, navigate to `/testCases` directory and run:

`$ pytest  -v --html=Reports\report_VALID_Hitung_Dana_Pensiun.html testCases\test_valid_HitungDanaPensiun --self-contained-html`

*NOTE*: They will also generate a HTML report in `Reports\report_VALID_Hitung_Dana_Pensiun.html`

### invalid test:
To run Invalid Login tests only, navigate to `/testCases` directory and run:

`$ pytest  -v --html=Reports\report_INVALID_Hitung_Dana_Pensiun.html testCases\test_invalid_HitungDanaPensiun --self-contained-html`

*NOTE*: They will also generate a security risks HTML report in `Reports\report_INVALID_Hitung_Dana_Pensiun.html`

### *VIDEO DOCUMENTATION*:

Tes Automation Hitung Dana Pensiun Sequis WEB.mp4 
