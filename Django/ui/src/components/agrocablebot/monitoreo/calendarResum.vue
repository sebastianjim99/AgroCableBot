<template>
<section>
    <div class="container text-center py-4 py-xl-5">
        <div class="row mb-5">
            <div class="col">
                <h2>Resumen del calendario</h2>
            </div>
        </div>
        <div class="row gy-4">
            <div class="col-xxl-4">
                <div class="d-flex flex-column align-items-center">
                    <img src="@/assets/iconos/reigo.png" class="img-fluid mb-3" alt="Ultimo Riego" style="width: 100px; height: 100px;">
                    <div>
                        <h4>Ultimo Riego</h4>
                        <p>Fecha: {{ this.fechaActualizacion }} </p>
                        <p>Hora: {{ this.horaActualizacion }}</p>
                    </div>
                </div>
            </div>
            <div class="col-xxl-4">
                <div class="d-flex flex-column align-items-center">
                    <img src="@/assets/iconos/presion.png" class="img-fluid mb-3" alt="Ultimo censado de presión" style="width: 100px; height: 100px;">
                    <div>
                        <h4>Ultimo censado de presión</h4>
                        <p>Fecha: {{ this.fechaActualizacion }} </p>
                        <p>Hora: {{ this.horaActualizacion }}</p>
                        <p>Presion: {{ this.presion }}</p>
                    </div>
                </div>
            </div>
            <div class="col-xxl-4">
                <div class="d-flex flex-column align-items-center">
                    <img src="@/assets/iconos/temperatura.png" class="img-fluid mb-3" alt="Ultimo censado de Temperatura" style="width: 100px; height: 100px;">
                    <div>
                        <h4>Ultimo censado de Temperatura</h4>
                        <p>Fecha: {{ this.fechaActualizacion }} </p>
                        <p>Hora: {{ this.horaActualizacion }}</p>
                        <p>Temperatura: {{ this.temperatura }}</p>
                    </div>
                </div>
            </div>
            <div class="col-xxl-4">
                <div class="d-flex flex-column align-items-center">
                    <img src="@/assets/iconos/humedad.png" class="img-fluid mb-3" alt="Ultimo censado de humedad" style="width: 100px; height: 100px;">
                    <div>
                        <h4>Ultimo censado de humedad</h4>
                        <p>Fecha: {{ this.fechaActualizacion }} </p>
                        <p>Hora: {{ this.horaActualizacion }}</p>
                        <p>Humedad: {{ this.humedad }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>


</template>

<script>

import axios from 'axios'

export default {
    name: "Calendar_resum",
    data(){
      return{
        'api': `${process.env.VUE_APP_API_URL}`,
        Datos_sensores: [],
        temperatura: null,
        humedad: null,
        timestamp: null,
        fechaActualizacion:null,
        horaActualizacion:null
      }
    },

    mounted(){
        this.obtenerDatosSensores();
    },

    methods:{

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

            console.log(this.temperatura)

        },
    },
}
</script>