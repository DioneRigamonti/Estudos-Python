from playwright.sync_api import sync_playwright
from time import sleep

# with sync_playwright() as p:
#     navegador = p.chromium.launch(headless=False)

#     contexto = navegador.new_context(
#         user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
#     )

#     pagina = contexto.new_page()
#     pagina.goto("https://www.google.com")

#     # Espera um pouco para evitar que o Google bloqueie
#     sleep(2)

#     # Preenche o campo de busca
#     pagina.locator('xpath=//*[@id="APjFqb"]').fill("santos futebol clube")

#     # Clica no botão de pesquisa (pega o primeiro botão visível)
#     pagina.locator(".gNO89b").first.click()

#     print("passou")
#     sleep(5)


######################### exemplo com multi abas ################################

# with sync_playwright() as p:
#     navegador = p.chromium.launch(headless=False)
#     contexto = navegador.new_context()

#     # Primeira aba
#     aba1 = contexto.new_page()
#     aba1.goto("https://www.google.com")
#     aba1.locator('xpath=//*[@id="APjFqb"]').fill("santos futebol clube")
#     aba1.locator(".gNO89b").first.click()
#     #aba1.press('enter')

#     sleep(2)

#     # Segunda aba
#     aba2 = contexto.new_page()
#     aba2.goto("https://www.google.com")
#     aba2.locator('xpath=//*[@id="APjFqb"]').fill("previsão do tempo são paulo")
#     aba2.locator(".gNO89b").first.click()

#     sleep(5)
#     navegador.close()


# with sync_playwright() as p:
#     navegador = p.chromium.launch(headless=False,args=["--start-maximized"])

#     contexto = navegador.new_context(no_viewport=True,
#         user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
#     )

#     pagina = contexto.new_page()
#     pagina.goto("https://ge.globo.com/")
#     pagina.locator('xpath=/html/body/div[7]/div/div[3]/button/span').click() #fecha pop up
#     sleep(2)
#     pagina.locator('.menu-button').first.click()
#     pagina.locator('xpath=//*[@id="menu-1-brasileirao"]/a/span[1]').click()


#     print("passou")
#     sleep(5)

##############  Exemplo com paginas dinamicas utilizando o wait for... OBS: parametro timeout é milisegundos (1000 = 1 segundo) ####################

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False, args=["--start-maximized"])

    contexto = navegador.new_context(
        no_viewport=True,
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    )

    pagina = contexto.new_page()
    pagina.goto("https://ge.globo.com/")

    # Espera e fecha o pop-up (se aparecer)
    try:
        popup = pagina.locator('xpath=/html/body/div[7]/div/div[3]/button/span')
        popup.wait_for(timeout=10000)
        popup.click()
    except:
        print("Popup não apareceu.")

    # Espera o botão do menu estar visível
    menu_button = pagina.locator('xpath=//*[@id="header-produto"]/div[2]/div/div/div[1]/div')
    menu_button.wait_for(timeout=10000)
    menu_button.click()

    # Espera e clica no item do menu "Brasileirão"
    item_brasileirao = pagina.locator('xpath=//*[@id="menu-1-brasileirao"]/a/span[1]')
    item_brasileirao.wait_for(timeout=10000)
    item_brasileirao.click()

    print("passou")
    sleep(10)
