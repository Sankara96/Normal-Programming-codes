from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class Harpic(object):

    def __init__(self):
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

        self.webdriver = webdriver.Firefox(firefox_profile=firefox_profile)

        self.webdriver.get("http://www.rbmavericks.com/team6.php")
        print 'First sleep'
        print 'second sleep'
        sleep(5)
        links = self.webdriver.find_elements_by_partial_link_text('Vote')
        for link in links:
            print link.get_attribute("href")
        #element = self.webdriver.find_element_by_xpath('//*[@id="xSectionGallery_xModule"]/div/div[3]/div/div[1]/div/div[4]/ul/li[1]/a')
        '''hov = ActionChains(self.webdriver).move_to_element(element)
        hov.perform()
        sleep(10)
        element.click()'''
        print 'third sleep'
        sleep(10)
        print 'fourth sleep'

if __name__ == '__main__':
    harpic = Harpic()