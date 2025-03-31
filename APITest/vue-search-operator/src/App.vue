<template>
  <div class="search-container">
    <h1>Buscar Operadora</h1>
    <div class="search-inputs">
      <input v-model="filterByCNPJ" type="text" placeholder="Buscar por CNPJ" class="input-field">
      <input v-model="filterByName" type="text" placeholder="Buscar por Nome" class="input-field">
      <button @click="searchOperator" class="btn-search">Buscar</button>
    </div>
    <ul class="results-list" v-if="results.length">
      <li v-for="operator in results" :key="operator.CNPJ" class="result-item">
        <strong>{{ operator.Razao_Social }}</strong> - {{ operator.Nome_Fantasia }} (CNPJ: {{ operator.CNPJ }})
      </li>
    </ul>
    <p v-else-if="message" class="no-results">{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      filterByCNPJ: '',
      filterByName: '',
      results: [],
      message: ''
    };
  },
  methods: {
    async searchOperator() {
      try {
        const { filterByCNPJ, filterByName } = this;
        const url = `http://localhost:5000/?filterbycnpj=${filterByCNPJ}&filterbyname=${filterByName}`;
        const response = await axios.get(url);
        this.results = response.data;
        this.message = this.results.length ? '' : 'Nenhuma operadora encontrada.';
      } catch (error) {
        this.message = 'Erro ao buscar operadora.';
      }
    }
  }
};
</script>

<style>
.search-container {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  background-color: #2c3e50;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  font-family: 'Arial', sans-serif;
  color: #ecf0f1;
  text-align: center;
}

.search-inputs {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.input-field {

  padding: 12px;
  font-size: 16px;
  border: 1px solid #34495e;
  border-radius: 5px;
  background-color: #34495e;
  color: #ecf0f1;
}

.input-field:focus {
  border-color: #3498db;
  outline: none;
}

.btn-search {
  padding: 12px;
  background-color: #2980b9;
  color: white;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-search:hover {
  background-color: #1abc9c;
}

.results-list {
  list-style: none;
  padding: 0;
  margin-top: 20px;
}

.result-item {
  background-color: #34495e;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
}

.no-results {
  font-size: 18px;
  color: #7f8c8d;
}
</style>
