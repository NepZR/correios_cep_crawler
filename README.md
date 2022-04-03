# Web Crawler com Selenium: Busca de endereços pelo Código de Endereçamento Postal (CEPs)

#### Este é um projeto feito na disciplina de Teste e Qualidade de Software na Universidade Federal do Oeste do Pará - Curso de Bacharelado em Ciência da Computação.

> This is the Portuguese Brazilian version of this README. To access the English version, please click <a href="https://github.com/NepZR/correios_cep_crawler/blob/main/README_ENG.md">here</a>.
---


## Objetivos deste código:
 - Demonstrar a capacidade do Selenium para automatização de tarefas baseadas na _web_;
 - Demonstrar a capacidade do Selenium em ser multi-plataformas;
 - Demonstrar a compatibilidade para implementação do Selenium em múltiplos navegadores;
   - Nesse caso específico, foi utilizado apenas o ChromeDriver - baseado no Google Chrome.
 - Demonstrar como a biblioteca pode ser utilizada para testes e outros propósitos;
 - Implementar um "código teste";
 - Efetuar a coleta de dados em uma plataforma definida;
   - Site de busca dos Correios para encontrar endereços/logradouros pelo CEP;
 - Implementar funçoes nativas do Selenium;
   - Navegar entre páginas;
   - Executar açoes (como cliques e capturas de tela);
   - Verificar o conteúdo das páginas baseado em parâmetros (como ID, XPath);
   - Extrair dados de acordo com parâmetros definidos;
 - Combinar com a biblioteca Pandas;
   - Criar um Pandas DataFrame (a partir de um dicionário);
     - `pd.DataFrame(data = dict)`
   - Exportar como um arquivo CSV com codificação UTF-8;
     - `df.to_csv('file_name.csv', encoding='utf-8', index=False)`

---

## Como executar:
1. Clonar o repositório:
   ~~~
   $ git clone https://github.com/NepZR/correios_cep_crawler.git
   ~~~
2. Instalar as dependências com o PIP ou Conda:
   ~~~
   $ pip install -r requirements.txt
   -------------- ou --------------
   $ conda install pandas selenium -y
   ~~~
3. Executar o script do crawler:
   ~~~
   $ python -u selenium_correios_cep.py
   ~~~
   > Caso você queira configurar os CEPs a serem acessados, basta abrir o arquivo em um editor ou IDE desejado e modificar a lista contida na chave "CEP" do dicionário "test_data". Devem ser inseridos **apenas os números** do CEP, sem caracteres extras e em formato de texto/_string_.

- Os dados coletados e as capturas de tela geradas serão salvos, respectivamente, nas pastas "data" e "img" em formato CSV e PNG.

 
---
<div style="display: flex; align-itens: center; justify-content: center;">
  <h2 style="font-family: 'Montserrrat', sans-serif;">Desenvolvedor</h2>
</div>

<table style="display: flex; align-itens: center; justify-content: center;">
  <tr>
    <td align="center"><a href="https://github.com/NepZR"><img style="width: 150px; height: 150;" src="https://avatars.githubusercontent.com/u/37887926" width="100px;" alt=""/><br /><sub><b>Lucas Darlindo Freitas Rodrigues</b></sub></a><br /><sub><b>Graduando em Ciência da Computação</sub></a><br /><a href="https://www.linkedin.com/in/lucasdfr"><sub><b>LinkedIn (lucasdfr)</b></sub></a></td>
  </tr>
<table>