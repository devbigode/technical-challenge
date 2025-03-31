import tabula
import pandas as pd
import os
import csv
import zipfile

def extractTables(pdfPath):
    tables = tabula.read_pdf(pdfPath, pages='all', multiple_tables=True, lattice=True, stream=False)

    if not tables:
        raise ValueError("Nenhuma tabela foi extraída do PDF.")

    print(f"Total de tabelas extraídas: {len(tables)}")
    return tables

def cleanMergeTables(tables):
    # Concatena todas as tabelas
    dfMerge = pd.concat(tables, ignore_index=True).copy()

    # Remove colunas 'Unnamed' e linhas totalmente vazias
    dfClean = dfMerge.loc[:, ~dfMerge.columns.str.contains("Unnamed")].copy()

    dfClean.dropna(how='all', inplace=True)

    dfClean.columns = (
        dfClean.columns
        .str.replace('\r', ' ')
        .str.replace('\n', ' ')
        .str.strip()
    )

    for col in dfClean.columns:
        dfClean[col] = (
            dfClean[col]
            .astype(str)
            .replace(['nan', 'None', '<NA>'], 'NA')
            .str.replace('\r', ' ')
            .str.replace('\n', ' ')
            .str.strip()
        )

    return dfClean

def saveZip(df, name):
    csvFile = "rol_de_procedimentos.csv"

    df.to_csv(csvFile, index=False, encoding='utf-8-sig', quoting=csv.QUOTE_MINIMAL, quotechar='"')

    zip = f"Teste_{name}.zip"

    # Compacta o arquivo CSV
    with zipfile.ZipFile(zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csvFile)

    # Remove o arquivo CSV temporário
    os.remove(csvFile)

    print(f"Arquivo {zip} criado com sucesso!")