<template>
    <div>
      <div class="container">
        <input type="date" v-model="selectedDay" @change="fetchData" />
        <div v-if="!selectedDay">Seleccionar fecha para graficar Humedad de un día en especifico</div>
        <div v-else id="chart-container1">
          <Line :data="chartData" :options="options" v-if="loaded" />
          <div v-else>Cargando...</div>
        </div>
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
    name: 'graficaHumedad',
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
    mounted() {
      if (this.selectedDay) {
        this.fetchData();
      }
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
          const response = await axios.get(`${this.api}/Sensor_MQTT/`);
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
              label: 'Humedad',
              backgroundColor: 'rgba(54, 162, 235, 0.2)',
              borderColor: 'rgba(48, 137, 93, 1)',
              borderWidth: 1,
              data: filteredData.map(item => item.humedad),
            }
          ]
        };
      },
      async downloadChart() {
        try {
          await this.$nextTick(); // Espera a que el componente se haya renderizado completamente
          const chartContainer = document.getElementById('chart-container1');
          if (chartContainer) {
            const canvas = await html2canvas(chartContainer);
            const imageData = canvas.toDataURL('image/png');
  
            // Para descargar la imagen en el dispositivo del cliente
            const downloadLink = document.createElement('a');
            downloadLink.href = imageData;
            downloadLink.download = 'grafico_humedad_diaEspecifico.png';
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
  