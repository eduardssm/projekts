import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = 'https://nodarbibas.rtu.lv/'
driver.get(url)

study_program = driver.find_element(By.CLASS_NAME, "filter-option-inner")
study_program.click()

RDBI0 = driver.find_element(By.XPATH, "//span[text()='Informācijas tehnoloģija (RDBI0)']")
RDBI0.click()

course = driver.find_element(By.ID, "course-id")
course.click()
course_selection = driver.find_element(By.XPATH , "//option[@value='1']")
course_selection.click()

group = driver.find_element(By.ID , "group-id")
group.click()
group_selection = driver.find_element(By.XPATH, "//option[@value='11451']")
group_selection.click()

today = datetime.today()
tomorrow = (today + timedelta(days=1)).strftime('%Y-%m-%d')
tomorrow_datetime = datetime.strptime(tomorrow, '%Y-%m-%d')
day_of_week = tomorrow_datetime.strftime('%A').lower()[:3]

string = "fc-daygrid-day.fc-day.fc-day-" + day_of_week + ".fc-day-future"
#print(string)
time.sleep(1)
day = driver.find_element(By.CLASS_NAME, string)

time.sleep(1)

time_rtu = day.find_elements(By.CLASS_NAME, "fc-event-time")
class_rtu = day.find_elements(By.CLASS_NAME, "fc-event-title")

if class_rtu:
    for i, j in zip(class_rtu, time_rtu):
        print(f"{i.text} plkst. {j.text}") 
else:
    print("Lekciju rīt nav")

time.sleep(5)
driver.quit()
