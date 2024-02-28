<template>
    <div class="container">
      <input type="date" v-model="startDate" @change="fetchData" />
      <input type="date" v-model="endDate" @change="fetchData" />
      <div v-if="!startDate || !endDate">Seleccionar rango de fechas para graficar temperatura</div>
      <div v-else>
        <Line :data="chartData" :options="options" v-if="loaded" />
        <div v-else>Cargando...</div>
      </div>
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
    name: 'graficaTemperatura',
    components: {
      Line
    },
    data() {
      return {
        chartData: {},
        startDate: null, // Fecha de inicio del rango
        endDate: null, // Fecha de fin del rango
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
        api: `${process.env.VUE_APP_API_URL}`,
      }
    },
    mounted() {
      // No se llama a fetchData() en el montaje inicial
    },
    watch: {
      startDate(newVal) {
        // Llamamos a fetchData() cuando cambia la fecha de inicio del rango
        if (newVal && this.endDate) {
          this.fetchData();
        }
      },
      endDate(newVal) {
        // Llamamos a fetchData() cuando cambia la fecha de fin del rango
        if (newVal && this.startDate) {
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
        // Filtrar los datos para el rango de fechas seleccionado
        const filteredData = data.filter(item => {
          const timestamp = moment(item.timestamp).format('YYYY-MM-DD');
          return timestamp >= this.startDate && timestamp <= this.endDate;
        });
  
        // Agrupar los datos por fecha y calcular el promedio de temperatura para cada día
        const dailyAverageTemperatures = {};
        filteredData.forEach(item => {
          const date = moment(item.timestamp).format('YYYY-MM-DD');
          if (!dailyAverageTemperatures[date]) {
            dailyAverageTemperatures[date] = [item.temperatura];
          } else {
            dailyAverageTemperatures[date].push(item.temperatura);
          }
        });
  
        const chartData = {
          labels: Object.keys(dailyAverageTemperatures),
          datasets: [
            {
              label: 'Temperatura promedio',
              backgroundColor: 'rgba(255, 99, 132, 0.2)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1,
              data: Object.values(dailyAverageTemperatures).map(temperatures => {
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
  