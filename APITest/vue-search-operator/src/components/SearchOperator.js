// src/components/SearchOperator.js
export default {
  data() {
    return {
      cnpj: "",
      operators: [],
    };
  },
  methods: {
    async searchOperator() {
      const response = await fetch(
        `http://localhost:5000/?filterbycnpj=${this.cnpj}`
      );
      const data = await response.json();
      this.operators = data;
    },
  },
};
