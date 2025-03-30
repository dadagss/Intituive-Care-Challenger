<!-- frontend/src/components/Search.vue -->
<template>
  <div>
    <h1>Busca de Operadoras</h1>
    <input v-model="searchTerm" @input="buscar" placeholder="Digite para buscar...">
    <ul>
      <li v-for="op in resultados" :key="op.registro_ans">
        {{ op.nome_fantasia }} - {{ op.razao_social }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      searchTerm: '',
      resultados: []
    }
  },
  methods: {
    buscar() {
      if(this.searchTerm.length > 2) {
        axios.get('http://localhost:5000/api/operadoras', {
          params: { q: this.searchTerm }
        })
        .then(response => this.resultados = response.data)
      }
    }
  }
}
</script>