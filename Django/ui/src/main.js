import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import '../src/resources/css/bootstrap.css'
import axios from 'axios'
import store from './store'
import { BootstrapIconsPlugin } from "bootstrap-icons-vue";
import '../src/resources/css/Bootstrap-Calendar.css' 

axios.defaults.baseURL = 'http://localhost:8000'

// createApp(App).use(router).use(store).mount('#app')

const app = createApp(App);
app.use(router).use(store);
app.use(BootstrapIconsPlugin);


app.mount('#app');