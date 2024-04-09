from anticaptchaofficial.recaptchav3proxyless import *

# Função para resolver o reCAPTCHA v3
def solve_recaptcha_v3(KEY, ws_url, ws_key, VERBOSE=1, MIN_SCORE=0.7):
    solver = recaptchaV3Proxyless()
    solver.set_verbose(VERBOSE)
    solver.set_key(KEY)
    solver.set_website_url(ws_url)
    solver.set_website_key(ws_key)
    solver.set_min_score(MIN_SCORE)

    solver.set_soft_id(0)

    g_response = solver.solve_and_return_solution()
    if g_response != 0:
        token = g_response
        return token
    else:
        return None


# Exemplo de uso de teste
KEY = 'SUA_CHAVE_AQUI'
ws_url = 'SUA_URL_AQUI'
ws_key = 'SUA_KEY_AQUI'
token = solve_recaptcha_v3(KEY, ws_url, ws_key)
print(token)


driver = webdriver.Chrome()

driver.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{token}'")

