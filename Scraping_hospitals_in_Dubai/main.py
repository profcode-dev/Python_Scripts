from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 
from time import sleep  

class Map_Scraper:

    def __init__(self) -> None:
        # driver up_to_date
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


    def Open_Website(self, url): 
        # To open the browser to start working
        self.driver.get(url)
        self.driver.maximize_window()

    def Getting_ELements(self):
        Box =  WebDriverWait(self.driver, 5).until(                 ## Wait for the Page is loading
                    EC.presence_of_element_located((By.XPATH, "//div[@role='feed']"))
                )
        self.Hospitals = Box.find_elements(By.XPATH, ".//div[contains(@class, 'Nv2PK')]")
    
    def Scrapping_Website(self):
        print("Start Scrapping Operation")

        self.hospital_websites=[]
        self.hospitals_on_map = []
        self.hospital_titles = []
        self.reviews = []
        self.places = []
        self.numbers = []

        for hospital in self.Hospitals: 
            try: 
                sleep(5)
                hospital_website = hospital.find_element(By.XPATH, ".//a[@class='lcr4fd S9kvJb ']")
                self.hospital_websites.append(hospital_website.get_attribute('href'))
                print(hospital_website.get_attribute('href'))

                link_map = hospital.find_element(By.XPATH, ".//a[@class='hfpxzc']")
                self.hospitals_on_map.append(link_map.get_attribute('href'))
                print(link_map.get_attribute('href'))
                link_map.click()
                
                sleep(4)
                hospital_title = self.driver.find_element(By.XPATH, "//h1[@class='DUwDvf lfPIob']")
                self.hospital_titles.append(hospital_title.text)
                print(hospital_title.text)

                review = self.driver.find_element(By.XPATH, "//div[@class='F7nice ']")
                self.reviews.append(review.text)
                print(review.text)

                place = self.driver.find_element(By.XPATH, "(//div[contains(@class, 'Io6YTe ')])[1]")
                self.places.append(place.text)
                print(place.text)

                Number_hospital = self.driver.find_element(By.XPATH, "(//div[contains(@class, 'Io6YTe ')])[3]")
                self.numbers.append(Number_hospital.text)
                print(Number_hospital.text)

                self.driver.find_element(By.XPATH, "//button[contains(@class, 'yHy1rc ')]").click()

                print("****************************************************")
            except: 
                print('there are an error here ################# :(')
        
    def Exporting_Data(self):
        print("Exporting Data...")
        try: 
            # Exporting data to a csv file 
            self.df = pd.DataFrame({'Title': self.hospital_titles, 'Hospital_link_map': self.hospitals_on_map , 'place': self.places, 'PhoneNumber': self.numbers, 'reviews':self.reviews })
            self.df.to_excel('Hospital_Dubai_List.xlsx', index=False)
            print(self.df)

        except: 
            print('Go out there is an error here :(')

    def Close_Browser(self):
        # print("Scrappeing Page successfully.")
        self.driver.quit()

 



# This is for testing/Debugging 
if __name__ == "__main__":
    
    # Create an instance of the SeleniumExample class
    selenium_example = Map_Scraper()
    
    # Open the Google website
    selenium_example.Open_Website('https://www.google.com/maps/search/dubai+hospitals+list/@25.2404505,55.1073003,11z?entry=ttu')
    
    # Perform a search
    selenium_example.Getting_ELements()
    selenium_example.Scrapping_Website()

    # Export Data 
    selenium_example.Exporting_Data()
    
    # Close the browser
    selenium_example.Close_Browser()

