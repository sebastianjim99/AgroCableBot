<template>

  <div class="">
    <navbar_monitoreo />
  </div>

  <div class="container">
    <h1 class="divider-style mb-4"> <span>Gráficas de un día en específico</span> </h1>
    <div class="row">
      <!-- Columna 1 -->
      <div class="col-lg-6">
        <div class="mb-4">
          <h2 class="mb-3">Gráfica de temperatura</h2>
          <grafica_temperatura />
        </div>
      </div>

      <!-- Columna 2 -->
      <div class="col-lg-6">
        <div class="mb-4">
          <h2 class="mb-3">Gráfica de humedad</h2>
          <grafica_humedad_dia_esp />
        </div>
      </div>
    </div>
  </div>

  <div class="container">
    <h1 class="divider-style mb-4"> 
      <span>Gráficas históricas </span>    
        <span> <button @click="showTemperatureChart = true" :class="{ 'active': showTemperatureChart }" class="btn btn-success me-2">Temperatura</button> </span>
        <span> <button @click="showTemperatureChart = false" :class="{ 'active': !showTemperatureChart }" class="btn btn-success">Humedad</button> </span> 
    
    </h1> 
    
    <div class="row">
      <div class="col-lg-12">
        <h2 class="text-center mb-4">{{ chartMessage }}</h2>
        <grafica_historica_temperatura v-if="showTemperatureChart" />
        <grafica_humedad v-else />
      </div>
    </div>


  </div>



      <div class="container">
        <h1 class="divider-style mb-4"> <span>Gráficas por rango de fechas</span> </h1> 
        <div class="row">
          <!-- Columna 1 -->
          <div class="col-lg-6">
            <div class="mb-4">
              <h2 class="mb-3">Temperatura</h2>
              <grafica_temperatura_rango_fecha />
            </div>
          </div>

          <!-- Columna 2 -->
          <div class="col-lg-6">
            <div class="mb-4">
              <h2 class="mb-3">Humedad</h2>
              <grafica_humedad_rango_fecha />
            </div>
          </div>
        </div>
      </div>
  
      <section>
        <footer_imacuna />
      </section>

</template>
 
<script>

import navbar_monitoreo from '/src/components/agrocablebot/base.vue'
import footer_imacuna from '/src/components/footer.vue'
import grafica_temperatura from '/src/components/agrocablebot/estadisticas/graficaTemperatura.vue'
import grafica_humedad from '/src/components/agrocablebot/estadisticas/graficaHumedad.vue'
import grafica_historica_temperatura  from '/src/components/agrocablebot/estadisticas/historicoTemperatura.vue'
import grafica_humedad_dia_esp from '/src/components/agrocablebot/estadisticas/graficaHumedadDiaEsp.vue'
import grafica_temperatura_rango_fecha from '/src/components/agrocablebot/estadisticas/graficaTemperaturaRangoFecha.vue'
import grafica_humedad_rango_fecha from '/src/components/agrocablebot/estadisticas/graficaHumedadRangoFecha.vue'


 export default {

  components: {
    navbar_monitoreo,
    footer_imacuna,
    grafica_temperatura,
    grafica_humedad,
    grafica_historica_temperatura,
    grafica_humedad_dia_esp,
    grafica_temperatura_rango_fecha,
    grafica_humedad_rango_fecha,
  },  
  
  data(){
    return {
      showTemperatureChart: true
    };
  },
  computed: {
    chartMessage() {
      return this.showTemperatureChart ? "Gráfica de temperatura" : "Gráfica de humedad";
    }
  }
}

</script>
 
 
  
<style >

  .divider-style:before {
    content: "";
    display: block;
    border-top: solid 1px black;
    width: 100%;
    height: 1px;
    position: absolute;
    top: 50%;
    z-index: 1;
  }

.divider-style {
  margin-top: 0px;
  position: relative;
  margin-right: 40px;
  margin-left: 40px;
}

.divider-style span {
  background: #fff;
  padding: 0 20px;
  position: relative;
  z-index: 5;
}
</style>