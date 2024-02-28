<template>
  <div class="container">
    <Bar :data="chartData" :options="chartOptions" v-if="loaded" />
    <div v-else>Cargando...</div>
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs';
import axios from 'axios';
import moment from 'moment';
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
  BarElement,
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
        const response = await axios.get(`${this.api}/Sensor_MQTT/`);
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
    }
  }
};
</script>
