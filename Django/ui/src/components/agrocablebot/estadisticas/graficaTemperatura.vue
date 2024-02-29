<template>
  <div class="container">
    <input type="date" v-model="selectedDay" @change="fetchData" />
    <div v-if="!selectedDay">Seleccionar fecha para graficar temperatura de un día en especifico</div>
    <div v-else id="chart-container">
      <div v-if="loaded" >
        <Line :data="chartData" :options="options" />
      </div>
      <div v-else>Cargando...</div>
    </div>
    <button @click="downloadChart" v-if="loaded">Descargar Gráfico</button>
  </div>
</template>

<script>
import { Line } from 'vue-chartjs';
import axios from 'axios';
import moment from 'moment';
import html2canvas from 'html2canvas';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  TimeScale
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  TimeScale
);

export default {
  name: 'graficaTemperatura',
  components: {
    Line
  },
  data() {
    return {
      chartData: {},
      selectedDay: moment().format('YYYY-MM-DD'),
      options: {
        responsive: true,
        maintainAspectRatio: false,
        aspectRatio: 2,
        scales: {
          y: {
            beginAtZero: false,
            ticks: {
              callback: function(value) {
                return value + '°C';
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
  watch: {
    selectedDay(newVal) {
      if (newVal) {
        this.fetchData();
      }
    }
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
      const filteredData = data.filter(item => moment(item.timestamp).format('YYYY-MM-DD') === this.selectedDay);
      this.chartData = {
        labels: filteredData.map(item => moment(item.timestamp).format('HH:mm')),
        datasets: [
          {
            label: 'Temperatura',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 200, 0, 1)',
            borderWidth: 1,
            data: filteredData.map(item => item.temperatura),
          }
        ]
      };
    },
    async downloadChart() {
      try {
        await this.$nextTick(); // Espera a que el componente se haya renderizado completamente
        const chartContainer = document.getElementById('chart-container');
        if (chartContainer) {
          const canvas = await html2canvas(chartContainer);
          const imageData = canvas.toDataURL('image/png');

          // Para descargar la imagen en el dispositivo del cliente
          const downloadLink = document.createElement('a');
          downloadLink.href = imageData;
          downloadLink.download = 'grafico_temperatura_diaEspecifico.png';
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
