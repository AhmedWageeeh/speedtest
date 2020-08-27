##----My Tool Kit----##

def speedtest():
    try:
        from speedtest import Speedtest
    except:
        print('Error!')

    st = Speedtest()
    print('Your connection\'s download speed is : ', st.download()/1000000 + "Mbps")
    print('Your connection\'s upload speed is : ', st.upload()/1000000 + "Mbps")


def send_msg_to_waNum():
    import pywhatkit as kit

    to_num = str(input('Enter the receiver number : '))
    msg = str(input('Enter the message : '))
    print('if you want send it in 10:10 write in time 10,09 with prev seprator.')
    time = int(input('Enter the time when you want send it : '))

    kit.sendwhatmsg(to_num, msg, time)

def send_news_to_myNum():
    pass
    
def passGenerator():
                from password_generator import PasswordGenerator
                pwo = PasswordGenerator()
                

                pwo.excludeuchars = "ABCDEFTUVWXY" # (Optional)
                pwo.excludelchars = "abcdefghijkl" # (Optional)
                pwo.excludenumbers = "012345" # (Optional)
                pwo.excludeschars = "!$%^=-_" # (Optional)

		  # All properties are optional
                pwo.minlen = 20 # (Optional)
                pwo.maxlen = 20 # (Optional)
                pwo.minuchars = 2 # (Optional)
                pwo.minlchars = 3 # (Optional)
                pwo.minnumbers = 1 # (Optional)
                pwo.minschars = 1 # (Optional)

                print(pwo.generate())

		  # It takes two arguments
		  # required characters and length of required password
                pwo.shuffle_password('sdafasdf#@&^#&234u8', 20)


def network_speed():
    import speedtest
    from tabulate import tabulate

    class network(object):
        def __init__(self):
            self.parser = speedtest.Speedtest()
        def data(self):
            down = str(f"{round(self.parser.download()/1_000_000, 2)} Mbps")
            up = str(f"{round(self.parser.upload()/ 1_000_000, 2)} Mbps")
            return [["Interface", "Download", "Upload"], ["We", down, up]]
        def __repr__(self):
            speed = self.data()
            return tabulate(speed, headers="firstrow", tablefmt="fancy_grid")
    if __name__ == "__main__":
        print(network())


def auto_happyBirthday_fb():
    # importing necessary classes 
    # from different modules 
    from selenium import webdriver 
    from selenium.webdriver.common.by import By 
    from selenium.webdriver.support.ui import WebDriverWait 
    from selenium.webdriver.support import expected_conditions as EC 
    from selenium.webdriver.firefox.options import Options
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    from selenium.webdriver.common.keys import Keys 
    import time 

    cap = DesiredCapabilities().FIREFOX
    browser =webdriver.Firefox(capabilities=cap, executable_path="C:/Users/ahmed/InstaPy/assets/geckodriver.exe")      

    firefox_options = webdriver.FirefoxOptions() 
      
    #prefs = {"profile.default_content_setting_values.notifications": 2} 
    firefox_options.preferences = {"profile.default_content_setting_values.notifications": 2} 
      
    # open facebook.com using get() method 
    browser.get('https://www.facebook.com/') 
      
    # user_name or e-mail id 
    username = "agrawal.abhi108@gmail.com"
      
    # getting passowrd from text file 
    with open('test.txt', 'r') as myfile: 
        password = myfile.read().replace('\n', '') 
      
    print("Let's Begin") 
      
    element = browser.find_elements_by_xpath('//*[@id ="email"]') 
    element[0].send_keys(username) 
      
    print("Username Entered") 
      
    element = browser.find_element_by_xpath('//*[@id ="pass"]') 
    element.send_keys(password) 
      
    print("Password Entered") 
      
    # logging in 
    log_in = browser.find_elements_by_id('loginbutton') 
    log_in[0].click() 
      
    print("Login Successful") 
      
    browser.get('https://www.facebook.com/events/birthdays/') 
      
    feed = 'Happy Birthday !'
      
    element = browser.find_elements_by_xpath('''//*[@class ='enter_submit\ 
           uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea\ 
                      inlineReplyTextArea mentionsTextarea textInput']''') 
      
    cnt = 0
      
    for el in element: 
        cnt += 1
        element_id = str(el.get_attribute('id')) 
        XPATH = '//*[@id ="' + element_id + '"]'
        post_field = browser.find_element_by_xpath(XPATH) 
        post_field.send_keys(feed) 
        post_field.send_keys(Keys.RETURN) 
        print("Birthday Wish posted for friend" + str(cnt)) 
      
    # Close the browser 
    browser.close() 


def screenshot():
    import os
    import pyautogui
    save_path = os.path.join(os.path.expanduser("~"), "Pictures")

    shot = pyautogui.screenshot()
    shot.save(f"{save_path}\\python_screenshot.png")
    return print(f"\nScreenshot taken, and saved to {save_path}")
#-----------------Choices------------------
print("1.Get your Net Speed\n2.Send msg to WA number\n3.Send News to my WA num\n4.Generate Strong Password\n5.Get Network speed")
print("6.Auto Happy FB for all\n7.Take ScreenShot")
ch = int(input('Enter your choice : '))
if ch == 1:
    speedtest()
elif ch == 2:
    send_msg_to_waNum()
elif ch == 3:
    send_news_to_myNum()
elif ch == 4:
    passGenerator()
elif ch == 5:
    network_speed()
elif ch == 6:
    auto_happyBirthday_fb()
elif ch == 7:
    screenshot()
elif ch == 8:
    pass
elif ch == 9:
    pass
elif ch == 10:
    pass
elif ch == 11:
    pass
elif ch == 12:
    pass
elif ch == 2:
    pass
