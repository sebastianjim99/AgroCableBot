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
                            <td v-for="(planta, columnaIndex) in fila" :key="columnaIndex" style="padding:1px;" @click="seleccionarPlanta(filaIndex, columnaIndex)"  :style="{ backgroundColor: plantaSeleccionada && filaIndex === plantaSeleccionada.fila && columnaIndex === plantaSeleccionada.columna ? 'rgb(178,218,250, 0.5)' : '' }">
                                <div class="text-center">
                                    <p v-if="planta">{{ planta.nombre }}</p>
                                    <img  class="img-planta"  style=" margin:0 8px 8px 8px;" v-if="planta" :src="planta.cultivo.iconosPlantas" alt="Imagen de planta" >
                                    <p v-else>{{ obtenerContadorPosicion(filaIndex, columnaIndex) }}
                                    <img class="img-planta" src="@/assets/iconos/sin_imagen.png"  alt="Sin imagen de planta" ></p>
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
              <div>
                <h1 class="text-center mb-4">Alertas</h1>
                <ul class="list-group">
                    <!-- Alerta por alta temperatura -->
                    <li class="list-group-item" v-if="this.temperatura > 40" >
                        Alerta de Temperatura Alta: {{ this.temperatura }}°C
                    </li>
                    <!-- Alerta por baja humedad -->
                    <li class="list-group-item" v-if="this.humedad < 50" >
                        Alerta de Humedad Baja: {{ this.humedad }}%
                    </li>
                    <!-- Mensaje si no hay alertas adicionales -->
                    <li class="list-group-item" v-if="temperatura <= 40 && humedad >= 50">
                        No hay alertas 
                    </li>
                </ul>
              </div>
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
        cultivoSeleccionado:null,
        Datos_sensores: [],
        temperatura: null,
        humedad: null,
        
      }
    },

    mounted(){
      // Realizar las solicitudes HTTP para obtener datos
      //Lectura tipo de cultivo
      axios.get(this.api + '/api/tipoCultivo').then(response =>{
        this.tipo_cultivo=response.data
      })
      .catch(error =>{
        console.log(error)
      })
      //Lectura de cultivo
      axios.get(this.api + '/api/cultivo')
      .then(response =>{
        this.cultivos=response.data
      })
      .catch(error =>{
        console.log(error)
      })
      //Lectura de plantas
      axios.get(this.api + '/api/plantas')
      .then(response =>{
        this.plantas=response.data
        this.initializeMatriz()
      })
      .catch(error =>{
        console.log(error)
      })

      this.obtenerDatosSensores();
      
    },

    methods: {
      // Función para inicializar la matriz con los datos de las plantas
      initializeMatriz() {
        for (let i = 0; i < 9; i++) {
          this.matriz.push(new Array(9).fill(null));
        }
        // Asignar las plantas a la matriz según el número de planta asignado
        this.plantas.forEach(planta => {
          const fila = Math.floor((planta.numeroPlanta - 1) / 9);
          const columna = (planta.numeroPlanta - 1) % 9;
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
      },

      obtenerDatosSensores() {
          axios.get(this.api + '/api/Sensor_MQTT/')
          .then(response => {
              this.Datos_sensores=response.data
              this.obtenerUltimaActualizacion();
          })
          .catch(error => {
              console.error('Error al obtener los datos de los sensores:', error);
          });
      },

      obtenerUltimaActualizacion() {

            // Ordenar los datos por timestamp de forma descendente para obtener la última actualización primero
            const ultimaActualizacion = this.Datos_sensores.sort((a, b) => b.id - a.id)[0];

            // Obtener el timestamp de la última actualización
            const timestamp = ultimaActualizacion.timestamp;

            // Convertir el timestamp a un objeto Date de JavaScript
            const fechaHora = new Date(timestamp);

            // Extraer componentes de fecha
            const dia = fechaHora.getDate();
            const mes = fechaHora.getMonth() + 1; // Los meses van de 0 a 11, sumamos 1
            const anio = fechaHora.getFullYear();

            // Formatear la fecha en DD/MM/AAAA
            const fechaFormateada = `${dia}/${mes}/${anio}`;

            // Extraer componentes de hora
            const horas = fechaHora.getHours();
            const minutos = fechaHora.getMinutes();
            const segundos = fechaHora.getSeconds();

            // Formatear la hora en formato de 24 horas HH:MM:SS
            const horaFormateada = `${horas}:${minutos}:${segundos}`;

            // Asignar los datos formateados a las variables de la interfaz de usuario
            this.timestamp = `${fechaFormateada} ${horaFormateada}`;
            this.fechaActualizacion= `${fechaFormateada}`;
            this.horaActualizacion= `${horaFormateada}`;
            
            // Actualizar las variables de la interfaz de usuario con los datos de la última actualización
            this.acelerometro_roll = ultimaActualizacion.acelerometro_roll;
            this.acelerometro_pitch = ultimaActualizacion.acelerometro_pitch;
            this.acelerometro_yaw = ultimaActualizacion.acelerometro_yaw;
            
            this.giroscopio_pitch = ultimaActualizacion.giroscopio_pitch;
            this.giroscopio_roll = ultimaActualizacion.giroscopio_roll;
            this.giroscopio_yaw = ultimaActualizacion.giroscopio_yaw;

            this.humedad = ultimaActualizacion.humedad;
            this.presion = ultimaActualizacion.presion;
            this.temperatura = ultimaActualizacion.temperatura;

      },
    

    }
    
}
</script>

<style>

</style>
