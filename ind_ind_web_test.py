import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner
import time
import os

class IndonesiaIndicatorFunctionalityTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get("https://indonesiaindicator.com/home/")
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.ID, "root")))
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

    def tearDown(self):
        test_name = self.id().split('.')[-1]
        self.driver.save_screenshot(f"screenshots/{test_name}.png")
        self.driver.quit()

    # Menguji fungsi navigasi menu Produk
    def testProduct(self):
        try:
            product_link = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar"]/div/div/ul/li[3]/a'))
            )
            product_link.click()
            self.assertEqual(self.driver.current_url, 'https://indonesiaindicator.com/product', "Failed to navigate")
            time.sleep(5)

        except Exception as e:
            self.fail(f"Failed to click the element or validate the page: {str(e)}")

    # Menguji fungsi navigasi menu Strategic Framework
    def testStrategicFramework(self):
        try:
            strategicframework_link = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar"]/div/div/ul/li[2]/a'))
            )
            strategicframework_link.click()
            self.assertEqual(self.driver.current_url, 'https://indonesiaindicator.com/strategic-framework', "Failed to navigate")
            time.sleep(5)

        except Exception as e:
            self.fail(f"Failed to click the element or validate the page: {str(e)}")

    # Menguji fungsi navigasi menu News setelah mengklik Learn More
    def testNews(self):
        try:
            strategicframework_link = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar"]/div/div/ul/li[1]/a'))
            )
            strategicframework_link.click()
            news_button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarContent"]/ul/li[4]/a'))
            )
            news_button.click()
            self.assertEqual(
                self.driver.current_url, 
                'https://indonesiaindicator.com/news',
                "Failed to navigate"
            )
            time.sleep(5)

        except Exception as e:
            self.fail(f"Failed to click the element or validate the page: {str(e)}")

    # Menguji fungsi navigasi menu Geostrategic Intelligence setelah mengklik menu Strategic Framework
    def testGeoAfterStrategic(self):
        try:
            strategicframework_link = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar"]/div/div/ul/li[2]/a'))
            )
            strategicframework_link.click()
            geostrategic_link = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[3]/div/div/div/div[2]/div[1]/div/div[2]/button'))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", geostrategic_link)
            time.sleep(10)
            geostrategic_link.click()
            self.assertEqual(
                self.driver.current_url, 
                'https://indonesiaindicator.com/geostrategic-inteligence',
                "Failed to navigate"
            )
            time.sleep(5)

        except Exception as e:
            self.fail(f"Failed to click the element or validate the page: {str(e)}")

    # Menguji fungsi navigasi menu News setelah mengklik menu News lalu membuka salah satu berita
    def testViewNews(self):
        try:
            news_link = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar"]/div/div/ul/li[4]/a'))
            )
            news_link.click()
            the_news_link = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="hero"]/div/div/div[1]/div/div[2]/div/a/button'))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", the_news_link)
            time.sleep(10)
            the_news_link.click()
            time.sleep(10)
            new_tab = self.driver.window_handles[1]  
            self.driver.switch_to.window(new_tab) 
            self.assertEqual(
                self.driver.current_url, 
                'https://www.ntvnews.id/ekonomi/0129559/tiktok-jadi-platform-media-sosial-paling-populer-2024-di-indonesia',
                "Failed to navigate"
            )
            time.sleep(5)

        except Exception as e:
            self.fail(f"Failed to click the element or validate the page: {str(e)}")

    # FAIL TEST CASE
    def test_click_disabled_menu(self):
        try:
            search = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="navbar"]/div/div/div/button/svg'))
            )
            search.click()
            self.assertEqual(self.driver.current_url, 'https://indonesiaindicator.com/home', "Should not navigate")
            time.sleep(5)
        except Exception as e:
            self.fail(f"Failed to click the element or validate the page: {str(e)}")


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="test_reports",  
            report_name="TestReport",  
            verbosity=2
        )
    )
