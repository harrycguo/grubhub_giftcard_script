from selenium import webdriver
from selenium.webdriver.common.keys import Keys

giftCardsFile = 'PATH/TO/YOUR/GIFTCARDSFILE'
chromeDriverPath = 'PATH/TO/YOUR/CHROMEDRIVER'

# Open TDP list
with open(giftCardsFile) as f:
    tdps = f.read().splitlines()

# Open Browser and go to gift card site

browser = webdriver.Chrome(chromeDriverPath)
browser.get('https://grubhub.cashstar.com/store/')

count = 0

for line in tdps:

    split = line.split(" ")
    email = split[0]
    numberGC = int(split[1])

    count = count + numberGC

    # MAX OF 99 GIFT CARDS PER TRANSACTION 
    # ALSO MAX OF 15 UNIQUE RECIPIENTS IN CART
    if (count > 99):
        break

    recipientName = browser.find_element_by_id('recipientName-input')
    recipientName.send_keys(email)

    recipientName = browser.find_element_by_id('senderName-input')
    recipientName.send_keys("SENDER NAME")

    continueButton = browser.find_element_by_class_name('btn--primary')
    continueButton.click()

    sendDigitalCard = browser.find_element_by_class_name('btn--primary')
    sendDigitalCard.click()

    continueButton = browser.find_element_by_class_name('btn--primary')
    continueButton.click()

    subtract = browser.find_element_by_class_name('spinner-control')

    for i in range(0, 16):
        subtract.click()

    add = browser.find_element_by_xpath("//*[@id='app-root']/div/main/div/form/section/div/div[3]/div/div/button[2]")
    for i in range(0, numberGC - 1):
        add.click()

    continueButton = browser.find_element_by_class_name('btn--primary')
    continueButton.click()

    continueButton = browser.find_element_by_class_name('btn--primary')
    continueButton.click()

    recipientName = browser.find_element_by_id('recipientEmail-input')
    recipientName.send_keys(email)

    continueButton = browser.find_element_by_class_name('btn--primary')
    continueButton.click()

    addAnotherCardButton = browser.find_element_by_class_name('btn_tertiary')
    addAnotherCardButton.click()
