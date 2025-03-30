USE ans;
-- Carrega operadoras
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Relatorio_cadop.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
    registro_ans, 
    cnpj, 
    razao_social, 
    nome_fantasia, 
    modalidade, 
    logradouro, 
    numero, 
    complemento, 
    bairro, 
    cidade, 
    uf, 
    cep, 
    ddd, 
    telefone, 
    fax, 
    email, 
    representante, 
    cargo_representante, 
    @data_registro_ans
)
SET data_registro_ans = STR_TO_DATE(@data_registro_ans, '%d/%m/%Y');

-- Carrega despesas (4T2024)
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/4T2024.csv'
INTO TABLE despesas
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
    data, 
    reg_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
SET data = STR_TO_DATE(data, '%Y-%m-%d');

-- Carrega despesas (4T2023)
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/4T2023.csv'
INTO TABLE despesas
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
    data, 
    reg_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
SET data = STR_TO_DATE(data, '%Y-%m-%d');