<template>

    <div class="container mt-3">
        <h1 class="divider-style mb-4"> <span> Descarga de datos</span> </h1> 
        <div class="row">
            <!-- Columna para selección de fechas -->
            <div class="col-md-6 col-sm-12">
                <div class="mb-3">
                    <label for="startDate" class="form-label">Fecha Inicio:</label>
                    <input id="startDate" class="form-control" type="date" v-model="startDate">
                </div>
                <div class="mb-3">
                    <label for="endDate" class="form-label">Fecha Fin:</label>
                    <input id="endDate" class="form-control" type="date" v-model="endDate">
                </div>
                <button class="btn btn-primary" @click="downloadData">Descargar Datos</button>
            </div>

            <!-- Columna para descarga de todos los datos -->
            <div class="col-md-6 col-sm-12">
                <div class="d-flex align-items-center justify-content-center" style="height: 100%;">
                    <button class="btn btn-primary" @click="downloadAllData">Descargar Todos los Datos</button>
                </div>
            </div>
        </div>
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

  <style scoped>
  

  </style>