# Testes de Nivelamento - Intuitive Care

## Descrição

Este repositório contém a solução para os testes de nivelamento v.250321 da **Intuitive Care**. Os testes foram desenvolvidos utilizando **Python**, **SQL (MySQL)** e **Vue.js**, cobrindo as seguintes áreas:

- **Web Scraping**: Coleta e compactação de arquivos PDF.
- **Transformação de Dados**: Extração e manipulação de tabelas.
- **Banco de Dados**: Estruturação, importação e análise de dados.
- **API**: Desenvolvimento de interface e endpoint para busca textual.

---

## Estrutura do Repositório

```plaintext
.
├── .github/                 # Arquivos de configuração do repositório
├── dados/                   # Dados baixados dos sites oficiais
├── database/                # Scripts SQL para criação e manipulação do banco
├── frontend/                # Código do front-end em Vue.js
├── scripts/                 # Scripts Python para Web Scraping e Transformação de Dados
├── postman.json             # Coleção do Postman para testes da API
└── README.md                # Documentação do projeto
```


## 1. Teste de Web Scraping
Objetivo:
Acessar o site da ANS.

Baixar os arquivos Anexo I e Anexo II (formato PDF).

Compactar os arquivos baixados em um único .zip.

Tecnologias Utilizadas:
Python (requests, BeautifulSoup, PyPDF2, zipfile).

```
cd scripts
python web_scraping.py

```
## 2. Teste de Transformação de Dados
Objetivo:
Extrair os dados da tabela Rol de Procedimentos e Eventos em Saúde do PDF Anexo I.

Converter a tabela extraída para .csv.

Substituir as abreviações OD e AMB pelas descrições completas.

Compactar o .csv gerado em um arquivo "Teste_{seu_nome}.zip".

Tecnologias Utilizadas:
Python (pdfplumber, pandas, zipfile).
```
cd scripts
python transformar_dados.py
```

## 3. Teste de Banco de Dados   
Teste de Banco de Dados
Objetivo:
Baixar e processar os dados financeiros das operadoras de saúde da ANS.

Criar tabelas no banco de dados.

Importar os dados para o banco.

Realizar consultas analíticas.

Tecnologias Utilizadas:
MySQL 8

SQL (CREATE TABLE, INSERT, SELECT)

```
-- Criar banco de dados
CREATE DATABASE ans_data;

-- Executar os scripts em database/
SOURCE database/script.sql;
SOURCE database/import.sql;
SOURCE database/Querys.sql;
```

## 4. Teste de API
Objetivo:
Criar um servidor em Python (Flask/FastAPI) para buscar operadoras por nome.

Criar uma interface Vue.js para consulta.

Fornecer uma coleção no Postman para testes.

Tecnologias Utilizadas:
Back-end: Python (Flask/FastAPI)

Front-end: Vue.js

API Testing: Postman

## 5. Teste de API
Objetivo:
Criar um servidor em Python (Flask/FastAPI) para buscar operadoras por nome.

Criar uma interface Vue.js para consulta.

Fornecer uma coleção no Postman para testes.

Tecnologias Utilizadas:
Back-end: Python (Flask/FastAPI)

Front-end: Vue.js

API Testing: Postman

```
# Executar servidor API
cd scripts
python backend.py

# Executar Front-end
cd frontend
npm install
npm run dev
```

## Resultados Esperados
- Web Scraping realizado com sucesso.

- Tabela extraída e estruturada corretamente.

- Banco de dados populado e consultas analíticas funcionando.

- API acessível para busca textual de operadoras.

- Interface web funcional para interação com a API.

## Contato
Caso tenha alguma dúvida ou sugestão, entre em contato:
📧 Email: [daniel_sgsilva@hotmail.com]
🔗 LinkedIn: [Perfil](www.linkedin.com/in/daniel-silva-devops)
