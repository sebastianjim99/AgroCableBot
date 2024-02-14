import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import '../src/resources/css/bootstrap.css'
import '../src/assets/vendor/swiper/swiper-bundle.min.css'
// Import Swiper styles
  import 'swiper/css';
  import 'swiper/css/pagination';
import axios from 'axios'
import store from './store'
import { BootstrapIconsPlugin } from "bootstrap-icons-vue";
import '../src/resources/css/Bootstrap-Calendar.css' 
import '../src/resources/css/integrantes.css' 


axios.defaults.baseURL = 'http://0.0.0.0:8000'

// createApp(App).use(router).use(store).mount('#app')

const app = createApp(App);
app.use(router).use(store);
app.use(BootstrapIconsPlugin);


app.mount('#app');