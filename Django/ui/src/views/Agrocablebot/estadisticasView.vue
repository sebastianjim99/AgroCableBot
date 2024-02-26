<template>
    
    <div class="">
        <navbar_monitoreo />
    </div>


    <div class="row mt-3" >
        <div class="col-md-6 offset-3">
            <div class="card border border-dark">
                <div class="card-header bg-dark">

                </div>
                <div class="card-body">
                    <Bar :data="chartData" :options="chartOptions" />
                </div>

            </div>

        </div>

    </div>


    <section>
        <footer_imacuna />
    </section>


</template>


<script>
import navbar_monitoreo from '/src/components/agrocablebot/base.vue'
import footer_imacuna from '/src/components/footer.vue'
import axios from 'axios';
import { Bar,  } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default{
    extends: Bar,
    components:{
        navbar_monitoreo,
        footer_imacuna,
        Bar,
       
    },
    data(){
       return{
           'api': `${process.env.VUE_APP_API_URL}`,
            chartData: { 
                labels: [],
                datasets: [{
                    label: 'Valores de Sensores',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                    data: [],
                }],
            },
            chartOptions:{
                responsive:true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                    },
                },
            }
       }
    },
     mounted() {
        this.obtenerDatosSensores();
    },
    methods: {
        obtenerDatosSensores() {
            axios.get(this.api + '/Sensor_MQTT/')
            .then(response => {
                    this.procesarDatos(response.data);
                    console.log(response.data)
            })
            .catch(error => {
                console.error('Error al obtener los datos de los sensores:', error);
            });
        },
        procesarDatos(datosSensores) {
            console.log('Datos de sensores recibidos:', datosSensores);

            // Filtrar solo los registros que contienen el campo "temperatura"
            const datosTemperatura = datosSensores.filter(sensor => typeof sensor.temperatura !== 'undefined');

            // Obtener todos los valores de temperatura en un array
            const valoresTemperatura = datosTemperatura.map(sensor => sensor.temperatura);

            console.log('Valores de temperatura:', valoresTemperatura);

            // Actualizar los datos del gráfico para mostrar los valores de temperatura
            this.chartData.labels = datosTemperatura.map(sensor => sensor.timestamp);
            this.chartData.datasets[0].label = 'Temperatura'; // Cambia la etiqueta del conjunto de datos
            this.chartData.datasets[0].data = valoresTemperatura; // Usar los valores de temperatura
        },



    }
}
</script>