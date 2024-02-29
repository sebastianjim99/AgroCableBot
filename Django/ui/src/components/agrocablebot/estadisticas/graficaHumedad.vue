<template>
  <div> 
    <div id="container5" class="container">
      <Bar :data="chartData" :options="chartOptions" v-if="loaded" />
      <div v-else>Cargando...</div>
    </div>
    <button @click="downloadChart">Descargar Gráfico</button>
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs';
import axios from 'axios';
import moment from 'moment';
import html2canvas from 'html2canvas';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
  TimeScale
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  BarElement, // Corrección: Registrar BarElement en lugar de Bar
  Title,
  Tooltip,
  Legend,
  TimeScale
);

export default {
  name: 'App',
  components: {
    Bar
  },
  data() {
    return {
      chartData: {},
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        aspectRatio: 2,
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              callback: function(value) {
                return value + '%';
              }
            }
          }
        }
      },
      loaded: false,
      api: `${process.env.VUE_APP_API_URL}`
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get(`${this.api}/api/Sensor_MQTT/`);
        this.processData(response.data);
        this.loaded = true;
      } catch (error) {
        console.error('Error al obtener los datos:', error);
      }
    },
    processData(data) {
      // Agrupar los datos por fecha y calcular el promedio de humedad para cada día
      const dailyHumidity = {};
      data.forEach(item => {
        const date = moment(item.timestamp).format('YYYY-MM-DD');
        if (!dailyHumidity[date]) {
          dailyHumidity[date] = [item.humedad];
        } else {
          dailyHumidity[date].push(item.humedad);
        }
      });

      const chartData = {
        labels: Object.keys(dailyHumidity),
        datasets: [
          {
            label: 'Humedad promedio',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1,
            data: Object.values(dailyHumidity).map(humidities => {
              const sum = humidities.reduce((acc, val) => acc + val, 0);
              return sum / humidities.length;
            }),
          }
        ]
      };

      // Actualizar los datos de la gráfica
      this.chartData = chartData;
    },
    async downloadChart() {
      try {
        await this.$nextTick(); // Espera a que el componente se haya renderizado completamente
        const chartContainer = document.getElementById('container5');
        if (chartContainer) {
          const canvas = await html2canvas(chartContainer);
          const imageData = canvas.toDataURL('image/png');

          // Para descargar la imagen en el dispositivo del cliente
          const downloadLink = document.createElement('a');
          downloadLink.href = imageData;
          downloadLink.download = 'grafico_historico_humedad.png';
          downloadLink.click();
        } else {
          console.error('El contenedor del gráfico no existe.');
        }
      } catch (error) {
        console.error('Error al descargar el gráfico:', error);
      }
    }
  }
};
</script>
