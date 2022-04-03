'''
Portuguese (Brazilian) - PTBR:
-> Código escrito por..: Lucas Darlindo Freitas Rodrigues (lucas.darlindo@gmail.com);
-> Última atualização..: Quinta - Janeiro 13, 2022 - 23:10 [UTC-3] (Versão 3);
-> Descrição feita em..: Sábado - Abril 02, 2022 - 20:54 [UTC-3];
-> Objetivo............: Demonstração simples do Selenium WebDriver;
-> Plataforma escolhida: Correios - Sistema de verificação de CEPs e Endereços;
-> Disciplina..........: Teste e Qualidade de Software.

English - ENG:
-> Code written by.....: Lucas Darlindo Freitas Rodrigues (lucas.darlindo@gmail.com);
-> Last updated........: Thursday - January 13th, 2022 - 11:10 PM [UTC-3] (Version 3);
-> Description written.: Saturday - April 02nd, 2022 - 08:54 PM [UTC-3];
-> Objective...........: Simple overview of the Selenium WebDriver;
-> Crawled platform....: Correios - Verification system for CEPs and Addresses;
-> Disciplina..........: Software Testing.
'''

# PTBR: Bibliotecas
# ENG.: Libraries
from selenium import webdriver
from sys import platform
import time
import pandas as pd

# PTBR: Método para seleção automática do binário a ser utilizado no WebDriver, dependendo do SO
# ENG.: Method for automatically select the correct binary by OS for the ChromeDriver.
def webdriver_bin():
    if platform == 'darwin':
        return 'ChromeDriver/chromedriver_mac'
    elif platform == 'win32':
        return 'ChromeDriver/chromedriver_win.exe'
    else:
        return 'ChromeDriver/chromedriver_linux'

# PTBR: Dados de configuração dos testes.
# ENG.: Test config data.
test_data = {
    'CEP': ['68005200', '68005290', '04523001'],
    'input_xpath': '//div[@class="campos"]//input[@id="endereco"]',
    'submit_xpath': '//div[@class="botoes"]/button',
    'result_xpath': '//table[@id="resultado-DNEC"]',
    'data_tags': ['\"Logradouro/Nome\"', '\"Bairro/Distrito\"', '\"Localidade/UF\"', '\"CEP\"']
}

# PTBR: URL da página alvo para testes.
# ENG.: Target URL for the tests.
target_url = 'https://buscacepinter.correios.com.br/app/endereco/index.php'

# PTBR: Instanciamento e inicialização do WebDriver com o ChromeDriver.
# ENG.: WebDriver's initialization with ChromeDriver.
chromeDriver = webdriver.Chrome(executable_path='/home/lucasdfr/Documentos/chromedriver')
chromeDriver.get(target_url)

# PTBR: Dicionário para armazenar os dados coletados durante o processo de execução.
# ENG.: Dict to store the crawled data during the process.
correios_data = {
    'Logradouro/Nome': [],
    'Bairro/Distrito': [],
    'Localidade/UF'  : [],
    'CEP'            : []
}

# PTBR: Execução dos testes (Extração dos dados com o Selenium, e fazendo capturas de tela do processo).
# ENG.: Test Routine (Selenium crawling the data, taking screenshots).
for cep in test_data['CEP']:
    try:
        time.sleep(2)
        input_box  = chromeDriver.find_element_by_xpath(test_data['input_xpath'])
        submit_btn = chromeDriver.find_element_by_xpath(test_data['submit_xpath']) 

        input_box.send_keys(cep)
        submit_btn.click()

        time.sleep(3)
        chromeDriver.get_screenshot_as_file('img/test_CEP_{}.png'.format(cep))

        results = chromeDriver.find_element_by_xpath(test_data['result_xpath'])

        for xpath in test_data['data_tags']:
            for item in results.find_elements_by_xpath(('//td[@data-th={}]').format(xpath)):
                correios_data[str(xpath).replace('\"', '')].append(item.text)
        
    except:
        print('\nOcorreu um erro durante a execução do teste com o CEP {}. Continuando com os demais testes.'.format(cep))
        continue
    finally:
        chromeDriver.get(target_url)

# PTBR: Armazenando os dados em um Pandas DataFrame e exportando para CSV com Codificação UTF-8.
# ENG.: Making a Pandas DataFrame with the data in the "correios_data" dict and using it to export as a CSV file with the UTF-8 encoding.
df = pd.DataFrame(data = correios_data)
df.to_csv('data/selenium_correios_data.csv', encoding='utf-8', index=False)

# PTBR: Fechamento da aba e finalização do processo do WebDriver.
# ENG.: Closing the webdriver tab and ending it's process.
chromeDriver.close()
chromeDriver.quit()