from selenium import webdriver
from credentials import TOKEN

BASE_URL = "https://onlinebanking.bancogalicia.com.ar/login"
SEND_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_experimental_option("excludeSwitches", ['enable-automation'])
CHROME_OPTIONS.add_experimental_option("detach", True)
CHROME_OPTIONS.add_argument("window-size=1500,1000")

""" para no abrir ventana del navegador """
""" CHROME_OPTIONS.add_argument("headless") """

DEFAULT_MESSAGE = "Todavía no cobramos :("
TRANSFERENCIA_A_BUSCAR = "Transferencias Cash Sueldos"
SUCCESS_MESSAGE = "A mi plata la gasto como quiero:\n"
WRONG_DATE = "No es el ante ultimo dia habil del mes"
