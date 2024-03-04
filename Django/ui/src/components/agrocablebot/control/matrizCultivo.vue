<!-- POR AHORA NO ESTA EN USO -->


<template>
    <div class="row">
        <div class="col">
            <div class="container">
                <div class="row">
                    <!-- <div class="col-xxl-4" style="flex: 0 0 auto !important; width: 469px !important;">
                        <div style="text-align: center;">
                            <h2 class="divider-style"><span>Sensores</span></h2>
                        </div>
                        
                        <ul class="list-group">
                            <li class="list-group-item" style="background: var(--bs-body-bg);"><span>Planta #1</span></li>
                            <li class="list-group-item"><span>Humedad: 50%</span></li>
                            <li class="list-group-item"><span>Temperatura: 25°C</span></li>
                            <li class="list-group-item"><span>Otro dato</span></li>
                        </ul>
                        <div style="text-align: center;">
                            <h2 class="divider-style"><span>Ambiente</span></h2>
                        </div>
                        <ul class="list-group">
                            <li class="list-group-item" style="background: var(--bs-body-bg);"><span>Humedad: {{this.humedad}}</span></li>
                            <li class="list-group-item" style="background: var(--bs-body-bg);"><span>Temperatura: {{this.temperatura}}</span></li>
                            <li class="list-group-item" style="background: var(--bs-body-bg);"><span>Presión: {{this.presion}}</span></li>
                        </ul>
                        <div style="text-align: center;">
                            <h2 class="divider-style"><span>Giroscopio efector</span></h2>
                        </div>
                        <ul class="list-group">
                            <li class="list-group-item" style="background: var(--bs-body-bg);"><span>roll: {{this.giroscopio_pitch}}</span></li>
                            <li class="list-group-item" style="background: var(--bs-body-bg);"><span>Pitch: {{this.giroscopio_roll}}</span></li>
                            <li class="list-group-item" style="background: var(--bs-body-bg);"><span>yaw: {{this.giroscopio_yaw}}</span></li>
                        </ul>
                    </div> -->
                    <div class="col-6 col-xl-6 text-start text-bg-light">
                        <h1 style="text-align: center;padding: 12px;">Distribución del cultivo </h1>
                        <table>
                            <tbody>
                            <tr v-for="(fila, filaIndex) in matriz" :key="filaIndex">
                                <td v-for="(planta, columnaIndex) in fila" :key="columnaIndex" style="margin: auto;padding: initial;" width="100px" height="80px" @click="seleccionarPlanta(filaIndex, columnaIndex)" :style="{ backgroundColor: plantaSeleccionada && filaIndex === plantaSeleccionada.fila && columnaIndex === plantaSeleccionada.columna ? 'rgb(178,218,250, 0.5)' : '' }">
                                <div v-if="planta">
                                    <!-- Aquí puedes mostrar los datos de la planta, por ejemplo: -->
                                    <p>{{ planta.nombre }}</p>
                                    <img  :src="planta.cultivo.iconosPlantas" alt="Imagen de planta" style="margin: auto;padding: initial;" width="40px" height="40px">
                                </div>
                                <div v-else>
                                    {{ obtenerContadorPosicion(filaIndex, columnaIndex) }}
                                    <img  src="@/assets/iconos/sin_imagen.png" alt="Sin imagen de planta" style="margin: auto;padding: initial;" width="40px" height="40px">
                                </div>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>



<script>
import axios from 'axios'


export default{
    components:{
       
    },

    data(){

      return{
        'api': `${process.env.VUE_APP_API_URL}`,
        tipo_cultivo:[],
        cultivos:[],
        plantas:[],
        matriz: [],
        Datos_sensores: [],
        plantaSeleccionada: null,
        cultivoSeleccionado:null, 
        
      }
    },

    mounted(){
        this.obtenerDatosSensores();
        // Realizar las solicitudes HTTP para obtener datos
        //Lectura tipo de cultivo
        axios.get(this.api + 'api/tipoCultivo')
        .then(response =>{
            console.log("Tipo de cultivos")
            console.log(response.data)
            this.tipo_cultivo=response.data
        })
        .catch(error =>{
            console.log(error)
        })
        //Lectura de cultivo
        axios.get( this.api + '/api/cultivo')
        .then(response =>{
            console.log("Cultivos")
            console.log(response.data)
            this.cultivos=response.data
            this.initializeMatriz()
        })
        .catch(error =>{
            console.log(error)
        })
        //Lectura de plantas
        axios.get( this.api + '/api/plantas')
        .then(response =>{
            console.log("plantas")
            console.log(response.data)
            this.plantas=response.data
        })
        .catch(error =>{
            console.log(error)
        })
      
    },

    methods: {
        // Función para inicializar la matriz con los datos de las plantas
        initializeMatriz() {
            // Limpia la matriz para evitar duplicados si la función se llama varias veces
            this.matriz = [];
            // Crea una nueva matriz basada en la cantidad de plantas del cultivo seleccionado
            const cantidadDePlantas = this.cultivos.reduce((total, cultivo) => total + cultivo.cantidad, 0);
            const filas = Math.ceil(cantidadDePlantas / 9);

            for (let i = 0; i < filas; i++) {
            this.matriz.push(new Array(8).fill(null));
            }

            // Asignar las plantas a la matriz según el número de planta asignado
            let contadorPlanta = 0;
            this.cultivos.forEach(cultivo => {
            for (let i = 0; i < cultivo.cantidad; i++) {
                const fila = Math.floor(contadorPlanta / 9);
                const columna = contadorPlanta % 9;
                this.matriz[fila][columna] = {
                // nombre: cultivo.nombre,
                icono: cultivo.iconosPlantas,
                cultivo: cultivo
                };
                contadorPlanta++;
                }
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

        //  ---------- metodos de sensores----------------

        obtenerDatosSensores() {
            axios.get(this.api + '/api/Sensor_MQTT/')
            .then(response => {
                this.Datos_sensores=response.data
                this.obtenerUltimaActualizacion();
                console.log(this.Datos_sensores)
            })
            .catch(error => {
                console.error('Error al obtener los datos de los sensores:', error);
            });
        },
        obtenerUltimaActualizacion() {
            // Ordenar los datos por timestamp de forma descendente para obtener la última actualización primero
            const ultimaActualizacion = this.Datos_sensores.sort((a, b) => b.id - a.id)[0];
            
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
        enviarMensajeMQTT() {
            const csrfToken = window.csrfToken;

            const message = {
                interface: 'send_aio'
            };
            // Enviar una solicitud POST al servidor Django
            axios.post('http://127.0.0.1:8000/sensar-mqtt/', message, {
                headers: {
                    'X-CSRFToken': csrfToken // Incluye el token CSRF en la cabecera de la solicitud
                }
            })
            .then(() => {
                console.log('Mensaje MQTT enviado correctamente');
                this.obtenerDatosSensores()
                this.obtenerUltimaActualizacion();
            })
            .catch(error => {
                console.error('Error al enviar mensaje MQTT:', error);
            });

        },
        
    },  

}

</script>



<style>

    .divider-style:before {
    content: "";
    display: block;
    border-top: solid 1px black;
    width: 100%;
    height: 1px;
    position: absolute;
    top: 50%;
    z-index: 1;
    }

    .divider-style {
    margin-top: 0px;
    position: relative;
    margin-right: 40px;
    margin-left: 40px;
    }

    .divider-style span {
    background: #fff;
    padding: 0 20px;
    position: relative;
    z-index: 5;
    }

    @media (min-width:768px) {
    .col-md-12 {
    flex: 0 0 auto;
    width: 100%;
  }
}

.row > * {
  flex-shrink: 0;
  width: 100%;
  max-width: 100%;
  padding-right: calc(var(--bs-gutter-x) * .5);
  padding-left: calc(var(--bs-gutter-x) * .5);
  margin-top: var(--bs-gutter-y);
}

.navbar {
  --bs-navbar-padding-x: 0;
  --bs-navbar-padding-y: 0.5rem;
  --bs-navbar-color: rgba(var(--bs-emphasis-color-rgb), 0.65);
  --bs-navbar-hover-color: rgba(var(--bs-emphasis-color-rgb), 0.8);
  --bs-navbar-disabled-color: rgba(var(--bs-emphasis-color-rgb), 0.3);
  --bs-navbar-active-color: rgba(var(--bs-emphasis-color-rgb), 1);
  --bs-navbar-brand-padding-y: 0.3125rem;
  --bs-navbar-brand-margin-end: 1rem;
  --bs-navbar-brand-font-size: 1.25rem;
  --bs-navbar-brand-color: rgba(var(--bs-emphasis-color-rgb), 1);
  --bs-navbar-brand-hover-color: rgba(var(--bs-emphasis-color-rgb), 1);
  --bs-navbar-nav-link-padding-x: 0.5rem;
  --bs-navbar-toggler-padding-y: 0.25rem;
  --bs-navbar-toggler-padding-x: 0.75rem;
  --bs-navbar-toggler-font-size: 1.25rem;
  --bs-navbar-toggler-icon-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%2833, 37, 41, 0.75%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
  --bs-navbar-toggler-border-color: rgba(var(--bs-emphasis-color-rgb), 0.15);
  --bs-navbar-toggler-border-radius: var(--bs-border-radius);
  --bs-navbar-toggler-focus-width: 0.25rem;
  --bs-navbar-toggler-transition: box-shadow 0.15s ease-in-out;
  position: relative;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  padding: var(--bs-navbar-padding-y) var(--bs-navbar-padding-x);
}





    


</style>