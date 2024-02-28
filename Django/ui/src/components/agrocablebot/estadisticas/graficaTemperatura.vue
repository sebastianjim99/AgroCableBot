<template>
  <div class="container">
    <input type="date" v-model="selectedDay" @change="fetchData" />
    <div v-if="!selectedDay">Seleccionar fecha para graficar temperatura de un día en especifico</div>
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
      selectedDay: moment().format('YYYY-MM-DD'), // Fecha seleccionada por defecto es la fecha actual
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
    this.fetchData(); // Llamar a fetchData() al montar el componente para graficar la temperatura del día actual
  },
  watch: {
    selectedDay(newVal) {
      // Llamamos a fetchData() solo cuando selectedDay cambia y no es nulo o indefinido
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
      // Filtrar los datos para el día seleccionado
      const filteredData = data.filter(item => moment(item.timestamp).format('YYYY-MM-DD') === this.selectedDay);
      //console.log("fecha",this.selectedDay)
      // Formatear los datos para la gráfica de línea
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

      // Actualizar las opciones de la gráfica si es necesario
      // Puedes ajustar las opciones aquí según tus necesidades
    }
  }
}
</script>
