from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *
from tkinter import ttk

year = '2023'
ANU_URL = 'https://programsandcourses.anu.edu.au/'+year+'/course/'
course_name = 'astr1001'


# Open up chrome with the url.




def getClassNumber(row):
    return row.text[0:4]


def obtainClassNumbers():
    driver = webdriver.Chrome()
    course_name = classInput.get()
    search_url = ANU_URL + course_name
    print('Getting class content for ' + course_name.upper()+"...")
    driver.get(search_url)
    if len(driver.find_elements(By.LINK_TEXT, "Class")) == 0:
        print("Cannot find course.")
        return

    class_button = driver.find_element(By.LINK_TEXT, "Class")
    class_button.click()

    if len(driver.find_elements(By.CLASS_NAME, "course-tab-content")) == 0:
        print("Course does not offer classes for the year " + year)
        return

    course_tab_content = driver.find_element(
        By.CLASS_NAME, "course-tab-content")
    rows = course_tab_content.find_elements(By.TAG_NAME, "tr")

    sessions = course_tab_content.find_elements(By.CSS_SELECTOR, "h3")

    session_rows = []
    # Extract the rows of values for sessions
    for i in range(len(rows)):
        if (i % 2 == 1):
            session_rows.append(rows[i])

    # Print sessions
    for i in range(len(sessions)):
        print(sessions[i].text + " | Class Number: " +
              getClassNumber(session_rows[i]))


def getCourseName():
    try:
        course_name = float(classInput.get())
        label.set("clicked")
    except ValueError:
        pass


root = Tk()
root.title("ANU Manager")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


classInput = StringVar()
inputent = ttk.Entry(mainframe, width=10, textvariable=feet)
inputent.grid(column=3, row=1, sticky=(W, E))
label = StringVar()
ttk.Label(mainframe, textvariable=label).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Get Numbers", command=obtainClassNumbers).grid(column=3, row=3, sticky=W)

root.mainloop()




# obtainClassNumbers()
