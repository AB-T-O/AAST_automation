from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
text_input = driver.find_element(By.XPATH,"/html/body/main/div/form/div/div[1]/label[1]") #//*[@id="ctl00_ContentPlaceHolder1_Password"] /////html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/div[2]/table/tbody/tr[6]/td
text_input.find_element(By.XPATH, "//*[@id=\"my-text-id\"]").send_keys("admin@localhost.dev")
password_input = driver.find_element(By.XPATH,"/html/body/main/div/form/div/div[1]/label[2]")
password_input =password_input.find_element(By.XPATH, "/html/body/main/div/form/div/div[1]/label[2]/input")
password_input.send_keys("admin@localhost.dev")
button= driver.find_element(By.XPATH,"/html/body/main/div/form/div/div[2]/button")
dropdown_menu = driver.find_element(By.XPATH,"/html/body/main/div/form/div/div[2]/label[1]/select")
dropdown_element =Select(dropdown_menu)
dropdown_element.select_by_index(2)
ops = dropdown_element.options
ops_text =[]
what_to_select = "One"
for op in ops:
    ops_text.append(op.text)





#button.click()