import time
from selenium import webdriver
usernameStr = 'kremena1993@yahoo.com'
passwordStr = 'Kremen4et0'
browser= webdriver.Chrome('/Users/milus/Desktop/a/chromedriver')

browser.get("https://www.target.com/p/playstation-5-console/-/A-81114595")
buyButton = False
while not buyButton:

    try:
        addToCartBtn = addButton = browser.find_element_by_css_selector('[data-test="soldOutBlock"]')
        print("Button inst ready yet.")
        time.sleep(2)
        browser.refresh()

    except:
        i = 1
        while i < 30:
            addToCartBtn = addButton = browser.find_element_by_css_selector('[data-test="orderPickupButton"]')
            # addToCartBtn = addButton = browser.find_element_by_partial_link_text("")
            print("Button was clicked.")
            #browser.refresh()
            addToCartBtn.click()
            i=i+1
    
        #addToCartBtn = addButton = browser.find_element_by_css_selector('[data-test="orderPickupButton"]')
        # addToCartBtn = addButton = browser.find_element_by_partial_link_text("")
        #print("Button was clicked.")
        # addToCartBtn.click()
        buyButton = True
        #browser.get("https://www.target.com/co-cart")
        browser.get("https://www.target.com/co-login?shouldMergeCart=false&redirectToStep=PRECHECKOUT")
        time.sleep(2)
        browser.refresh()
        # username= browser.find_element_by_id('username')
        # username.send_keys(usernameStr)
        # time.sleep(2)
        # password = browser.find_element_by_id('password')
        # password.send_keys(passwordStr)
        # time.sleep(3)
        # submitBtn = browser.find_element_by_id('login')
        # submitBtn.click()
        

       


        #time.sleep(1)
        #checkOutButton = addButton = browser.find_element_by_css_selector('[data-test="checkout-button"]')
        #checkOutButton.click()
