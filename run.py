from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *
from tkinter import ttk
import argparse
import csv
import os
from datetime import datetime
year = '2023'
ANU_URL = 'https://programsandcourses.anu.edu.au/'+year+'/course/'


# Open up chrome with the url.

class CourseScraper:

    def __init__(self,course_name,year):
        self.ANU_URL = 'https://programsandcourses.anu.edu.au/'
        self.driver = webdriver.Chrome()
        self.year = year 
        self.course_name = course_name 


    def open_browser(self):
        search_url = f'https://programsandcourses.anu.edu.au/{self.year}/course/{self.course_name.upper()}'
        self.driver.get(search_url)
    
    def parse_class_number(self,row):
        return row.text[0:4]

    def get_class_numbers(self):
        class_numbers = []
        if len(self.driver.find_elements(By.LINK_TEXT, "Class")) == 0:
            print("Course does not exist: " + self.course_name)
            return class_numbers
        
        class_button = self.driver.find_element(By.LINK_TEXT, "Class")
        class_button.click()

        if len(self.driver.find_elements(By.CLASS_NAME, "course-tab-content")) == 0:
            print("Course does not offer classes for the year " + year)
            return class_numbers

        course_tab_content = self.driver.find_element(By.CLASS_NAME, "course-tab-content")
        rows = course_tab_content.find_elements(By.TAG_NAME, "tr")

        sessions = course_tab_content.find_elements(By.CSS_SELECTOR, "h3")

        # Extract the rows of values for sessions
        session_rows = [rows[i] for i in range(1, len(rows), 2)]

        class_numbers = []
        for i in range(len(sessions)):
            session = sessions[i].text
            class_number = self.parse_class_number(session_rows[i])
            class_numbers.append((session, class_number))

        return class_numbers
    

class CacheManager:
    @staticmethod
    def does_course_exist(course_name, year):
        file_path = f"data/{course_name}_{year}_class_info.csv"
        return os.path.exists(file_path)

    @staticmethod
    def get_data_from_cache(course_name, year):
        file_path = f"data/{course_name}_{year}_class_info.csv"
        data = []
        if CacheManager.does_course_exist(course_name, year):
            with open(file_path, 'r', newline='') as file:
                csv_reader = csv.reader(file)
                data = list(csv_reader)
        return data

class DataManager:
    @staticmethod
    def save_to_csv(course_name, year, data):
        file_name = f"data/{course_name}_{year}_class_info.csv"
        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Session", "Class Number"])
            writer.writerows(data)
        print(f"Data saved to {file_name}")


def main():
    parser = argparse.ArgumentParser(description= "ANU Course Scraper")
    parser.add_argument("course_name", help = "ANU Course Name")
    parser.add_argument("--year", default=str(datetime.now().year), help="Academic year")
    args = parser.parse_args()
    course_name = args.course_name
    year = args.year

    if CacheManager.does_course_exist(course_name,year):
        data = CacheManager.get_data_from_cache(course_name,year)
    else:
        scraper = CourseScraper(course_name,year)
        scraper.open_browser(course_name,year)
        data = scraper.get_class_numbers()
        if data:
            DataManager.save_to_csv(data)

    if data:
        for session, class_number in data:
            print(f"{session} | Class Number: {class_number}")
    

if __name__ == "__main__":
    main()