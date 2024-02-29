<template>
    <div class="container">
      <div class="row">
        <!-- Tabla de cultivos -->
        <div class="col-md-4">
          <h2>Lista de cultivos</h2>
          <table class="table">
            <thead>
              <tr>
                <th>Nombre del cultivo</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="cultivo in listaDeCultivos" :key="cultivo.id" @click="seleccionarCultivo(cultivo)">
                <td>{{ cultivo.nombre }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- Tabla de información del tipo de cultivo seleccionado -->
        <div class="col-md-8">
          <h2>Información del tipo de cultivo</h2>
          <div v-if="tipoDeCultivoSeleccionado">
            <button @click="ocultarTabla">Ocultar Tabla</button>
            <table class="table">
              <tbody>
                <tr>
                  <td>Nombre</td>
                  <td>{{ tipoDeCultivoSeleccionado.nombre }}</td>
                </tr>
                <tr>
                  <td>Descripción</td>
                  <td>{{ tipoDeCultivoSeleccionado.descripcion }}</td>
                </tr>
                <tr>
                  <td>Preparación del suelo</td>
                  <td>{{ tipoDeCultivoSeleccionado.preparacionSuelo }}</td>
                </tr>
                <tr>
                  <td>Riego</td>
                  <td>{{ tipoDeCultivoSeleccionado.riego }}</td>
                </tr>
                <tr>
                  <td>Control de Malezas</td>
                  <td>{{ tipoDeCultivoSeleccionado.controlMalezas }}</td>
                </tr>
                <tr>
                  <td>Control de plagas y Enfermedades</td>
                  <td>{{ tipoDeCultivoSeleccionado.controlPlagasyEnfermedades }}</td>
                </tr>
                <tr>
                  <td>Fertilización</td>
                  <td>{{ tipoDeCultivoSeleccionado.fertilizacion }}</td>
                </tr>
                <tr>
                  <td>Monitoreo y Registro</td>
                  <td>{{ tipoDeCultivoSeleccionado.moniteroRegistro }}</td>
                </tr>
                <tr>
                  <td>Estimado mínimo para germinación [días]</td>
                  <td>{{ tipoDeCultivoSeleccionado.estimadoGerminacionMin }}</td>
                </tr>
                <tr>
                  <td>Estimado máximo para germinación [días]</td>
                  <td>{{ tipoDeCultivoSeleccionado.estimadoGerminacionMax }}</td>
                </tr>
                <tr>
                  <td>Estimado mínimo para cosechar [días]</td>
                  <td>{{ tipoDeCultivoSeleccionado.estimadoCosechaMin }}</td>
                </tr>
                <tr>
                  <td>Estimado máximo para cosechar [días]</td>
                  <td>{{ tipoDeCultivoSeleccionado.estimadoCosechaMax }}</td>
                </tr>
                <tr>
                  <td>Temperatura mínima [°C]</td>
                  <td>{{ tipoDeCultivoSeleccionado.temperaturaOptimaMin }}</td>
                </tr>
                <tr>
                  <td>Temperatura máxima [°C]</td>
                  <td>{{ tipoDeCultivoSeleccionado.temperaturaOptimaMax }}</td>
                </tr>
                <tr>
                  <td>Profundidad de siembra [cm]</td>
                  <td>{{ tipoDeCultivoSeleccionado.profundidadSiembra }}</td>
                </tr>
                <!-- Agrega más filas para otras propiedades del tipo de cultivo según sea necesario -->
              </tbody>
            </table>
          </div>
          <div v-else>
            <p>Por favor, seleccione un cultivo de la lista.</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        'api' : `${process.env.VUE_APP_API_URL}`,
        listaDeCultivos: [],
        tipoDeCultivoSeleccionado: null
      };
    },
    mounted() {
      this.obtenerListaDeCultivos();
    },
    methods: {
      obtenerListaDeCultivos() {
        axios.get(this.api + '/api/tipoCultivo')
          .then(response => {
            this.listaDeCultivos = response.data;
          })
          .catch(error => {
            console.error('Error al obtener la lista de cultivos:', error);
          });
      },
      seleccionarCultivo(cultivo) {
        axios.get(this.api + `/api/tipoCultivo/${cultivo.id}`)
          .then(response => {
            this.tipoDeCultivoSeleccionado = response.data;
          })
          .catch(error => {
            console.error('Error al obtener la información del tipo de cultivo seleccionado:', error);
          });
      },
      ocultarTabla() {
        this.tipoDeCultivoSeleccionado = null;
      }
    }
  };
  </script>
  
  <style scoped>
  /* Estilos específicos para el componente */
  </style>
  