from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify
import re
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/consulta/<codigo_cliente>", methods=['GET'])



def consultaSefaz(codigo_cliente):
    try:
        cabecalho = {"User-Agent": "Opera"}
        url = f"https://consultapublica.sefaz.ce.gov.br/sintegra/consultar?tipdocumento=2&numcnpjcgf={codigo_cliente}"
        
        cnpj_req = requests.get(
            url, 
            verify=False, 
            headers=cabecalho,
            timeout=10
        )
        cnpj_req.raise_for_status()
        
        soup = BeautifulSoup(cnpj_req.text, "html.parser")
        enderecohtml = soup.find_all('table', {'id': 'enderecosintegara'})
        
        
        if not enderecohtml or len(enderecohtml) < 2:
            return jsonify({"situacao": "CLIENTE NAO ENCONTRADO"}), 404
        
        inf_comp = enderecohtml[1].contents[1].text
        infcomp_org = inf_comp.split('\n')
        
       
        if len(infcomp_org) < 21:
            return jsonify({"error": "DADOS INSUFICIENTES"}), 404
        
        situacao = infcomp_org[20]
        
        return jsonify({"situacao": situacao})
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    except IndexError as e:
        return jsonify({"error": "Erro ao processar dados"}), 500
    except Exception as e:
        return jsonify({"error": "Erro desconhecido"}), 5000
        

if __name__ == '__main__':
    app.run(debug=True, port=3002)