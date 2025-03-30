from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import List, Optional
import os

# Cria a instância do FastAPI
app = FastAPI()

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Caminho do arquivo CSV
CSV_PATH = os.path.join('dados', 'cadastrais', 'Relatorio_cadop.csv')

# Verifica se o arquivo existe
if not os.path.exists(CSV_PATH):
    raise RuntimeError(f"Arquivo CSV não encontrado em: {os.path.abspath(CSV_PATH)}")

# Carrega os dados do CSV com tratamento robusto
try:
    # Carrega mantendo os nomes originais das colunas conforme mostrado no log
    df_operadoras = pd.read_csv(
        CSV_PATH,
        sep=';',
        encoding='utf-8',
        dtype={'CEP': str, 'DDD': str}
    )
    
    # Padroniza os nomes das colunas (baseado no seu log)
    df_operadoras.columns = df_operadoras.columns.str.lower()
    
    print("\nDados carregados com sucesso!")
    print(f"Total de operadoras: {len(df_operadoras)}")
    print("Colunas disponíveis:", df_operadoras.columns.tolist())
    print("\nPrimeira operadora como exemplo:")
    print(df_operadoras.iloc[0].to_dict())
    
except Exception as e:
    error_msg = f"\nERRO ao carregar dados: {str(e)}\n"
    print(error_msg)
    df_operadoras = pd.DataFrame()

@app.get("/operadoras/")
async def buscar_operadoras(
    termo: Optional[str] = None,
    uf: Optional[str] = None,
    limit: int = 10
) -> List[dict]:
    """
    Busca operadoras por termo textual e/ou UF
    """
    try:
        if df_operadoras.empty:
            raise HTTPException(
                status_code=503,
                detail="Serviço indisponível: Dados não carregados corretamente"
            )
        
        resultado = df_operadoras.copy()
        
        # Filtra por termo de busca (usando nomes de colunas em lowercase)
        if termo:
            mask = (
                resultado['razao_social'].str.contains(termo, case=False, na=False) |
                resultado['nome_fantasia'].str.contains(termo, case=False, na=False) |
                resultado['cidade'].str.contains(termo, case=False, na=False)
            )
            resultado = resultado[mask].copy()
        
        # Filtra por UF (usando nome de coluna em lowercase)
        if uf:
            resultado = resultado[resultado['uf'].str.upper() == uf.upper()].copy()
        
        # Ordena e limita resultados
        resultado = resultado.sort_values('nome_fantasia').head(limit)
        
        # Converte para dict e trata valores nulos
        return resultado.replace({pd.NA: None, float('nan'): None}).to_dict('records')
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao processar requisição: {str(e)}"
        )

@app.get("/test")
async def test_endpoint():
    """Endpoint para verificação do serviço"""
    sample_data = df_operadoras.iloc[0].to_dict() if not df_operadoras.empty else {}
    return {
        "status": "ok" if not df_operadoras.empty else "erro",
        "total_operadoras": len(df_operadoras),
        "sample_data": sample_data
    }

# Configuração específica para execução direta
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "backend:app",  # Esta é a forma correta de referenciar o app
        host="0.0.0.0",
        port=8000,
        reload=True
    )