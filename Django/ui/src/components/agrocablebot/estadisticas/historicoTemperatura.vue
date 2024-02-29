<template>
  <div class="container">
    <div id="chart-container3">
      <Line :data="chartData" :options="options" v-if="loaded" />
      <div v-else>Cargando...</div>
    </div>
    <button @click="downloadChart">Descargar Gráfico</button>
  </div>
</template>

<script>
import { Line } from 'vue-chartjs';
import axios from 'axios';
import moment from 'moment';
import html2canvas from 'html2canvas';

export default {
  name: 'historico_temperatura',
  components: {
    Line
  },
  data() {
    return {
      chartData: {},
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
    }
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
      const dailyTemperatures = {};
      data.forEach(item => {
        const date = moment(item.timestamp).format('YYYY-MM-DD');
        if (!dailyTemperatures[date]) {
          dailyTemperatures[date] = [item.temperatura];
        } else {
          dailyTemperatures[date].push(item.temperatura);
        }
      });

      const chartData = {
        labels: Object.keys(dailyTemperatures),
        datasets: [
          {
            label: 'Temperatura promedio',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1,
            data: Object.values(dailyTemperatures).map(temperatures => {
              const sum = temperatures.reduce((acc, val) => acc + val, 0);
              return sum / temperatures.length;
            }),
          }
        ]
      };

      this.chartData = chartData;
    },
    async downloadChart() {
      try {
        await this.$nextTick(); // Espera a que el componente se haya renderizado completamente
        const chartContainer = document.getElementById('chart-container3');
        if (chartContainer) {
          const canvas = await html2canvas(chartContainer);
          const imageData = canvas.toDataURL('image/png');

          const downloadLink = document.createElement('a');
          downloadLink.href = imageData;
          downloadLink.download = 'grafico_historico_temperatura.png';
          downloadLink.click();
        } else {
          console.error('El contenedor del gráfico no existe.');
        }
      } catch (error) {
        console.error('Error al descargar el gráfico:', error);
      }
    }
  }
}
</script>
