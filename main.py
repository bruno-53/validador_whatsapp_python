from selenium import webdriver

#CONFIGURAR O SELENIUM
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
servico = Service(GeckoDriverManager().install())
navegador = webdriver.Firefox(service=servico)

# CONFIGURAR LISTA DE NUMEROS
arquivo_numeros = open('numeros.txt','r')
numeros = []
for linha in arquivo_numeros:
    linha = linha.strip()
    numeros.append(linha)
arquivo_numeros.close()

# ABRE ARQUIVO DE RESULTADOS
arquivo_resultado = open('resultado.txt','w')
resultado = []


#VALIDAR SE O LOGIN FOI FEITO
navegador.get('https://web.whatsapp.com/');
navegador.implicitly_wait(3.0)
validador = navegador.find_element('xpath','/html/body/div[1]/div/div/div[3]/div[1]/div/a').is_displayed()

# VALIDAR NUMERO
if validador is True:
    print('-----------------------------------')
    print('ATENÇÃO: FAÇA O LOGIN E TECLE ENTER')
    print('-----------------------------------')
    input('...')
    positivo = 0
    negativo = 0
    for numero in numeros:
        navegador.get('https://web.whatsapp.com/send/?phone=55'+ numero +
        '&text&type=phone_number')
        navegador.implicitly_wait(20.0)

        # VERIFICA SE É E SALVA EM NOVO ARQUIVO O RESULTADO
        try:
            mensagem_erro = navegador.find_element('xpath','/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div').is_displayed()
            print("Resultado: {}... NEGATIVO".format(numero))
            resultado.append("Numero: ")
            resultado.append(numero)
            resultado.append(" - Status: NAO WHATSAPP \n")
            negativo += 1
        except:
            print("Resultado: {}... POSITIVO".format(numero))
            resultado.append("Numero: ")
            resultado.append(numero)
            resultado.append(" - Status: OK \n")
            positivo += 1


print('\n--- RESULTADO ---')
print("TOTAL DE NUMEROS: {}\nPOSITIVO: {}\nNEGATIVO: {}".format((positivo+negativo),positivo,negativo))
print('----------------')
arquivo_resultado.writelines(resultado)
arquivo_numeros.close()