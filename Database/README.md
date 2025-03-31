# Banco de Dados - Estrutura e Queries

## Criação de queries para estruturar tabelas necessárias para o arquivo csv

### Tabela operadoras:

    CREATE TABLE operadoras (
    Registro_ANS VARCHAR(100) PRIMARY KEY,
    CNPJ VARCHAR(20),
    Razao_Social VARCHAR(500),
    Nome_Fantasia VARCHAR(500),
    Modalidade VARCHAR(100),
    Logradouro VARCHAR(255),
    Numero VARCHAR(20),
    Complemento VARCHAR(100),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    UF CHAR(2),
    CEP VARCHAR(10),
    DDD VARCHAR(2),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Endereco_eletronico VARCHAR(100),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(100),
    Regiao_de_Comercializacao VARCHAR(50),
    Data_Registro_ANS DATE
    );

### Tabela demonstracoes_contabeis:

    CREATE TABLE demonstracoes_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    DATA DATE,
    REG_ANS VARCHAR(100),
    CD_CONTA_CONTABIL VARCHAR(50),
    DESCRICAO VARCHAR(1000),
    VL_SALDO_INICIAL DECIMAL(15,2),
    VL_SALDO_FINAL DECIMAL(15,2),
    PERIODO_TRIMESTRAL VARCHAR(7),
    FOREIGN KEY (REG_ANS) REFERENCES operadoras(Registro_ANS)
    );

## Queries para importar o conteúdo dos arquivos preparados, atentando para o encoding correto

    LOAD DATA LOCAL INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\1T2023.csv'
    INTO TABLE demonstracoes_contabeis
    CHARACTER SET utf8mb4
    FIELDS TERMINATED BY ';'
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @vl_inicial, @vl_final)
    SET
    VL_SALDO_INICIAL = REPLACE(@vl_inicial, ',', '.'),
    VL_SALDO_FINAL = REPLACE(@vl_final, ',', '.'),
    PERIODO_TRIMESTRAL = '2023-1';

#### Observação: Repita o processo para todos os arquivos que deseja importar.

## Queries analíticas:

### Top 10 Operadoras - Último Trimestre

    SELECT
    dc.REG_ANS,
    op.Nome_Fantasia,
    dc.DESCRICAO,
    dc.VL_SALDO_FINAL
    FROM demonstracoes_contabeis dc
    JOIN operadoras op ON dc.REG_ANS = op.Registro_ANS
    WHERE dc.DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
    AND dc.PERIODO_TRIMESTRAL = '2024-4'
    ORDER BY dc.VL_SALDO_FINAL DESC
    LIMIT 10;

### Top 10 Operadoras - Último Ano

    SELECT
    dc.REG_ANS,
    op.Nome_Fantasia,
    dc.DESCRICAO,
    dc.PERIODO_TRIMESTRAL,
    SUM(dc.VL_SALDO_FINAL) AS Total_Despesas
    FROM demonstracoes_contabeis dc
    JOIN operadoras op ON dc.REG_ANS = op.Registro_ANS
    WHERE dc.DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
    AND dc.PERIODO_TRIMESTRAL LIKE '2024-%'
    GROUP BY dc.REG_ANS, op.Nome_Fantasia, dc.PERIODO_TRIMESTRAL
    ORDER BY Total_Despesas DESC
    LIMIT 10;

## Versões Utilizadas
- **MySQL Workbench:** 8.0.34
- **MySQL Server:** 8.0.33