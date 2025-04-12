from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager #baixar a lib "pip install webdriver-manager"
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# --- Configurações do Chrome para parecer humano ---
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--start-maximized")
options.add_argument("--disable-logging") #Desativa logs do navegador, evitando que o console fique poluído com mensagens desnecessárias
#option.add_argument("--headless=new")

servico = Service(EdgeChromiumDriverManager().install())
#driver = webdriver.Chrome(options=options)
driver = webdriver.Edge(service=servico,options=options)

# Tira o 'navigator.webdriver'
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
})

# --- Função com WebDriverWait e múltiplas abas ---
lista_sites = ['https://www.google.com/'] * 3
lista_temas = ['santos futebol club', 'dolar hoje', 'previsao do tempo para o feriado em sao paulo']
juntar = zip(lista_sites, lista_temas)

def paginas(zipped):
    wait = WebDriverWait(driver, 10)
    contador = 0

    for site, tema in zipped:
        if contador == 0:
            driver.get(site)
            sleep(0.5)
        else:
            driver.execute_script(f"window.open('{site}', '_blank');")
            driver.switch_to.window(driver.window_handles[-1])
            sleep(0.5)

        # Espera o campo de busca estar presente e visível
        campo_busca = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="APjFqb"]')))
        campo_busca.send_keys(tema)
        sleep(0.5)

        # Espera o botão "Pesquisar Google" estar clicável e clica
        botao_pesquisar = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'gNO89b')))
        botao_pesquisar.click()
        sleep(0.5)

        contador += 1

paginas(juntar)

sleep(60)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))  # só pra manter aberto um tempo
driver.quit()