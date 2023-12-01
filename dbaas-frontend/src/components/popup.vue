<!-- PopupModal.vue -->
<template>
    <div v-if="isVisible" class="box-border">
      <div class="modal-content">
        <p>{{ message }}</p>
        <button @click="closeModal">Close</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      message: String,
      isVisible: Boolean,
      onClose: Function,
    },
    methods: {
      closeModal() {
        this.onClose();
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your modal styles here */
  </style>
  