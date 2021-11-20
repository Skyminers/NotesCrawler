'''
This is a Web Crawler To: https://www.mobinovels.com/
'''
import os.path
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def switch_to_new(driver):
    all_handles = driver.window_handles
    driver.switch_to.window(all_handles[-1])


def switch_to_origin(driver):
    all_handles = driver.window_handles
    driver.switch_to.window(all_handles[0])


def wait_until_download_end():
    download_path = os.path.join('/', 'Users', 'sky_miner', 'Downloads')
    end_flag = False
    while not end_flag:
        time.sleep(2)
        downloading = [x for x in os.listdir(download_path) if x.endswith('crdownload')]
        if len(downloading) == 0:
            end_flag = True


def main():
    driver = webdriver.Chrome('/Users/sky_miner/Projects/tmps/chromedriver')

    url = 'https://www.mobinovels.com/mushoku-tensei/'
    driver.get(url)
    page_wait = WebDriverWait(driver, 8)
    page_wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'brave_element__inner_link')))

    close_ad = driver.find_element(by=By.CLASS_NAME, value='brave_element__inner_link')
    close_ad.click()

    download_urls = driver.find_elements(by="class name", value='aioseop-link')
    print(download_urls)
    for ele in download_urls:
        ele.click()
        switch_to_new(driver)
        while True:
            try:
                try:
                    page_wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[1]/div[2]/button')))
                except TimeoutException:
                    page_wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="passcode"]')))
                    driver.find_element(by=By.XPATH, value='//*[@id="passcode"]').send_keys('6195')
                    driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/div/div[1]/div/div/div/div[2]/div[2]/button').click()
                    page_wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[1]/div[2]/button')))
                break
            except TimeoutException:
                driver.refresh()

        download_button = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/div/div/div[4]/div[1]/div[2]/button')
        download_button.click()
        time.sleep(2)
        wait_until_download_end()
        driver.close()
        switch_to_origin(driver)


if __name__ == '__main__':
    main()

