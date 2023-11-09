import unittest
from ..main import CourseScraper
from selenium.webdriver.common.by import By

class TestCourseScraper(unittest.TestCase):
    def setUp(self):
        # Create a new CourseScraper instance for each test
        self.scraper = CourseScraper("ASTR1001", "2023")

    def tearDown(self):
        # Clean up resources, such as closing the web driver
        self.scraper.driver.quit()

    def test_open_browser(self):
        # Test whether the open_browser method opens the correct URL
        self.scraper.open_browser()
        self.assertEqual(self.scraper.driver.current_url, "https://programsandcourses.anu.edu.au/2023/course/ASTR1001")

    def test_parse_class_number(self):
        # Test the parsing of class numbers from a sample row
        row = self.scraper.driver.find_element(By.CSS_SELECTOR, ".sample-class-row")
        class_number = self.scraper.parse_class_number(row)
        self.assertEqual(class_number, "1234")

    def test_get_class_numbers(self):
        # Test whether get_class_numbers returns a list of tuples
        class_numbers = self.scraper.get_class_numbers()
        self.assertTrue(isinstance(class_numbers, list))
        if class_numbers:
            self.assertTrue(isinstance(class_numbers[0], tuple))
    
    # Add more test cases as needed for your specific application

if __name__ == '__main__':
    unittest.main()
