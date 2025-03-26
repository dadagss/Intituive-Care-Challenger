# main.py
from WebScraping import baixar_anexos
from TransfomacaoDados import processar_anexo_i


if __name__ == "__main__":
    zip_path = baixar_anexos()
    if zip_path:
        processar_anexo_i(zip_path, "Daniel") 
