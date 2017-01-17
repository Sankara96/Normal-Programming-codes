from selenium import webdriver
#import pywinauto
from selenium.webdriver.common.keys import Keys
from time import sleep
import speech_recognition
import winsound

class Internet(object):

    def __init__(self):
        self.driver = webdriver.Firefox()
        from twilio.rest import TwilioRestClient

        # put your own credentials here
        ACCOUNT_SID = "AC47de814a0732878938b142a1ff33d051"
        AUTH_TOKEN = "597c9be990460fbcf00b221b9c0abf4a"

        self.client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)


    def facebook(self):
        self.driver.get("http://facebook.com")
        #sleep(5)
        email = self.driver.find_element_by_id("email")
        password = self.driver.find_element_by_id("pass")
        email.send_keys("sank.96")
        password.send_keys("Sankar98945")
        #sleep(1)
        log_in = self.driver.find_element_by_id("u_0_l")
        log_in.click()
        #sleep(10)

        try:
            chat_bar = self.driver.find_element_by_xpath('//*[@id="fbDockChatBuddylistNub"]/a')

            chat_bar.click()
        except:
            pass


        previous_count = 0
        while True:
            print "check"
            messages = self.driver.find_element_by_xpath('//*[@id="mercurymessagesCountValue"]')
            print messages
            messages_count = messages.text
            print "Message Count: "+str(messages_count)
            if messages_count > 0 and messages_count != '':
                message = []
                call = self.client.calls.create(
                    to="+919894512447",
                    from_="+18662652714",
                    url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient",
                    status_events="answered")
                break


        print "Done"

    def search_google(self,topic):

        self.search = self.driver.execute_script('window.open("","_blank");')
        self.driver.get("https://google.com")
        search = self.driver.find_element_by_xpath('//*[@id="lst-ib"]')
        search.send_keys(topic)
        search_button = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]')
        search_button.click()



if __name__ == '__main__':
    app = Internet()
    app.facebook()
