from galicia.galicia import Galicia
from constants import CHROME_OPTIONS
from constants import WRONG_DATE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import calendar
from telegram.telegram import Telegram

today = date.today()
# dd/mm/YY
todayFormatted = today.strftime("%d/%m/%Y")

def isPenultimateWorkingDayOfTheMonth() -> bool:
    """ Indica si es el día que se cobra o no. """
    return today.day == calendar.monthrange(today.year, today.month)[1]-1 and today.weekday() < 5


if (isPenultimateWorkingDayOfTheMonth()):
    bot = Galicia(options=CHROME_OPTIONS)
    telegram = Telegram()
    
    bot.go_to_login_page()

    wait = WebDriverWait(bot, 10)

    bot.fill_form()

    wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "container-fluid ")))
    wait.until(EC.element_to_be_clickable(bot.find_element(By.LINK_TEXT, "Cuentas")))

    bot.go_to_cuentas()

    
    wait.until(EC.element_to_be_clickable(bot.find_element(By.CLASS_NAME, "box_ctas")))
    bot.go_to_movimientos_de_cuenta()

    messageToSend = bot.find_deposit()

    telegram.send_telegram_msg(messageToSend)

    bot.__exit__()



else:
    print(WRONG_DATE)
