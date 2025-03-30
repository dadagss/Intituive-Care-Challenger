-- Verifica e corrige a estrutura da tabela antes de criar índices

USE ans;

-- 1. VERIFICAR E CORRIGIR A ESTRUTURA DA TABELA (se necessário)
SET @dbname = DATABASE();
SET @tablename = 'despesas';
SET @columnname = 'operadora_id';

-- Verifica se a coluna operadora_id existe
SET @preparedStatement = (SELECT IF(
    (
        SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS
        WHERE table_schema = @dbname
        AND table_name = @tablename
        AND column_name = @columnname
    ) > 0,
    'SELECT 1', -- Coluna já existe
    CONCAT('ALTER TABLE ', @tablename, ' CHANGE COLUMN reg_ans ', @columnname, ' VARCHAR(20) NOT NULL')
));
PREPARE alterTableIfNeeded FROM @preparedStatement;
EXECUTE alterTableIfNeeded;
DEALLOCATE PREPARE alterTableIfNeeded;

-- 2. CRIAR ÍNDICES (após garantir que a coluna existe)
SET @indexname = 'idx_despesas_operadora';
SET @preparedStatement = (SELECT IF(
    (
        SELECT COUNT(*) FROM INFORMATION_SCHEMA.STATISTICS
        WHERE table_schema = @dbname
        AND table_name = @tablename
        AND index_name = @indexname
    ) > 0,
    'SELECT 1', -- Índice já existe
    CONCAT('CREATE INDEX ', @indexname, ' ON ', @tablename, '(', @columnname, ')')
));
PREPARE createIndexIfNotExists FROM @preparedStatement;
EXECUTE createIndexIfNotExists;
DEALLOCATE PREPARE createIndexIfNotExists;

-- 3. CONSULTAS ANALÍTICAS (com colunas corrigidas)
-- Top 10 Operadoras no Último Trimestre
SELECT 
    o.registro_ans,
    o.nome_fantasia AS operadora,
    o.uf,
    SUM(d.vl_saldo_final) AS total_despesas,
    FORMAT(SUM(d.vl_saldo_final), 2, 'de_DE') AS total_formatado,
    COUNT(*) AS qtde_registros,
    MAX(d.data) AS data_mais_recente
FROM 
    despesas d
JOIN 
    operadoras o ON d.operadora_id = o.registro_ans
WHERE 
    d.descricao LIKE '%EVENTOS/%SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    AND d.data >= DATE_SUB((SELECT MAX(data) FROM despesas), INTERVAL 3 MONTH)
GROUP BY 
    o.registro_ans, o.nome_fantasia, o.uf
ORDER BY 
    total_despesas DESC
LIMIT 10;
