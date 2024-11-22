from bs4 import BeautifulSoup
import requests
from urllib3.exceptions import InsecureRequestWarning
import urllib3
urllib3.disable_warnings(category=InsecureRequestWarning)
from flask import Flask
from markupsafe import escape
app = Flask(name)

@app.route("/consulta/<codigo_cliente>", method='GET')

def consultaSefaz(codigo_cliente):
    cabecalho = {"User-Agent": "Opera"}
    url = "https://internet-consultapublica.apps.sefaz.ce.gov.br/sintegra/consultar?tipdocumento=2&numcnpjcgf="
    urlcomp = url + codigo_cliente.replace('.', '').replace('/', '').replace('-', '')
    cnpj_req = requests.get(urlcomp, verify=False, headers=cabecalho)
    soup = BeautifulSoup(cnpj_req.text, "html.parser")
    enderecohtml = soup.find_all('table', {'id': 'enderecosintegara'})
    inf_comp = enderecohtml[1].contents[1].text
    infcomp_org = inf_comp.split('\n')
    situacao = infcomp_org[20]
    print("Situação Cadastral Vigente:", situacao)
    return situacao