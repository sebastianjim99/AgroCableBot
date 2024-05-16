<template>
    <div>
        <input type="date" v-model="startDate">
        <input type="date" v-model="endDate">
        <button @click="downloadData">Descargar Datos</button>
        <button @click="downloadAllData">Descargar Todos los Datos</button>
    </div>
</template>
  
<script>
    export default {
        data() {
            return {
                startDate: '',
                endDate: ''
            };  
        },
        methods: {
            downloadData() {
                const url = `//localhost:8000/download-data/?start=${this.startDate}&end=${this.endDate}`;
                window.open(url, '_blank');
            },
            downloadAllData() {
                const url = '//localhost:8000/download-all-data/'; // Asegúrate de que esta URL es accesible según tu configuración de Django
                window.open(url, '_blank');
            }
        }
  }
  </script>