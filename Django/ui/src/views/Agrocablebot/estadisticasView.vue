<template>
    <div>
      <div class="">
        <navbar_monitoreo />
      </div>
  
      <div class="">
        <h2>Gráfica de temperatura de un día en especifico</h2>
        <grafica_temperatura />
      </div>

      <div class="">
        <h2>Gráfica de humedad de un día en especifico</h2>
        <grafica_humedad_dia_esp />
      </div>

      <div class="">
        <h2>Histórico de temperatura </h2>
        <grafica_historica_temperatura />
      </div>

      <div class="">
        <h2>Histórico de humedad </h2>
        <grafica_humedad />
      </div>
      
      <div class="">
        <h2>Temperatura en un rango de fechas </h2>
        <grafica_temperatura_rango_fecha />
      </div>

      <div class="">
        <h2>Humedad en un rango de fechas </h2>
        <grafica_humedad_rango_fecha />
      </div>
  
      <section>
        <footer_imacuna />
      </section>
    </div>
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
 }
 </script>
 
 
  
<style scoped>
/* Estilos específicos si los necesitas */
</style>