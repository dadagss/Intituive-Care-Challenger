import pdfplumber
import pandas as pd
import zipfile
import os

def processar_anexo_i(zip_path: str, seu_nome: str):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            if 'Anexo I.pdf' not in zip_ref.namelist():
                raise FileNotFoundError("Anexo I.pdf não encontrado no ZIP")
            
            zip_ref.extract('Anexo I.pdf')

        todas_linhas = []
        colunas = []

        with pdfplumber.open('Anexo I.pdf') as pdf:
            for page in pdf.pages:
                # Ajustar área de extração
                bbox = page.bbox if page.width > 1000 else (0, 0, page.width, page.height)
                
                table = page.crop(bbox).extract_table({
                    "vertical_strategy": "lines",
                    "horizontal_strategy": "lines",
                    "explicit_vertical_lines": page.curves + page.edges,
                    "explicit_horizontal_lines": page.curves + page.edges,
                    "snap_tolerance": 10,
                    "join_tolerance": 10
                })
                
                if table:
                    if not colunas:
                        colunas = [cell.replace('\n', ' ').strip() if cell else '' for cell in table[0]]
                        table = table[1:]
                    
                    for row in table:
                        cleaned_row = [cell.replace('\n', ' ').strip() if cell else '' for cell in row]
                        if len(cleaned_row) == len(colunas):
                            todas_linhas.append(cleaned_row)

        if len(todas_linhas) == 0:
            raise ValueError("Nenhum dado extraído do PDF")

        mapeamento = {
            'OD': 'Odontológico',
            'AMB': 'Ambulatorial'
        }
        novas_colunas = [mapeamento.get(col, col) for col in colunas]

        df = pd.DataFrame(todas_linhas, columns=novas_colunas)

        # Remover linhas totalmente vazias
        df = df.dropna(how='all')
        df = df[df.ne('').any(axis=1)]

        csv_filename = 'Rol_Procedimentos.csv'
        zip_final = f'Teste_{seu_nome}.zip'
        
        df.to_csv(
            csv_filename,
            index=False,
            sep=';',
            encoding='utf-8-sig',
            quoting=1,  
            quotechar='"'
        )
        
        with zipfile.ZipFile(zip_final, 'w') as zipf:
            zipf.write(csv_filename)
        
        for arquivo in [csv_filename, 'Anexo I.pdf']:
            if os.path.exists(arquivo):
                os.remove(arquivo)
        
        print(f"Arquivo {zip_final} gerado com sucesso!")
        return zip_final

    except Exception as e:
        print(f"Erro no processamento: {str(e)}")
        for arquivo in ['Anexo I.pdf', 'Rol_Procedimentos.csv']:
            if os.path.exists(arquivo):
                os.remove(arquivo)
        return None
    
        
if __name__ == "__main__":
    processar_anexo_i()