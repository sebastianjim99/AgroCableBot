<template>
    <div>
      <div id="container5" class="container">
        <Line :data="chartData" :options="chartOptions" v-if="loaded" />
        <div v-else>Cargando...</div>
      </div>
      <button class="btn btn-primary" @click="downloadChart">Descargar Gráfico</button>
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
    name: 'App',
    components: {
      Line
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
        // Agrupar los datos por fecha y calcular el promedio de giroscopio para cada día
        const dailyGyroscope = {};
        data.forEach(item => {
          const date = moment(item.timestamp).format('YYYY-MM-DD');
          if (!dailyGyroscope[date]) {
            dailyGyroscope[date] = {
              roll: [item.giroscopio_roll],
              pitch: [item.giroscopio_pitch],
              yaw: [item.giroscopio_yaw]
            };
          } else {
            dailyGyroscope[date].roll.push(item.giroscopio_roll);
            dailyGyroscope[date].pitch.push(item.giroscopio_pitch);
            dailyGyroscope[date].yaw.push(item.giroscopio_yaw);
          }
        });
  
        const averagedData = Object.values(dailyGyroscope).map(gyro => ({
          roll: gyro.roll.reduce((acc, val) => acc + val, 0) / gyro.roll.length,
          pitch: gyro.pitch.reduce((acc, val) => acc + val, 0) / gyro.pitch.length,
          yaw: gyro.yaw.reduce((acc, val) => acc + val, 0) / gyro.yaw.length,
        }));
  
        // Encontrar el valor mínimo y máximo entre todos los datos promediados
        const allValues = averagedData.flatMap(gyro => [gyro.roll, gyro.pitch, gyro.yaw]);
        const minY = Math.min(...allValues);
        const maxY = Math.max(...allValues);
  
        // Configurar los datos de la gráfica
        const chartData = {
          labels: Object.keys(dailyGyroscope),
          datasets: [
            {
              label: 'Giroscopio Roll promedio',
              backgroundColor: 'rgba(255, 99, 132, 0.2)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1,
              fill: false,
              data: averagedData.map(gyro => gyro.roll),
            },
            {
              label: 'Giroscopio Pitch promedio',
              backgroundColor: 'rgba(54, 162, 235, 0.2)',
              borderColor: 'rgba(54, 162, 235, 1)',
              borderWidth: 1,
              fill: false,
              data: averagedData.map(gyro => gyro.pitch),
            },
            {
              label: 'Giroscopio Yaw promedio',
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1,
              fill: false,
              data: averagedData.map(gyro => gyro.yaw),
            }
          ]
        };
  
        // Actualizar las opciones del gráfico con los nuevos límites del eje Y
        this.chartOptions.scales.y.min = minY - 5; // Añadir un margen
        this.chartOptions.scales.y.max = maxY + 5; // Añadir un margen
  
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
            downloadLink.download = 'grafico_giroscopio.png';
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
  