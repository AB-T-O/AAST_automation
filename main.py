import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

id=int(input("Enter ID: "))
pid=input("Enter PIN: ")
cs=input("Enter cs: ")
driver = webdriver.Firefox()
driver.get("https://alexreg.aast.edu/aastreg/frm_login.aspx")#https://www.selenium.dev/selenium/web/web-form.html
def login_s1(ID, pincod):
     driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder1_UserName\"]").send_keys(ID)
     driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder1_Password\"]").send_keys(pincod)
     driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder1_btn_login\"]").click()
def s2():
    try:
        driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder1_lmajor\"]").click()
    except:
        print("S2 problem")
def s3():
    driver.find_element(By.XPATH,"// *[ @ id = \"ctl00_ContentPlaceHolder1_Lbtn_Reg\"]").click()

def s_testing():
    print("you are in testing mode")
    driver.find_element(By.XPATH, "//*[@id=\"ctl00_ContentPlaceHolder1_lbtn_changeReg\"]").click()
def s4():
    print("you are in normal mode")
    while True :
        try:
            driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder1_lbtn_InsertTermCourse\"]").click()
            break
        except:
            s3()
            continue
def fun(xp,xpaths,what_to_select):
    try:
        dropdown_menu = driver.find_element(By.XPATH,xp)
        dropdown_element =Select(dropdown_menu)
        ops = dropdown_element.options
        ops_text =[]
        for op in ops:
            ops_text.append(op.text.lower())
        for text in ops_text:
            if what_to_select.lower() in text:
                dropdown_element.select_by_index(ops_text.index(text))
                break
        ##time.sleep(2)
        return True
    except:
        return False

def s5(what_to_select):
    xpaths = {"//*[@id=\"ctl00_ContentPlaceHolder1_grdvw_courses_ctl02_drp_cls\"]","//*[@id=\"ctl00_ContentPlaceHolder1_grdvw_courses_ctl03_drp_cls\"]","//*[@id=\"ctl00_ContentPlaceHolder1_grdvw_courses_ctl04_drp_cls\"]","//*[@id=\"ctl00_ContentPlaceHolder1_grdvw_courses_ctl05_drp_cls\"]","//*[@id=\"ctl00_ContentPlaceHolder1_grdvw_courses_ctl06_drp_cls\"]","//*[@id=\"ctl00_ContentPlaceHolder1_grdvw_courses_ctl07_drp_cls\"]"}
    for xp in xpaths :
         while True:
             if fun(xp,xpaths,what_to_select):
                 break
login_s1(id,pid)#enter your di and pin cod
s2()
s3()
#s4() # used for normal use does not work for testing
s_testing() #used for testing do not use for normal use
s5(cs)
#:)