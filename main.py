from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://alexreg.aast.edu/aastreg/frm_login.aspx")#https://www.selenium.dev/selenium/web/web-form.html
def login_s1(ID, pincod):
     driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder1_UserName\"]").send_keys(ID)
     driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder1_Password\"]").send_keys(pincod)
     driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder1_btn_login\"]").click()
def s2():
    driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder1_lmajor\"]").click()
def s3():
    driver.find_element(By.XPATH,"// *[ @ id = \"ctl00_ContentPlaceHolder1_Lbtn_Reg\"]").click()
def s4(what_to_select):
     dropdown_menu = driver.find_element(By.XPATH,"/html/body/main/div/form/div/div[2]/label[1]/select")
     dropdown_element =Select(dropdown_menu)
     ops = dropdown_element.options
     ops_text =[]
     for op in ops:
        ops_text.append(op.text.lower())
     for text in ops_text:
         if what_to_select.lower() in text:
            dropdown_element.select_by_index(ops_text.index(text))
            break


login_s1(123,13)
s2()
s3()
#s4()


