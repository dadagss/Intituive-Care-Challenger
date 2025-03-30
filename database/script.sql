-- Selecionar o banco correto
USE ans;

-- Tabela de Operadoras Ativas 
CREATE TABLE IF NOT EXISTS operadoras (
    registro_ans VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(14), 
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(50),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep CHAR(8),      
    ddd CHAR(2),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    email VARCHAR(100),
    representante VARCHAR(100),
    cargo_representante VARCHAR(100),
    data_registro_ans DATE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabela de Despesas 
CREATE TABLE IF NOT EXISTS despesas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,                  
    operadora_id VARCHAR(20) NOT NULL,    
    cd_conta_contabil VARCHAR(20),      
    descricao VARCHAR(255),              
    vl_saldo_inicial DECIMAL(15,2),     
    vl_saldo_final DECIMAL(15,2),        
    FOREIGN KEY (operadora_id) 
        REFERENCES operadoras(registro_ans)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;