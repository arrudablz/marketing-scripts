# -*- coding: utf-8 -*-​
from selenium import webdriver
from time import sleep
import time
import requests, csv, sys, re
from io import StringIO
from math import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mydriver = webdriver.Chrome(executable_path='/Users/caio.leite/Downloads/chromedriver')

mydriver.set_window_size(1120, 550)

#É UM "SLEEP"
mydriver.implicitly_wait(2)

# print ("############## Sephora - Checkout ##############")
# baseurl = "https://www.sephora.com.br/"
# mydriver.get(baseurl)
# mydriver.find_element_by_class_name("welcome-msg").click()
# sleep(1)
# mydriver.find_element_by_id('email').send_keys('jessica@fax.dix.asia')
# mydriver.find_element_by_id('pass').send_keys('abacaxi123')
# mydriver.find_element_by_id('btn-login').click()
# mydriver.get("https://www.sephora.com.br/maquiagem")
# mydriver.find_element_by_class_name('product-image').click()
# sleep(3)
# mydriver.find_element_by_id("product-to-cart").click()
# sleep(3)
# mydriver.get("https://www.sephora.com.br/firecheckout/")
# sleep(1)
# import ipdb;ipdb.set_trace()
# mydriver.find_element_by_id("process-checkout").click()
# sleep(10)

# print ("\n\n\n############## Order {} - Boleto {} ##############\n\n\n".format(order_id, boleto))


'''
print ("############## The Beauty Box - OK ##############")
baseurl = "https://www.thebeautybox.com.br/"
mydriver.get(baseurl)
mydriver.find_element_by_class_name("__p_details_btn").click()
mydriver.find_element_by_class_name("buy-button").click()
mydriver.find_element_by_xpath('//*[@title="Fechar pedido"]').click()
sleep(1)
mydriver.find_element_by_id("client-pre-email").send_keys("jessica.abacaxi123@gmail.com")
mydriver.find_element_by_id("btn-client-pre-email").click()
sleep(1)
mydriver.find_element_by_id("btn-identified-user-button").click()
sleep(2)
mydriver.find_element_by_id("btn-go-to-payment").click()
sleep(5)
mydriver.find_element_by_link_text("Boleto bancário").click()
sleep(4)
mydriver.find_element_by_class_name("payment-submit-wrap").click()
sleep(10)
order_id = re.findall('[0-9.]+', mydriver.find_element_by_id("order-id").text.split('#v')[1].split('-')[0])[0]
boleto = mydriver.find_element_by_class_name("vtex-text-copy__text").text
print ("\n\n\n############## Order {} - Boleto {} ##############\n\n\n".format(order_id, boleto))
print ("############## The Beauty Box - OK ##############")
baseurl = "https://www.ikesaki.com.br/locao-nupill-tonico-facil-vitamina-c-200ml/p"
mydriver.get(baseurl)
sleep(1)
mydriver.find_element_by_class_name("js-product-buy-button").click()
sleep(1)
mydriver.find_element_by_id("cart-to-orderform").click()
sleep(1)
mydriver.find_element_by_id("client-pre-email").send_keys("jessica.abacaxi123@gmail.com")
mydriver.find_element_by_id("btn-client-pre-email").click()
sleep(1)
mydriver.find_element_by_id("btn-identified-user-button").click()
sleep(4)
mydriver.find_element_by_link_text("Boleto bancário").click()
sleep(10)
mydriver.find_element_by_id("payment-data-submit").click()
'''

print ("############## Época - Site Down##############")
baseurl = "https://www.epocacosmeticos.com.br/joico-curl-refreshed-reanimating-mist-anti-frizz/p"
mydriver.get(baseurl)
sleep(1)
element = mydriver.find_element_by_class_name("buy-button")
mydriver.execute_script("arguments[0].click();", element)
mydriver.get("https://www.epocacosmeticos.com.br/checkout/#/cart")
sleep(1)
mydriver.find_element_by_id("cart-to-orderform").click()
sleep(1)
mydriver.find_element_by_id("client-pre-email").send_keys("jessica.abacaxi123@gmail.com")
mydriver.find_element_by_id("btn-client-pre-email").click()
sleep(2)
element = mydriver.find_element_by_id("btn-identified-user-button")
mydriver.execute_script("arguments[0].click();", element)
sleep(2)
mydriver.find_element_by_link_text("Boleto bancário").click()
sleep(2)
element = mydriver.find_element_by_id("payment-data-submit")
mydriver.execute_script("arguments[0].click();", element)
sleep(3)
try:
	mydriver.find_element_by_id("btFechar").click()
except:
	pass

order_id = re.findall('[0-9.]+', mydriver.find_element_by_id("order_id"))[0] #corrigir#
print ("\n\n\n############## Order {}\n\n\n".format(order_id))
