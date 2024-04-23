import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import axios from 'axios'
import store from './store'

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

import '../src/resources/css/Bootstrap-Calendar.css' 
import '../src/resources/css/integrantes.css' 
import '../src/resources/css/imacuna_style.css' 
import '../src/resources/css/tareasProgramados.css' 
import 'bootstrap'; 
import 'bootstrap/dist/js/bootstrap.bundle.min.js'; // Importa el JavaScript de Bootstrap
import 'swiper/css';
import 'swiper/css/pagination';

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'



axios.defaults.baseURL = 'http://0.0.0.0:8000'


const app = createApp(App);
app.use(ElementPlus)
app.use(router).use(store);
// app.use(BootstrapIconsPlugin);


app.mount('#app');