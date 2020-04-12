import time
from selenium import webdriver
from types import SimpleNamespace

driver = webdriver.Chrome()
base_url = 'https://www.callofduty.com/warzone/strategyguide/tac-map-atlas/'

def get_all_zones_meta():
    driver.get(base_url)
    time.sleep(5)
    if (driver.find_element_by_css_selector('button[title="Accept Cookies"]').is_displayed()):
        driver.find_element_by_css_selector('button[title="Accept Cookies"]').click()
    sectors = []
    # sector = {}
    sector_selector = '.sector-entry'
    sector_elements = driver.find_elements_by_css_selector(sector_selector);
    for s_e in sector_elements:
       s_e.click()
    zone_selector = '.sector-entry li a'
    zones = driver.find_elements_by_css_selector(zone_selector)
    for zone in zones:
        name = zone.text
        path = zone.get_attribute('href')
        sector = SimpleNamespace(name=name, path=path)
        sectors.append(sector)
    print(sectors)
    time.sleep(5) # Let the user actually see something!
    driver.quit()


if __name__ == '__main__':
    get_all_zones_meta()