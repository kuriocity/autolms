from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as p
keyd=str(input("Enter your lms email id\n"))+'\n'
paswd=str(input("Enter your lms password\n"))+'\n'
b=webdriver.Chrome()
#b.get('https://www.google.com')
b.get("http://mydy.dypatil.edu")
login=b.find_element_by_id('username')
login.send_keys(keyd)
access=b.find_element_by_id('password')
access.send_keys(paswd)

lnch=b.find_elements_by_class_name('launchbutton')

curr = b.current_window_handle
for k in lnch:
        #lnch[k].click()
        print(k.get_attribute('href'))
        idnew=k.get_attribute('href')
        lenid=len(idnew)
        finalid=idnew[lenid-4:]#idnew[lenid-1]+idnew[lenid-2]+idnew[lenid-3]+idnew[lenid-4]
        #http://mydy.dypatil.edu/rait/course/view.php?id=1812 (example)
        p.hotkey('ctrl','t')
        b.switch_to.window(b.window_handles[1])
        b.get('http://mydy.dypatil.edu/rait/course/customview.php?id='+finalid)
        #http://mydy.dypatil.edu/rait/course/customview.php?id=1812 (example)
        h1=b.find_elements_by_class_name('pending')
        for i in h1:
                i.send_keys(Keys.CONTROL + Keys.SHIFT + Keys.ENTER)
                p.hotkey('ctrl','w')
        p.hotkey('ctrl','w')
        b.switch_to.window(curr)
        
