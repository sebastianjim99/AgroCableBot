import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import '../src/resources/css/bootstrap.css'
import '../src/assets/vendor/swiper/swiper-bundle.min.css'

import axios from 'axios'
import store from './store'
import VueNativeSock from 'vue-native-websocket';

import { BootstrapIconsPlugin } from "bootstrap-icons-vue";

import '../src/resources/css/Bootstrap-Calendar.css' 
import '../src/resources/css/integrantes.css' 
import '../src/resources/css/imacuna_style.css' 
import '../src/resources/css/tareasProgramados.css' 
import '../src/resources/css/listcultivo.css' 
import 'bootstrap'; 
import 'bootstrap/dist/js/bootstrap.bundle.min.js'; // Importa el JavaScript de Bootstrap
import 'swiper/css';
import 'swiper/css/pagination';



axios.defaults.baseURL = 'http://0.0.0.0:8000'

Vue.use(VueNativeSock, 'ws://localhost:8000/ws/sensor_data/', {
  reconnection: true, // Reconexión automática
  reconnectionAttempts: 5, // Número de intentos de reconexión
  reconnectionDelay: 3000, // Retraso entre intentos de reconexión (en milisegundos)
});

const app = createApp(App);
app.use(router).use(store);
app.use(BootstrapIconsPlugin);


app.mount('#app');