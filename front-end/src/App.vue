<template>
  <div class="container">
    <h1>Busca de Operadoras de Saúde</h1>
    
    <div class="search-box">
      <input 
        v-model="termoBusca" 
        placeholder="Digite nome, razão social ou cidade..."
        @keyup.enter="buscarOperadoras"
      >
      
      <select v-model="ufFiltro">
        <option value="">Todos os estados</option>
        <option v-for="uf in ufs" :value="uf" :key="uf">{{ uf }}</option>
      </select>
      
      <button @click="buscarOperadoras">Buscar</button>
    </div>
    
    <div v-if="carregando" class="loading">Carregando...</div>
    
    <div v-if="erro" class="error">{{ erro }}</div>
    
    <div class="results">
      <div v-for="op in operadoras" :key="op.registro_ans" class="card">
        <h3>{{ op.nome_fantasia || 'Sem nome fantasia' }}</h3>
        <p><strong>Razão Social:</strong> {{ op.razao_social }}</p>
        <p><strong>Registro ANS:</strong> {{ op.registro_ans }}</p>
        <p><strong>Localização:</strong> {{ op.cidade }}/{{ op.uf }}</p>
        <p><strong>Contato:</strong> {{ op.telefone }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      termoBusca: '',
      ufFiltro: '',
      operadoras: [],
      carregando: false,
      erro: null,
      ufs: [
        'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 
        'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 
        'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
      ]
    }
  },
  methods: {
    async buscarOperadoras() {
      this.carregando = true
      this.erro = null
      
      try {
        const params = new URLSearchParams()
        if (this.termoBusca) params.append('termo', this.termoBusca)
        if (this.ufFiltro) params.append('uf', this.ufFiltro)
        
        const response = await fetch(`http://localhost:8000/operadoras/?${params}`)
        
        if (!response.ok) {
          throw new Error('Erro ao buscar operadoras')
        }
        
        this.operadoras = await response.json()
      } catch (error) {
        this.erro = error.message
      } finally {
        this.carregando = false
      }
    }
  }
}
</script>

<style>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.search-box {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.search-box input {
  flex: 1;
  padding: 10px;
  font-size: 16px;
}

.search-box select, .search-box button {
  padding: 10px;
  font-size: 16px;
}

.results {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.card {
  border: 1px solid #ddd;
  padding: 15px;
  border-radius: 5px;
  background: #f9f9f9;
}

.loading {
  padding: 20px;
  text-align: center;
  font-style: italic;
  color: #666;
}

.error {
  padding: 20px;
  text-align: center;
  color: #d32f2f;
  background: #ffebee;
  border-radius: 5px;
}
</style>