<template>
    <div>
      <div class="container">
        <input type="date" v-model="selectedDay" @change="fetchData" class="custom-input">
        <div v-if="!selectedDay">Seleccionar fecha para graficar datos del giroscopio de un día en específico</div>
        <div v-else id="chart-container-giroscopio">
          <Line :data="chartData" :options="chartOptions" v-if="loaded" />
          <div v-else>Cargando...</div>
        </div>
      </div>
      <button @click="downloadChart" class="btn btn-primary">Descargar Gráfico</button>
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
    LineElement, // Cambiado a LineElement para el gráfico de líneas
    Title,
    Tooltip,
    Legend,
    TimeScale
  );
  
  export default {
    name: 'graficaGiroscopio',
    components: {
      Line
    },
    data() {
      return {
        chartData: {
          labels: [],
          datasets: []
        },
        selectedDay: moment().format('YYYY-MM-DD'),
        chartOptions: {
          responsive: true,
          maintainAspectRatio: false,
          aspectRatio: 2,
          scales: {
            y: {
              beginAtZero: false, // No comenzar necesariamente en cero
              ticks: {
                callback: function(value) {
                  return value.toFixed(2) + '°'; // Formato con dos decimales y unidad
                }
              }
            }
          }
        },
        loaded: false,
        api: `${process.env.VUE_APP_API_URL}`,
      };
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
          const response = await axios.get(`${this.api}/api/Sensor_MQTT/`);
          this.processData(response.data);
          this.loaded = true;
        } catch (error) {
          console.error('Error al obtener los datos:', error);
        }
      },
      processData(data) {
        const filteredData = data.filter(item => moment(item.timestamp).format('YYYY-MM-DD') === this.selectedDay);
  
        if (filteredData.length === 0) {
          this.chartData = {
            labels: [],
            datasets: []
          }; // Manejar el caso donde no hay datos para el día seleccionado
          return;
        }
  
        const allValues = filteredData.flatMap(item => [item.giroscopio_roll, item.giroscopio_pitch, item.giroscopio_yaw]);
        const minY = Math.min(...allValues);
        const maxY = Math.max(...allValues);
  
        this.chartData = {
          labels: filteredData.map(item => moment(item.timestamp).format('HH:mm')),
          datasets: [
            {
              label: 'Giroscopio Roll',
              backgroundColor: 'rgba(255, 99, 132, 0.2)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1,
              fill: false,
              data: filteredData.map(item => item.giroscopio_roll),
            },
            {
              label: 'Giroscopio Pitch',
              backgroundColor: 'rgba(54, 162, 235, 0.2)',
              borderColor: 'rgba(54, 162, 235, 1)',
              borderWidth: 1,
              fill: false,
              data: filteredData.map(item => item.giroscopio_pitch),
            },
            {
              label: 'Giroscopio Yaw',
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1,
              fill: false,
              data: filteredData.map(item => item.giroscopio_yaw),
            }
          ]
        };
  
        // Actualizar las opciones del gráfico con los nuevos límites del eje Y
        this.chartOptions.scales.y.min = minY - 5; // Añadir un margen
        this.chartOptions.scales.y.max = maxY + 5; // Añadir un margen
      },
      async downloadChart() {
        try {
          await this.$nextTick(); // Espera a que el componente se haya renderizado completamente
          const chartContainer = document.getElementById('chart-container-giroscopio');
          if (chartContainer) {
            const canvas = await html2canvas(chartContainer);
            const imageData = canvas.toDataURL('image/png');
  
            // Para descargar la imagen en el dispositivo del cliente
            const downloadLink = document.createElement('a');
            downloadLink.href = imageData;
            downloadLink.download = 'grafico_giroscopio_diaEspecifico.png';
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
  
  <style>
  .custom-input {
    width: 30%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box;
    text-align: center;
  }
  </style>
  