from selenium import webdriver
from lxml import html
import requests

def rmi():
    #Variables
    login = 'sbrooks'
    password = 'Wednes99day1'
    searchTerm = 'juniper'

    #Start of script
    driver = webdriver.Firefox()
    type(driver)
    driver.get('https://rmi.rmplc.net/internal/ifl/knowledgelibrary.asp')

    try:
        loginElm = driver.find_element_by_id('UserName')
        loginElm.send_keys(login)
        passwordElm = driver.find_element_by_id('Password')
        passwordElm.send_keys(password)
        signInElm = driver.find_element_by_id('SignInButton')
        signInElm.submit()
    except:
        print('Was not able to find an element with that name.')

    try:
        search = driver.find_element_by_xpath('//*[@id="inpSearchString"]')
        search.send_keys(searchTerm)
        searchClick = driver.find_element_by_xpath('//*[@id="top"]/tbody/tr[2]/td[2]/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td[10]/input')
        searchClick.click()
    except:
        print("You are wrong mate")

    iframe = driver.find_elements_by_xpath('//iframe[@id="kl_frameset"]')
    driver.switch_to_frame(iframe)
    link = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[4]/table/tbody/tr/td/a')

rmi()

