<template> 
  <div class="container" >
    <div class="row" style="padding-bottom: 30px;">
      <!-- Tabla de cultivos -->
      <div class="col-md-2">
        <h2>Lista de cultivos</h2>
        <table class="table table-hover">
          <thead >
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
      <!-- Información del tipo de cultivo -->
      <div class="col-md-9">
        <div class="tipo-cultivo" v-if="tipoDeCultivoSeleccionado">

          <div class="row">
            <div class="col-md-auto" style="max-width: 660px;"  >
              <h2>Información del tipo de cultivo</h2>
              <div style="max-height: 300px; overflow-y: auto;">  
                <table class="table" >
                  <tbody>
                    <tr>
                      <td><strong>Nombre:</strong></td>
                      <td>{{ tipoDeCultivoSeleccionado.nombre }}</td>
                    </tr>
                    <tr>
                      <td><strong>Descripción:</strong></td>
                      <td style="text-align: justify;" >{{ tipoDeCultivoSeleccionado.descripcion }}</td>
                    </tr>
                    <tr>
                      <td><strong>Preparación del suelo</strong></td>
                      <td style="text-align: justify;" >{{ tipoDeCultivoSeleccionado.preparacionSuelo }}</td>
                    </tr>
                    <tr>
                      <td><strong>Riego</strong></td>
                      <td style="text-align: justify;" >{{ tipoDeCultivoSeleccionado.riego }}</td>
                    </tr>
                    <tr>
                      <td><strong>Control de Malezas</strong></td>
                      <td style="text-align: justify;" >{{ tipoDeCultivoSeleccionado.controlMalezas }}</td>
                    </tr>
                    <tr>
                      <td><strong>Control de plagas y Enfermedades</strong></td>
                      <td style="text-align: justify;" >{{ tipoDeCultivoSeleccionado.controlPlagasyEnfermedades }}</td>
                    </tr>
                    <tr>
                      <td><strong>Fertilización</strong></td>
                      <td style="text-align: justify;" >{{ tipoDeCultivoSeleccionado.fertilizacion }}</td>
                    </tr>
                    <tr>
                      <td><strong>Fertilización</strong></td>
                      <td style="text-align: justify;" >{{ tipoDeCultivoSeleccionado.moniteroRegistro }}</td>
                    </tr>
                    <!-- Agregar más información aquí -->
                  </tbody>
                </table>
              </div>
            </div>
            <div class="col-md-4">
              <h2>Estimados</h2>
              <table class="table">
                <tbody>
                  <tr>
                    <td><strong>Germinación (mín-máx):</strong></td>
                    <td>{{ tipoDeCultivoSeleccionado.estimadoGerminacionMin }} - {{ tipoDeCultivoSeleccionado.estimadoGerminacionMax }} días</td>
                  </tr>
                  <tr>
                    <td><strong>Cosecha (mín-máx):</strong></td>
                    <td >{{ tipoDeCultivoSeleccionado.estimadoCosechaMin }} - {{ tipoDeCultivoSeleccionado.estimadoCosechaMax }} días</td>
                  </tr>
                  <tr>
                    <td><strong>Temperatura (mín-máx)  </strong></td>
                    <td>{{ tipoDeCultivoSeleccionado.temperaturaOptimaMin }} - {{ tipoDeCultivoSeleccionado.temperaturaOptimaMax }} °C </td>
                  </tr>
                  <tr>
                    <td><strong>Profundidad de siembra </strong></td>
                    <td>{{ tipoDeCultivoSeleccionado.profundidadSiembra }} Cm </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div v-else>
          <p class="text-muted">Por favor, seleccione un cultivo de la lista.</p>
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
  