import requests
from bs4 import BeautifulSoup
import zipfile
import os
from urllib.parse import urljoin
import re

def baixar_anexos():
    # 1.1 Acesso ao site
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    
    try:
        # Configurar headers para simular navegador
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # 1.2 Encontrar os links dos PDFs
        print("Acessando o site para encontrar os anexos...")
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Verifica erros HTTP
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Lista para armazenar os links dos anexos
        pdf_links = []
        
        # Procurar por todos os links na página
        for link in soup.find_all('a'):
            href = link.get('href', '')
            link_text = link.text.strip().lower()
            
            # Verificação mais precisa usando regex
            if re.search(r'anexo\s+i(?!i)', link_text) and href.lower().endswith('.pdf'):
                pdf_links.append(('Anexo I.pdf', href))
            elif re.search(r'anexo\s+ii', link_text) and href.lower().endswith('.pdf'):
                pdf_links.append(('Anexo II.pdf', href))
        
        if not pdf_links:
            raise Exception("Não foram encontrados os links para os anexos PDF")
        
        # 1.2 Download dos PDFs
        arquivos_baixados = []
        for nome_arquivo, pdf_url in pdf_links:
            try:
                # Converter URL relativa para absoluta se necessário
                if not pdf_url.startswith('http'):
                    pdf_url = urljoin(url, pdf_url)
                
                print(f"Baixando {nome_arquivo} de {pdf_url}...")
                
                # Fazer o download do PDF
                response = requests.get(pdf_url, headers=headers, stream=True)
                response.raise_for_status()
                
                # Salvar o arquivo
                with open(nome_arquivo, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                arquivos_baixados.append(nome_arquivo)
                print(f"{nome_arquivo} baixado com sucesso!")
            
            except Exception as e:
                print(f"Erro ao baixar {nome_arquivo}: {str(e)}")
                continue
        
        # 1.3 Compactar os arquivos
        if arquivos_baixados:
            zip_filename = "Anexos.zip"
            print(f"Criando arquivo compactado {zip_filename}...")
            
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                for arquivo in arquivos_baixados:
                    zipf.write(arquivo)
            
            # Remover os arquivos PDF temporários
            for arquivo in arquivos_baixados:
                try:
                    os.remove(arquivo)
                except:
                    pass
            
            print("Processo concluído com sucesso!")
            return zip_filename
        else:
            raise Exception("Nenhum arquivo PDF foi baixado com sucesso")
    
    except Exception as e:
        print(f"Erro durante a execução: {str(e)}")
        return None

# Executar a função principal
if __name__ == "__main__":
    baixar_anexos()