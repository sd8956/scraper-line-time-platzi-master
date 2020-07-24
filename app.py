"""Scraper platz profile"""

import time
import os
import requests
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()


def get_courses():
    """Start the scraper process"""

    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://platzi.com/login/')

    faceebook_button = driver.find_element_by_link_text(
        "Inicia sesión con Facebook")
    faceebook_button.click()

    time.sleep(2)

    input_email = driver.find_element_by_id("email")
    input_pass = driver.find_element_by_id("pass")

    time.sleep(2)

    input_email.send_keys(os.getenv("EMAIL"))
    input_pass.send_keys(os.getenv("PASS"))

    time.sleep(2)

    login_button = driver.find_element_by_id("loginbutton")
    login_button.click()

    time.sleep(2)

    driver.get('https://platzi.com/@santiDuque1700/')

    time.sleep(2)

    arrow = driver.find_element_by_class_name(
        "SeeMore").find_element_by_tag_name('span')
    arrow.click()

    time.sleep(2)

    courses_buttons = driver.find_elements_by_class_name("is-approved")

    urls = []

    for course_btn in courses_buttons:
        urls.append(course_btn.find_element_by_tag_name(
            'a').get_attribute('href'))

    time.sleep(2)

    for url in urls:
        driver.get(url)

        diplom_content = driver.find_element_by_class_name("Diploma")

        title = diplom_content.find_element_by_class_name("Diploma-course").text
        image = diplom_content.find_element_by_tag_name("img").get_attribute("src")
        image = image[13:]
        
        print('--------------------------------------------------------------------------------------')
        print(title)
        print('--------------------------------------------------------------------------------------')

        requests.post('http://127.0.0.1:8000/courses', json={
            "title": title,
            "image": image
        })

        time.sleep(2)

    driver.close()


if __name__ == "__main__":
    print('Selenium starts')
    get_courses()
