<template>
  <div>
    <div class="container" id="chart-container6">
      <div class="row justify-content-between">
        <div class="col-md-5">
          <input class="form-control" type="date" v-model="startDate" @change="fetchData" />
        </div>
        <div class="col-md-5 mt-3 mt-md-0">
          <input class="form-control" type="date" v-model="endDate" @change="fetchData" />
        </div>
      </div>
      <div v-if="!startDate || !endDate">Seleccionar rango de fechas para graficar humedad</div>
      <div v-else>
        <Line :data="chartData" :options="options" v-if="loaded" />
        <div v-else>Cargando...</div>
      </div>
    </div>
    <button class="btn btn-primary" @click="downloadChart">Descargar Gráfico</button>
  </div>
</template>

<script>
import { Line } from 'vue-chartjs';
import axios from 'axios';
import moment from 'moment';
import html2canvas from 'html2canvas';

export default {
  name: 'graficaHumedad',
  components: {
    Line
  },
  data() {
    return {
      chartData: {},
      startDate: null,
      endDate: null,
      options: {
        responsive: true,
        maintainAspectRatio: false,
        aspectRatio: 2,
        scales: {
          y: {
            beginAtZero: false,
            ticks: {
              callback: function(value) {
                return value + '%';
              }
            }
          }
        }
      },
      loaded: false,
      api: `${process.env.VUE_APP_API_URL}`,
    }
  },
  watch: {
    startDate(newVal) {
      if (newVal && this.endDate) {
        this.fetchData();
      }
    },
    endDate(newVal) {
      if (newVal && this.startDate) {
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
      const filteredData = data.filter(item => {
        const timestamp = moment(item.timestamp).format('YYYY-MM-DD');
        return timestamp >= this.startDate && timestamp <= this.endDate;
      });

      const dailyAverageHumidity = {};
      filteredData.forEach(item => {
        const date = moment(item.timestamp).format('YYYY-MM-DD');
        if (!dailyAverageHumidity[date]) {
          dailyAverageHumidity[date] = [item.humedad];
        } else {
          dailyAverageHumidity[date].push(item.humedad);
        }
      });

      const chartData = {
        labels: Object.keys(dailyAverageHumidity),
        datasets: [
          {
            label: 'Humedad promedio',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1,
            data: Object.values(dailyAverageHumidity).map(humidities => {
              const sum = humidities.reduce((acc, val) => acc + val, 0);
              return sum / humidities.length;
            }),
          }
        ]
      };

      this.chartData = chartData;
    },
    async downloadChart() {
      try {
        await this.$nextTick();
        const chartContainer = document.getElementById('chart-container6');
        if (chartContainer) {
          const canvas = await html2canvas(chartContainer);
          const imageData = canvas.toDataURL('image/png');

          const downloadLink = document.createElement('a');
          downloadLink.href = imageData;
          downloadLink.download = 'grafico_humedad_rangoFechas.png';
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
