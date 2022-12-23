from selenium import webdriver
from selenium.webdriver.common.by import By

year = '2023'
ANU_URL = 'https://programsandcourses.anu.edu.au/'+year+'/course/'
course_name = 'COMP1100'

search_url = ANU_URL + course_name;

print('Getting class content for ' + course_name.upper())

driver = webdriver.Chrome()# Open the website
driver.get(search_url)


def getClassNumber(row):
    return row.text[0:4]

def obtainClassNumbers():
    if len(driver.find_elements(By.LINK_TEXT, "Class")) == 0:
        print("Cannot find course.")
        return

    class_button = driver.find_element(By.LINK_TEXT, "Class")
    class_button.click()

    if len(driver.find_elements(By.CLASS_NAME,"course-tab-content")) == 0:
        print("Course does not offer classes for the year " +year)
        return

    course_tab_content = driver.find_element(By.CLASS_NAME,"course-tab-content")
    rows = course_tab_content.find_elements(By.TAG_NAME, "tr")

    sessions = course_tab_content.find_elements(By.CSS_SELECTOR, "h3")

    session_rows = []

    for i in range(len(rows)):
        if(i % 2 == 1):
            session_rows.append(rows[i])
    for i in range(len(sessions)):
        print(sessions[i].text + " | Class Number: " + getClassNumber(session_rows[i]))


obtainClassNumbers()