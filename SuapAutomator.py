from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from dotenv import load_dotenv
load_dotenv()


class SuapAutomator:
    def __init__(self):

        self.username = os.environ['username']
        self.password = os.environ['password']
        self.driver = self.initialize_driver()

    def initialize_driver(self):
        chrome_options = webdriver.ChromeOptions()
        # Executa o navegador em modo headless
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=chrome_options)

    def login(self):
        self.driver.get("https://suap.ifba.edu.br/")
        search_login = self.driver.find_element(By.NAME, "username")
        search_login.send_keys(self.username)

        search_password = self.driver.find_element(By.NAME, "password")
        search_password.send_keys(self.password)
        search_password.submit()

    def access_registration_notes(self, cod_turma, unidade):
        self.driver.get(f"https://suap.ifba.edu.br/edu/meu_diario/{cod_turma}/{unidade}/?tab=notas")

    def access_student_profile(self, profile_id):
        self.driver.get(
            f"https://suap.ifba.edu.br/ae/visualizarinscricaoae/{profile_id}")
        element = self.driver.find_element(
            By.XPATH, '//*[@id="content"]/div[3]/div[1]/div/table/tbody/tr[8]/td[2]')
        return element.text

    def access_student_register(self, register_id):
        self.driver.get(f"https://suap.ifba.edu.br/edu/aluno/{register_id}")
        cpf = self.driver.find_element(
            By.XPATH, '//*[@id="content"]/div[3]/div/div[2]/table/tbody/tr[3]/td[2]')

        periodo = self.driver.find_element(
            By.XPATH, '//*[@id="content"]/div[3]/div/div[2]/table/tbody/tr[4]/td[2]')

        return cpf.text, periodo.text

    def close_browser(self):
        input("Pressione Enter para fechar o navegador...")
        self.driver.quit()
