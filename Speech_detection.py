import speech_recognition as sr
import pyttsx
import datetime
import pybrain
#import pocketsphinx
import selenium
r = sr.Recognizer()
jarvis = pyttsx.init()

def activate():

    status = False

    while status == False:
        with sr.Microphone() as source:
            print "Please talk"
            audio = r.listen(source)

        try:
            data = r.recognize_google(audio)
            data_list = data.split()
            print "You said: {0}".format(data)
            print data_list, type(data_list)
            if "jarvis" in data_list or "Jarvis" in data_list:
                wakeup_jarvis(data_list)
            elif "Goodbye" in data_list:
                status = True
            else:
                pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            pass

def wakeup_jarvis(word_list):
    greeting_time = 0
    currentTime = datetime.datetime.now()
    if currentTime.hour < 12:
        greeting_time = "Good Morning"
    elif 12 <= currentTime.hour < 18:
        greeting_time = "Good Afternoon"
    elif 18<= currentTime.hour < 21:
        greeting_time = "Good Evening"
    else:
        greeting_time = "Good Night"
    active = True
    if len(word_list) > 1:
        if "hello" in word_list or "hi" in word_list or ("wake" in word_list and "up" in word_list):
            jarvis.say("{0} sir, How may i be of service to you now?".format(greeting_time))
            jarvis.runAndWait()
    else:
        jarvis.say("{0} sir, How may i be of service to you now?".format(greeting_time))
        jarvis.runAndWait()
    while active is True:

        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            data = r.recognize_google(audio)
            data_list = data.split()
            print "You said: {0}".format(data)
            if "sleep" in data_list or "standby" in data_list:
                jarvis.say("Ok sir call me when you need me again")
                jarvis.runAndWait()
                active = False
            else:
                pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            pass
if __name__ == '__main__':
    app = activate()