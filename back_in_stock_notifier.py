from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import smtplib

b = webdriver.PhantomJS()

b.get("URL_TO_OBSERVE")

try:

##### selects value small in Dropdown    
    select = Select(b.find_element_by_id('product-select-option-0'))

    select.select_by_value('Small') 
#####

    # find purchase button in html
    soup = BeautifulSoup(b.page_source, 'lxml') #parse with lxml
    purchase = soup.find('input', {'id': 'purchase'})

    if str(purchase).find("Add to cart") == -1:
        print('nothing there')


    else:
        # create an email message with just a subject line,
        msg = 'Subject: ITS AVAILABE'
        # set the 'from' address,
        fromaddr = 'YOUR_EMAIL'
        # set the 'to' addresses,
        toaddrs = ['FIRST_ADDRESS', 'SECOND_ADDRESS', 'A_THIRD_EMAIL_ADDRESS']

        # setup the email server, go to google settings to enable smtp
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login("YOUR_EMAIL_ADDRESS", "YOUR_PASSWORD")

        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)

        # send the email
        server.sendmail(fromaddr, toaddrs, msg)
        print('Message was send !!')
        # disconnect from the server
        server.quit()
except Exception as e:
    print(e)
