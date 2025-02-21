from SuapAutomator import SuapAutomator
from PlanilhaHandler import PlanilhaHandler
from selenium.webdriver.common.by import By

# Acessa o SUAP
suap = SuapAutomator()  
suap.login()

# Ler a planilha

caminho = 'notas.xlsx'
handler = PlanilhaHandler(caminho)
dados = handler.ler_planilha()

#handler.imprimir_tabulado_records()

codigo_turma = ""
unidade = ""

suap.access_registration_notes(codigo_turma, unidade)
for i, aluno in enumerate(dados, 1):
    print(f"Coletando dados: {i} de {len(dados)}")

    nome_aluno = aluno["Nome"]
    nota1 = aluno["Nota 1"]
    nota2 = aluno["Nota 2"]
    nota3 = aluno["Nota 3"]

    try:
        # Localizar aluno na página pelo nome
        aluno_td = suap.driver.find_element(By.XPATH, f"//td//dd[contains(text(), '{nome_aluno}')]")
        
        # Localizar campo das notas
        aluno_tr = aluno_td.find_element(By.XPATH, "./ancestor::tr")
        inputs = aluno_tr.find_elements(By.XPATH, ".//input[@type='text']")

        # Limpar e preencher os campos com as novas notas
        inputs[0].clear()
        inputs[0].send_keys(str(nota1))
        inputs[1].clear()
        inputs[1].send_keys(str(nota2))
        inputs[2].clear()
        inputs[2].send_keys(str(nota3))

        print(f"Notas preenchidas para {nome_aluno}")

    except Exception as e:
        print(f"Erro ao preencher notas para {nome_aluno}")

suap.close_browser()