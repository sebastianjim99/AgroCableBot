<template>
    <div class="container">
      <input type="date" v-model="startDate" @change="fetchData" />
      <input type="date" v-model="endDate" @change="fetchData" />
      <div v-if="!startDate || !endDate">Seleccionar rango de fechas para graficar humedad</div>
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
    name: 'graficaHumedad',
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
  
        // Agrupar los datos por fecha y calcular el promedio de humedad para cada día
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
  
        // Actualizar los datos de la gráfica
        this.chartData = chartData;
      }
    }
  }
  </script>
  