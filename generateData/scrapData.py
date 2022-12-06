import generateData.constants as const
import os
from selenium import webdriver
from prettytable import PrettyTable
from selenium.webdriver.common.by import By
import numpy as np


class ScrapData(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\seleniumDriver",
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(ScrapData, self).__init__(options=options)
        self.implicitly_wait(15)
        # self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def openEvents(self):
        eventLink = self.find_element(By.CSS_SELECTOR, "a[href='events.php']")
        # print(eventLink)
        # for elem in eventLink:
        #     if elem.get_attribute('innerHTML').strip() == 'View More':
        #         print('Button')
        #     else:
        #         print(elem.get_attribute('innerHTML').strip())

        eventButton = eventLink.find_element(By.TAG_NAME, 'button')
        eventButton.click()

    def getNewsData(self):
        tableContainer = self.find_element(By.ID, "web-design-2")
        table = tableContainer.find_element(By.TAG_NAME, "table")
        head = table.find_element(By.TAG_NAME, 'thead')
        headRow = table.find_element(By.TAG_NAME, 'tr')
        fieldElem = table.find_elements(By.TAG_NAME, 'th')

        fieldNames = []

        for elem in fieldElem:
            fieldNames.append(elem.get_attribute('innerHTML').strip())

        fieldNames.append('Link')

        content = table.find_element(By.TAG_NAME, 'tbody')
        contentRows = content.find_elements(By.TAG_NAME, 'tr')

        content = []
        for row in contentRows:
            rowFields = row.find_elements(By.TAG_NAME, 'td')
            row = []
            count = 0
            linkVal = ""
            for field in rowFields:
                if count == 2:
                    if '</font>' in field.get_attribute('innerHTML').strip():
                        xpath = f'//*[@id="web-design-2"]/ul/table/tbody/tr[{len(content)}]/td[3]/font/font'
                        wrapper = field.find_element(By.XPATH, xpath)
                        row.append(wrapper.get_attribute('innerHTML').strip())
                        count += 1
                        continue
                if count == 1:
                    linkTag = field.find_element(By.TAG_NAME, "a")
                    linkVal = linkTag.get_attribute('href')
                    strVal = linkTag.get_attribute('innerHTML').strip()
                    row.append(strVal)
                    count += 1
                    continue
                else:
                    strVal = field.get_attribute('innerHTML').strip()
                    if len(strVal) == 0 or strVal == '-':
                        row.append(np.nan)
                    else:
                        row.append(strVal)
                count += 1
            row.append(linkVal)
            content.append(row)

        # table = PrettyTable(
        #     field_names=fieldNames
        # )
        # table.add_rows(content)
        # print(table)

        data = [fieldNames, content]
        return data
