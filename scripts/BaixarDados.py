import requests
import os
import zipfile
from urllib.parse import urljoin

def download_ans_data():
    # URLs atualizadas (baseado na estrutura real do site)
    base_url = "https://dadosabertos.ans.gov.br/FTP/PDA/"
    
    # Criar pastas
    os.makedirs("dados/demonstracoes", exist_ok=True)
    os.makedirs("dados/cadastrais", exist_ok=True)

    # ------ Parte 1: Baixar Operadoras Ativas (arquivo correto) ------
    operadoras_url = urljoin(base_url, "operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv")
    response = requests.get(operadoras_url)
    if response.status_code == 200:
        with open("dados/cadastrais/Relatorio_cadop.csv", "wb") as f:
            f.write(response.content)
        print("Operadoras baixadas com sucesso!")
    else:
        print(f"Erro ao baixar operadoras: Status {response.status_code}")

    # ------ Parte 2: Baixar Demonstrações Contábeis (4T2024 e 4T2023) ------
    quarters = [
        ("2023", "4T2023.zip"),  # Pasta 2023
        ("2024", "4T2024.zip")   # Pasta 2024
    ]

    for year, file_name in quarters:
        file_url = urljoin(base_url, f"demonstracoes_contabeis/{year}/{file_name}")
        response = requests.get(file_url)
        
        if response.status_code == 200:
            zip_path = f"dados/demonstracoes/{file_name}"
            with open(zip_path, "wb") as f:
                f.write(response.content)
            
            # Extrair ZIP
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall("dados/demonstracoes/")
            print(f"{file_name} extraído!")
        else:
            print(f"Erro ao baixar {file_name}: Status {response.status_code}")

if __name__ == "__main__":
    download_ans_data()