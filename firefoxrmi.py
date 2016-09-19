from selenium import webdriver

def rmi():
    #Variables
    login = 'sbrooks'
    password = 'Wednes99day1'

    #Start of script
    driver = webdriver.Firefox()
    type(driver)
    driver.get('https://rmi.rmplc.net')

    try:
        loginElm = driver.find_element_by_id('UserName')
        loginElm.send_keys(login)
        passwordElm = driver.find_element_by_id('Password')
        passwordElm.send_keys(password)
        signInElm = driver.find_element_by_id('SignInButton')
        signInElm.submit()
    except:
        print('Was not able to find an element with that name.')

rmi()
