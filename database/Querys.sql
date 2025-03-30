-- Último trimestre
SELECT o.nome_fantasia, SUM(d.valor) AS total
FROM demonstracoes d
JOIN operadoras o ON d.cnpj = o.cnpj
WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
AND d.data >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH)
GROUP BY o.nome_fantasia
ORDER BY total DESC
LIMIT 10;

-- Último ano
SELECT o.nome_fantasia, SUM(d.valor) AS total
FROM demonstracoes d
JOIN operadoras o ON d.cnpj = o.cnpj
WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
AND d.data >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY o.nome_fantasia
ORDER BY total DESC
LIMIT 10;