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