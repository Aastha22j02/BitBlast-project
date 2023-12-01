// store.js
import { defineStore } from 'pinia';
 
export const useInputStore = defineStore('input', {
  state: () => ({
    selectedType: '',
    selectedProvider: '',
    selectedTools:'',
  }),
  actions: {
    setType(value) {
      this.selectedType = value;
    },
    setProvider(value) {
      this.selectedProvider = value;
    },
    setTools(value) {
      this.selectedTools = value;
    },
  },
});