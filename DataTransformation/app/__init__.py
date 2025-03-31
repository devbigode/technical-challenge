from utils.utils import extractTables, cleanMergeTables, saveZip

def main():
    pdfPath = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    name = "Guilherme"

    try:
        # Extrai tabelas do PDF
        tables = extractTables(pdfPath)

        # Processa e limpa os dados
        df = cleanMergeTables(tables)

        # Mapeia as colunas a serem modificadas
        abbreviations = {
            'OD': 'Outros Procedimentos',
            'AMB': 'Ambulatório'
        }
        # Troca os nomes das colunas
        df.replace(abbreviations, inplace=True)

        # Converte DataFrame para csv e compacta
        saveZip(df, name)

        # Mostra uma amostra dos dados processados
        print("\nAmostra dos dados processados:")
        print(df.head())

    except Exception as e:
        print(f"\nErro durante o processamento: {str(e)}")

if __name__ == "__main__":
    main()