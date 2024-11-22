# API de Consulta SEFAZ

API REST para consulta de situação cadastral de empresas na SEFAZ-CE (Secretaria da Fazenda do Estado do Ceará).

## 🚀 Endpoint

```
GET https://consulta-sefaz.onrender.com/consulta/{cnpj}
```

### Parâmetros

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| cnpj | string | CNPJ da empresa (com ou sem formatação) |

### Exemplo de Requisição

```bash
curl https://consulta-sefaz.onrender.com/consulta/00066559700193
```

### Respostas

#### Sucesso (200 OK)
```json
{
    "situacao": "ATIVO"
}
```

#### Erro (404 Not Found)
```json
{
    "error": "Estrutura HTML não encontrada"
}
```

#### Erro (500 Internal Server Error)
```json
{
    "error": "Mensagem detalhando o erro"
}
```

## ⚙️ Tecnologias Utilizadas

- Python
- Flask
- BeautifulSoup4
- Gunicorn

## 🔒 Limitações

- A API depende da disponibilidade do sistema SEFAZ-CE
- Consultas limitadas a empresas registradas no Ceará
- Rate limiting pode ser aplicado

## 📝 Notas

- CNPJ pode ser enviado com ou sem formatação
- A API retorna a situação cadastral atual da empresa
- Tempo de resposta pode variar conforme disponibilidade do sistema SEFAZ

## 🤝 Contribuições

Para contribuir com o projeto:
1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Envie um pull request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
