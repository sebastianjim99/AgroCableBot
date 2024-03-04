<template>
    
  <section>
    <div class="container py-4 py-xl-5">
        <div class="row">
            <!-- Distribución del cultivo -->
            <div class="col-12 col-xl-6">
                <h1 class="text-center mb-4">Distribución del cultivo</h1>
                <table class="table">
                    <tbody>
                        <tr v-for="(fila, filaIndex) in matriz" :key="filaIndex">
                            <td v-for="(planta, columnaIndex) in fila" :key="columnaIndex" class="position-relative" @click="seleccionarPlanta(filaIndex, columnaIndex)"  :style="{ backgroundColor: plantaSeleccionada && filaIndex === plantaSeleccionada.fila && columnaIndex === plantaSeleccionada.columna ? 'rgb(178,218,250, 0.5)' : '' }">
                                <div class="text-center">
                                    <p v-if="planta">{{ planta.nombre }}</p>
                                    <img v-if="planta" :src="planta.cultivo.iconosPlantas" alt="Imagen de planta" width="40" height="40">
                                    <p v-else>{{ obtenerContadorPosicion(filaIndex, columnaIndex) }}
                                    <img src="@/assets/iconos/sin_imagen.png" alt="Sin imagen de planta" width="40" height="40"></p>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <!-- Datos del cultivo seleccionado y alertas -->
            <div class="col-12 col-xl-6 mt-4 mt-xl-0">
                <h1 class="text-center mb-4">Datos del cultivo seleccionado</h1>
                <div v-if="cultivoSeleccionado" class="mb-4">
                    <ul class="list-group">
                        <li class="list-group-item">Tipo de Cultivo: {{cultivoSeleccionado.tipoCultivo.nombre}}</li>
                        <li class="list-group-item">Fecha de siembra: {{cultivoSeleccionado.fechaSiembra}}</li>
                        <li class="list-group-item">Temperatura optima: {{cultivoSeleccionado.tipoCultivo.temperaturaOptimaMin}} - {{cultivoSeleccionado.tipoCultivo.temperaturaOptimaMax}} °C</li>
                        <li class="list-group-item">Estimado para cosechar: {{cultivoSeleccionado.tipoCultivo.estimadoCosechaMin}} - {{cultivoSeleccionado.tipoCultivo.estimadoCosechaMax}} Días</li>
                        <li class="list-group-item">Estimado de germinación: {{cultivoSeleccionado.tipoCultivo.estimadoGerminacionMin}} - {{cultivoSeleccionado.tipoCultivo.estimadoGerminacionMax}} Días</li>
                        <li class="list-group-item">Profundidad de siembra: {{ cultivoSeleccionado.tipoCultivo.profundidadSiembra }} cm</li>
                    </ul>
                </div>
                <div v-else>
                    <p class="text-center mb-4">Haz clic en una planta para ver los detalles del cultivo.</p>
                </div>
                <h1 class="text-center mb-4">Alertas</h1>
                <ul class="list-group">
                    <li class="list-group-item">Batería baja</li>
                </ul>
            </div>
        </div>
    </div>
</section>


</template>


<script>
  import axios from 'axios'
  export default {
    name: "CultivoVue",
    data(){
      return{
        'api': `${process.env.VUE_APP_API_URL}`,
        tipo_cultivo:[],
        cultivos:[],
        plantas:[],
        matriz: [],
        plantaSeleccionada: null,
        cultivoSeleccionado:null
        
      }
    },

    mounted(){
      // Realizar las solicitudes HTTP para obtener datos
      //Lectura tipo de cultivo
      axios.get(this.api + '/api/tipoCultivo')
      .then(response =>{
        console.log("Tipo de cultivos")
        console.log(response.data)
        this.tipo_cultivo=response.data
      })
      .catch(error =>{
        console.log(error)
      })
      //Lectura de cultivo
      axios.get(this.api + '/api/cultivo')
      .then(response =>{
        console.log("Cultivos")
        console.log(response.data)
        this.cultivos=response.data
      })
      .catch(error =>{
        console.log(error)
      })
      //Lectura de plantas
      axios.get(this.api +  '/api/plantas')
      .then(response =>{
        console.log("plantas")
        console.log(response.data)
        this.plantas=response.data
        this.initializeMatriz()
      })
      .catch(error =>{
        console.log(error)
      })
      
    },

    methods: {
      // Función para inicializar la matriz con los datos de las plantas
      initializeMatriz() {
        for (let i = 0; i < 8; i++) {
          this.matriz.push(new Array(8).fill(null));
        }

        // Asignar las plantas a la matriz según el número de planta asignado
        this.plantas.forEach(planta => {
          const fila = Math.floor((planta.numeroPlanta - 1) / 8);
          const columna = (planta.numeroPlanta - 1) % 8;
          this.matriz[fila][columna] = planta;  
        }); 
      },
      

      obtenerContadorPosicion(filaIndex, columnaIndex) {
        // Calcula el contador de posición basado en los índices de fila y columna
        return filaIndex * this.matriz[0].length + columnaIndex + 1;
      },
      // Seleccion de la planta mediante click y despliegue de informacion
      seleccionarPlanta(filaIndex, columnaIndex) {
        this.plantaSeleccionada = { fila: filaIndex, columna: columnaIndex };
        const planta = this.matriz[filaIndex][columnaIndex];
        this.cultivoSeleccionado = planta ? planta.cultivo : null;
      }

    }
    
}
</script>

<style>

</style>
