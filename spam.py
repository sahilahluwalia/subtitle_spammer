import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#variables
name=input("Enter the Name correctly\n")
delay=int(input("Enter delay time of messages\n"))
os=int(input("Which OS?\n Press 1 for Linux\n Press 2 for Windows\n"))
wait_time=int(input("Enter wait time in seconds to excute the spamming script \n(use more seconds if your browser is taking more time to scan barcode)\n for normal use 15-20\n"))

    
#firefox for linux and chrome for windows
if os==1: 
    driver = webdriver.Firefox()
elif os==2:
    driver = webdriver.Chrome('chromedriver.exe')
else :
    print("subscribe to pewdiepie")
    exit()

driver.get('https://web.whatsapp.com/')
#time for scaning barcode from mobile
time.sleep(wait_time)
#locating victim name in search bar
ele=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
time.sleep(1)
ele.send_keys(name)
time.sleep(1)
ele.send_keys(Keys.RETURN)
time.sleep(2)
#i guess this will prevent defocusing of victim chat for new message 
ele=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
ele.send_keys(Keys.RETURN)

#file opening
file=open("endgame.txt","r")
texts=file.read().split("\n")

#money brrbrrbrr brrrrrr
for sentence in texts:
    ele.send_keys(sentence)
    ele.send_keys(Keys.ENTER)
    time.sleep(delay)
