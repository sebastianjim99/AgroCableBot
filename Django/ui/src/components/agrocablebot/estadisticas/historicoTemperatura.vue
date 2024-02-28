<template>
    <div class="container">
      <Line :data="chartData" :options="options" v-if="loaded" />
      <div v-else>Cargando...</div>
    </div>
  </template>
  
  <script>
  import { Line } from 'vue-chartjs';
  import axios from 'axios';
  import moment from 'moment';
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
          const response = await axios.get(`${this.api}/Sensor_MQTT/`);
          this.processData(response.data);
          this.loaded = true;
        } catch (error) {
          console.error('Error al obtener los datos:', error);
        }
      },
      processData(data) {
        // Agrupar los datos por fecha y calcular el promedio de temperatura para cada día
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
  
        // Actualizar los datos de la gráfica
        this.chartData = chartData;
      }
    }
  }
  </script>
  