from selenium import webdriver
import constants as const
from credentials import DNI
from credentials import USERNAME
from credentials import PASSWORD
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Galicia(webdriver.Chrome):
    def __init__(self, options):
        super(Galicia, self).__init__(options = options)
        self.maximize_window()

    def go_to_login_page(self):
        print("Abriendo navegador...")
        self.get(const.BASE_URL)
    
    def fill_form(self):
        print("Completando formulario...")
        dni_field = self.find_element(By.ID, "DocumentNumber")
        username_field = self.find_element(By.ID, "UserName")
        password_field = self.find_element(By.ID, "Password")
        btnSubmit = self.find_element(By.ID, "submitButton")
        dni_field.send_keys(DNI)
        username_field.send_keys(USERNAME)
        password_field.send_keys(PASSWORD)
        btnSubmit.click()
        print("Logueando...")

    def go_to_cuentas(self):
        print("Navegando a Cuentas...")
        cuentasLink = self.find_element(By.LINK_TEXT, "Cuentas")
        cuentasLink.click()

    def go_to_movimientos_de_cuenta(self):
        print("Navegando a Movimientos de Cuenta...")
        self.find_element(By.CLASS_NAME, "box_ctas").click()

    def find_deposit(self) -> str:
        table = self.find_element(By.ID, "ContenedorMovimientos")
        message = const.DEFAULT_MESSAGE
        depositado = False

        for row in table.find_elements(By.CLASS_NAME, "table-row"):
            for cell in row.find_elements(By.CLASS_NAME, "detalle-movimiento"):
                if (cell.text == const.TRANSFERENCIA_A_BUSCAR and not (depositado)):
                    print("Sueldo depositado")
                    message = const.SUCCESS_MESSAGE + row.text.replace("\n", " ")
                    depositado = True
        return message

    def __exit__(self):
        print("Exiting...")
        self.quit()