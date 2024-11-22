from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify
import re

app = Flask(__name__)

@app.route("/consulta/<codigo_cliente>", methods=['GET'])


def consultaSefaz(codigo_cliente):

    try:
        cabecalho = {"User-Agent": "Opera"}
        url = f"https://internet-consultapublica.apps.sefaz.ce.gov.br/sintegra/consultar?tipdocumento=2&numcnpjcgf={codigo_cliente}"
        
        cnpj_req = requests.get(
            url, 
            verify=False, 
            headers=cabecalho,
            timeout=10
        )
        cnpj_req.raise_for_status()
        
        soup = BeautifulSoup(cnpj_req.text, "html.parser")
        enderecohtml = soup.find_all('table', {'id': 'enderecosintegara'})
        
        inf_comp = enderecohtml[1].contents[1].text
        infcomp_org = inf_comp.split('\n')
        situacao = infcomp_org[20]
        
        return jsonify({"situacao": situacao})
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=3002)