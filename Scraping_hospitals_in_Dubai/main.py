from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import pandas as pd 
from time import sleep 

# driver up_to_date
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
website = "https://www.google.com/maps/search/dubai+hospitals+list/@25.2404505,55.1073003,11z?entry=ttu"

# To open the browser to start working
driver.get(website)
driver.maximize_window()

sleep(4)
Box = driver.find_element(By.XPATH, "//div[@role='feed']")

Hospitals = Box.find_elements(By.XPATH, ".//div[contains(@class, 'Nv2PK')]")

hospital_websites=[]
hospitals_on_map = []
hospital_titles = []
reviews = []
places = []
numbers = []

for hospital in Hospitals: 
    try: 
        sleep(2)
        hospital_website = hospital.find_element(By.XPATH, ".//a[@class='lcr4fd S9kvJb ']")
        hospital_websites.append(hospital_website.get_attribute('href'))
        print(hospital_website.get_attribute('href'))

        link_map = hospital.find_element(By.XPATH, ".//a[@class='hfpxzc']")
        hospitals_on_map.append(link_map.get_attribute('href'))
        print(link_map.get_attribute('href'))
        link_map.click()

        sleep(1)
        hospital_title = driver.find_element(By.XPATH, "//h1[@class='DUwDvf lfPIob']")
        hospital_titles.append(hospital_title.text)
        print(hospital_title.text)

        review = driver.find_element(By.XPATH, "//div[@class='F7nice ']")
        reviews.append(review.text)
        print(review.text)

        place = driver.find_element(By.XPATH, "(//div[contains(@class, 'Io6YTe ')])[1]")
        places.append(place.text)
        print(place.text)

        Number_hospital = driver.find_element(By.XPATH, "(//div[contains(@class, 'Io6YTe ')])[3]")
        numbers.append(Number_hospital.text)
        print(Number_hospital.text)

        print('exit page')
        driver.find_element(By.XPATH, "//button[contains(@class, 'yHy1rc ')]").click()

        print("****************************************************")
    except: 
        print('there are an error here ################# :(')
        

# Exporting data to a csv file 
df = pd.DataFrame({'Title': hospital_titles, 'Hospital_link_map': hospitals_on_map , 'place': places, 'PhoneNumber': numbers, 'reviews':reviews })
df.to_excel('Hospital_Dubai_List.xlsx', index=False)

print(df)


# closing the browser 
driver.quit()