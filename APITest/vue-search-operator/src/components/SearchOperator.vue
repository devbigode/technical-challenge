<!-- src/components/SearchOperator.vue -->
<template>
  <div class="search-container">
    <div class="search-inputs">
      <!-- Input para busca por CNPJ -->
      <div class="search-field">
        <input
          v-model="cnpj"
          type="text"
          placeholder="Digite o CNPJ"
          class="input-field"
        />
        <button @click="searchByCNPJ" class="btn-search">Buscar por CNPJ</button>
      </div>

      <!-- Input para busca por nome -->
      <div class="search-field">
        <input
          v-model="name"
          type="text"
          placeholder="Digite o Nome da Operadora"
          class="input-field"
        />
        <button @click="searchByName" class="btn-search">Buscar por Nome</button>
      </div>
    </div>

    <!-- Exibição dos resultados -->
    <div v-if="operators.length">
      <ul class="results-list">
        <li v-for="operator in operators" :key="operator.CNPJ" class="result-item">
          {{ operator.Nome_Fantasia }} - {{ operator.Razao_Social }}
        </li>
      </ul>
    </div>
    <div v-else>
      <p class="no-results">Nenhuma operadora encontrada.</p>
    </div>
  </div>
</template>

<script src="./SearchOperator.js"></script>
<link rel="stylesheet" href="./SearchOperator.css" />
