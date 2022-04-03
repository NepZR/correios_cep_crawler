# Selenium Crawler: Address Search by Postal Codes (CEPs)

#### Project made in the Software Testing classes on the Federal University of Western Para - Course: Computer Science.

> Esta é a versão em Inglês deste LEIA-ME. Para acessar a versão em Português Brasileiro, por favor, clique <a href="https://github.com/NepZR/correios_cep_crawler/blob/main/README.md">aqui</a>.
---


### Code objectives:
 - Demonstrate the Selenium's capability to automate web based tasks;
 - Demonstrate the Selenium's capability to be multiplatform;
 - Demonstrate the Selenium's implementation capability on multiple browsers;
   - Here, only the ChromeDriver was utilized - based on Google Chrome.
 - Demonstrate how the library can be used for testing and other purposes;
 - "Test Code" Implementation;
 - Crawl the data from a specific web platform;
   - The Correios' address search page to find addresses based on CEP.
 - Implement native functions from Selenium;
   - Navigate between pages;
   - Execute actions (mouse clicks and screenshots);
   - Verify the page's content based on parameters (ID, XPath);
   - Extract data based on defined parameters.
 - Integrate with the Pandas Library;
   - Create a Pandas DataFrame (from a dictionary);
     - `pd.DataFrame(data = dict)`
   - Export the data as a CSV file with the UTF-8 encoding.
     - `df.to_csv('file_name.csv', encoding='utf-8', index=False)`
  
---

## How to:
1. Clone the repository:
   ~~~
   $ git clone https://github.com/NepZR/correios_cep_crawler.git
   ~~~
2. Install the dependencies with PIP or Conda:
   ~~~
   $ pip install -r requirements.txt
   -------------- or --------------
   $ conda install pandas selenium -y
   ~~~
3. Run the crawler script:
   ~~~
   $ python -u selenium_correios_cep.py
   ~~~
   > If needed, you can change the list of CEPs to be searched. Just edit the "_selenium_correios_cep.py_" file in a text editor or desired IDE and modify the list in the key "CEP" on the dict "test_data". Use **only numbers** in a string.

- All the collected data and generated screenshots will be saved on the "data" and "img" folders, in the CSV and PNG formats.

 
---
<div style="display: flex; align-itens: center; justify-content: center;">
  <h2 style="font-family: 'Montserrrat', sans-serif;">Developer</h2>
</div>

<table style="display: flex; align-itens: center; justify-content: center;">
  <tr>
    <td align="center"><a href="https://github.com/NepZR"><img style="width: 150px; height: 150;" src="https://avatars.githubusercontent.com/u/37887926" width="100px;" alt=""/><br /><sub><b>Lucas Darlindo Freitas Rodrigues</b></sub></a><br /><sub><b>Undergraduate in Computer Science</sub></a><br /><a href="https://www.linkedin.com/in/lucasdfr/?locale=en_US"><sub><b>LinkedIn (lucasdfr)</b></sub></a></td>
  </tr>
<table>