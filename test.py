#importing requred modules
import selenium.webdriver as wd
import selenium.common.exceptions as ex
import time
import subprocess as sp
import datetime as dt
from selenium.webdriver.common.keys import Keys

login = True

chrome_options = wd.ChromeOptions()
chrome_options.add_argument("user-data-dir=selenium") #loading the chrome driver

driver = wd.Chrome("/home/vanshika/Downloads/chromedriver3", chrome_options=chrome_options)
# names = ["Anju Kumari", "Radhey Shyam", "Kunal", "Swarnima Tiwari", "Abhimanyu Deswal", "Gouri Kakkanat Ullas", "Khadija Mohamad Haneefa", "Krishnaja R. Nair", "Anusree V A ", "Arjun Anand", "Shivam Kumar", "Reetvik Chatterjee ", "Harit Yadav", "Sujay", "Dev Tyagi", "Mohit Raj", "Prateek Srivastava", "Ishita Chauhan", "Yash Punia", "Vaibhav Pathak", "Shubhi Yadav", "Kriti Sharma", "Aitik Gupta", "Aadit Agarwal", "Mokshda Sharma", "Akshat Sharma", "Aman Verma", "Aniket Tiwari", "Jayvardhan Patil", "Shubham Pandit", "NIHAR SANDA", "Satyam Kumar", "Priyam", "Anany talwad", "Sachin Som ", "Pratik Singh", "Rishabh baid", "Jigyansh varshney", "Aniket Kumar", "Harsh singh", "Nomulla Abbhinav Reddie", "Pasala Santosh Sai Gowtham", "Chandra pavan reddy Chada", "Rahul Sanjay", "Anjali sahu", "Priyanka Prasad", "Divya garg", "Tushar Jain", "Rishav Mazumdar", "Neha ", "Urja", "saijal bansal"]
# phones = [9643720184, 7988512757, 8219948385, 8384859321, 9306434981, 8111811783, 8943370331, 8078031875, 8111850312, 7889608162, 7982884322, 8219793207, 9660040281, 9044002979, 8076277971, 7870541098, 6230077791, 9027021228, 9873921954, 9910517217, 9793197171, 7018623256, 9821633928, 8179675451, 8239332636, 8219753575, 9198780006, 8294571223, 7038344824, 8104470803, 8097283441, 6284900945, 8439279268, 8979207002, 8824634027, 7808729929, 8619006174, 8171762485, 7979913066, 8303458001, 6281466008, 9652868956, 9533962021, 9550398681, 7354996701, 9145956343, 7976657299, 7982250544, 7033965384, 9736257880, 7814475542, 8003962862]
phones = [9518139757,9306434981,9813614130]  #list of phone numbers to whom the message is to be sent
names = ["Paramjeet","Abhimanyu Deswal","Rahul"]

if not login:
    driver.get("https://web.whatsapp.com") #if the user is not logged in then opening the link
else:
    i = 0
    for index in range(0,len(phones)):
        phone = phones[index]
        message = f"""Dear {names[index]},
The project submissions for our event *"Game of Codes"* has been started. The deadline for the project submissions is 23:59 08/08/2020. After that no project submissions will be entertained.

The link is mentioned below as well as on your website.
Link : https://forms.gle/m9aFDAkMKREzeMw26

Do join us on telegram for the lastest updates:
Link : https://t.me/codecops

Cheers
Team CodeCops
"""
        print(f"{index+1}/{len(phones)}")  # getting the count of total number of contacts to whom the message is to be sent
        driver.get(f"https://web.whatsapp.com/send?phone=91{phone}&text&source&data&app_absent")
        time.sleep(8)    
        try:
            messageText = driver.find_elements_by_class_name('_3FRCZ') #finding the element by class
            if len(messageText)==1:
                print(f"Not on whatsapp {phone}")
                continue
            messageText = messageText[1]     
            for row in str(message).split("\n"):  #splitting the text into rows and then pressing the shift and enter key
                messageText.send_keys(row)
                messageText.send_keys(Keys.SHIFT,Keys.ENTER)
            time.sleep(3)
            sendButton = driver.find_element_by_class_name('_1U1xa')
            sendButton.click()
            time.sleep(3)
        except ex.NoSuchElementException: #if in case the array does not retun anything the given message is logged out
            print(f"Not on whatsapp {phone}")
