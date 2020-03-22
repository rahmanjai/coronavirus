from selenium import webdriver
import time

class CoronaVirus:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.worldometers.info/coronavirus/')

    def get_data(self,country):
        # country = "China"
        try:
            country_contains = "contains(., '%s')" % country

            time.sleep(3)

            table = self.driver.find_element_by_xpath(
                '//*[@id="main_table_countries_today"]/tbody[1]')

            country_element = table.find_element_by_xpath(
                "//td[%s]" % country_contains)
            row = country_element.find_element_by_xpath("./..")
            total_cases = row.find_element_by_xpath(
                "//tr[%s]/td[2]" % country_contains)
            new_cases = row.find_element_by_xpath(
                "//tr[%s]/td[3]" % country_contains)
            total_deaths = row.find_element_by_xpath(
                "//tr[%s]/td[4]" % country_contains)
            new_deaths = row.find_element_by_xpath(
                "//tr[%s]/td[5]" % country_contains)
            active_cases = row.find_element_by_xpath(
                "//tr[%s]/td[6]" % country_contains)
            total_recovered = row.find_element_by_xpath(
                "//tr[%s]/td[7]" % country_contains)
            serious_critical = row.find_element_by_xpath(
                "//tr[%s]/td[8]" % country_contains)
            tot_1m = row.find_element_by_xpath(
                "//tr[%s]/td[9]" % country_contains)

            print("Country: " + str(country_element.text))
            print("Total cases: " + str(total_cases.text))
            print("New cases: " + str(new_cases.text))
            print("Total deaths: " + str(total_deaths.text))
            print("New deaths: " + str(new_deaths.text))
            print("Active cases: " + str(active_cases.text))
            print("Total recovered: " + str(total_recovered.text))
            print("Serious, critical cases: " + str(serious_critical.text))
            print("Total cases/1M population: " + str(tot_1m.text))

            self.driver.close()
        except Exception as e:
            print(e)
            self.driver.quit()


if __name__ == '__main__':
    bot = CoronaVirus()
    bot.get_data("Indo")
