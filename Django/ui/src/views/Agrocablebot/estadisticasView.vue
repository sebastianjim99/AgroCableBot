<template>
    <div>
      <div class="">
        <navbar_monitoreo />
      </div>
  
      <div class="row mt-3">
        <div class="col-md-6 offset-3">
          <div class="card border border-dark">
            <div class="card-header bg-dark"></div>
            <div class="card-body">
              <canvas id="temperatureChart"></canvas>
            </div>
          </div>
        </div>
      </div>
  
      <section>
        <footer_imacuna />
      </section>
    </div>
</template>
 
<script>

import navbar_monitoreo from '/src/components/agrocablebot/base.vue'
import footer_imacuna from '/src/components/footer.vue'
import axios from 'axios';
import { Chart as ChartJS, Title, Tooltip, Legend, LineController, LinearScale, PointElement, LineElement, TimeScale } from 'chart.js'; // Agrega TimeScale a la lista de elementos importados
import 'chartjs-adapter-moment'; 
import moment from 'moment'; 

 ChartJS.register(Title, Tooltip, Legend, LineController, LinearScale, PointElement, LineElement, TimeScale); // Agrega TimeScale al registro de elementos
 
 ChartJS.defaults.plugins.tooltip.callbacks.label = function(context) {
   return context.dataset.label + ': ' + context.parsed.y + ' °C';
 };
 ChartJS.defaults.plugins.tooltip.displayColors = false;
 
 moment.updateLocale('en', {
   week: { dow: 1 } 
 });
 
 export default {
   components: {
     navbar_monitoreo,
     footer_imacuna,
   },
 
   data() {
     return {
       'api': `${process.env.VUE_APP_API_URL}`,
       temperaturaData: []
     }
   },
   async mounted() {
     await this.getTemperaturaData();
   },
   methods: {
     async getTemperaturaData() {
       try {
         const response = await axios.get(this.api + '/Sensor_MQTT/');
         if (response.data && Array.isArray(response.data)) {
           this.temperaturaData = response.data;
 
           const times = this.temperaturaData.map(data => moment(data.timestamp).format('HH:mm')); 
           const temperatures = this.temperaturaData.map(data => data.temperatura);
 
           const ctx = document.getElementById('temperatureChart').getContext('2d');
           new ChartJS(ctx, {
             type: 'line',
             data: {
               labels: times,
               datasets: [{
                 label: 'Temperatura vs Hora',
                 data: temperatures,
                 borderColor: 'rgb(75, 192, 192)',
                 borderWidth: 1
               }]
             },
             options: {
               scales: {
                 x: {
                   type: 'time',
                   time: {
                     parser: 'HH:mm', 
                     unit: 'hour',
                     displayFormats: {
                       hour: 'HH:mm'
                     }
                   }
                 },
                 y: {
                   beginAtZero: true
                 }
               }
             }
           });
         } else {
           console.error('Data format is incorrect:', response.data);
         }
       } catch (error) {
         console.error('Error fetching temperatura data:', error);
       }
     }
   }
 }
 </script>
 
 
  
<style scoped>
/* Estilos específicos si los necesitas */
</style>