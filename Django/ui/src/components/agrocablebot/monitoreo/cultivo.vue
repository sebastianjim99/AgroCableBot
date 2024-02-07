<template>
    <br>
    <section>
        <div class="row">
            <div class="col">
                <div class="container">
                    <div class="row">
                        <div class="col-6 col-xl-6 text-start text-bg-light">
                            <h1 style="text-align: center;padding: 12px;">Distribución del cultivo </h1>                                    
                            <table>
                              <tbody>
                                <tr v-for="(fila, filaIndex) in matriz" :key="filaIndex">
                                  <td v-for="(planta, columnaIndex) in fila" :key="columnaIndex" style="margin: auto;padding: initial;" width="100px" height="80px" @click="seleccionarPlanta(filaIndex, columnaIndex)" :style="{ backgroundColor: plantaSeleccionada && filaIndex === plantaSeleccionada.fila && columnaIndex === plantaSeleccionada.columna ? 'rgb(178,218,250, 0.5)' : '' }">
                                    <div v-if="planta">
                                      <!-- Aquí puedes mostrar los datos de la planta, por ejemplo: -->
                                      <p>{{ planta.nombre }}</p>
                                      <img  :src="planta.cultivo.iconosPlantas" alt="Imagen de planta" style="margin: auto;padding: initial;" width="40px" height="40px">
                                    </div>
                                    <div v-else>
                                      {{ obtenerContadorPosicion(filaIndex, columnaIndex) }}
                                      <img  src="@/assets/iconos/sin_imagen.png" alt="Sin imagen de planta" style="margin: auto;padding: initial;" width="40px" height="40px">
                                    </div>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                        </div>
                        <div class="col">
                            <br>
                            <h1 style="text-align: center;">Datos del cultivo seleccionado</h1>
                            <br>
                            <div v-if="cultivoSeleccionado">
                              <ul class="list-group" >
                                  <li class="list-group-item" style="background: var(--bs-body-bg);"><span>Tipo de Cultivo: {{cultivoSeleccionado.tipoCultivo.nombre}}</span></li>
                                  <!-- <li class="list-group-item"><span> Descripción: {{tipoCultivo.descripcion}} </span></li> -->
                                  <li class="list-group-item" ><span>Fecha de siembra: {{cultivoSeleccionado.fechaSiembra}}</span></li>
                                  <li class="list-group-item"><span>Temperatura optima: {{cultivoSeleccionado.tipoCultivo.temperaturaOptimaMin}} - {{cultivoSeleccionado.tipoCultivo.temperaturaOptimaMax}} °C</span></li>
                                  <li class="list-group-item"><span>Estimado para cosechar: {{cultivoSeleccionado.tipoCultivo.estimadoCosechaMin}} - {{cultivoSeleccionado.tipoCultivo.estimadoCosechaMax}} Días</span></li>
                                  <li class="list-group-item"><span>Estimado de germinación: {{cultivoSeleccionado.tipoCultivo.estimadoGerminacionMin}} - {{cultivoSeleccionado.tipoCultivo.estimadoGerminacionMax}} Días</span></li>
                                  <li class="list-group-item"><span>Profundidad de siembra: {{ cultivoSeleccionado.tipoCultivo.profundidadSiembra }} cm </span></li>
                              </ul>
                            </div>
                            <div v-else>
                              <p style="text-align: center;">Haz clic en una planta para ver los detalles del cultivo.</p>
                            </div>
                            <br>
                            <br>
                            <br>
                            <h1 style="text-align: center;">Alertas</h1>
                            <ul class="list-group">
                                <li class="list-group-item" style="background: var(--bs-body-bg);"><span>Batería baja</span></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>


<script>
  import axios from 'axios'
  export default {
    name: "CultivoVue",
    data(){
      return{
        tipo_cultivo:[],
        cultivos:[],
        plantas:[],
        matriz: [],
        plantaSeleccionada: null,
        cultivoSeleccionado:null
        
      }
    },

    mounted(){
      // Realizar las solicitudes HTTP para obtener datos
      //Lectura tipo de cultivo
      axios.get('http://localhost:8000/api/tipoCultivo')
      .then(response =>{
        console.log("Tipo de cultivos")
        console.log(response.data)
        this.tipo_cultivo=response.data
      })
      .catch(error =>{
        console.log(error)
      })
      //Lectura de cultivo
      axios.get('http://localhost:8000/api/cultivo')
      .then(response =>{
        console.log("Cultivos")
        console.log(response.data)
        this.cultivos=response.data
      })
      .catch(error =>{
        console.log(error)
      })
      //Lectura de plantas
      axios.get('http://localhost:8000/api/plantas')
      .then(response =>{
        console.log("plantas")
        console.log(response.data)
        this.plantas=response.data
        this.initializeMatriz()
      })
      .catch(error =>{
        console.log(error)
      })
      
    },

    methods: {
      // Función para inicializar la matriz con los datos de las plantas
      initializeMatriz() {
        for (let i = 0; i < 8; i++) {
          this.matriz.push(new Array(8).fill(null));
        }

        // Asignar las plantas a la matriz según el número de planta asignado
        this.plantas.forEach(planta => {
          const fila = Math.floor((planta.numeroPlanta - 1) / 8);
          const columna = (planta.numeroPlanta - 1) % 8;
          this.matriz[fila][columna] = planta;  
        }); 
      },

      obtenerContadorPosicion(filaIndex, columnaIndex) {
        // Calcula el contador de posición basado en los índices de fila y columna
        return filaIndex * this.matriz[0].length + columnaIndex + 1;
      },
      // Seleccion de la planta mediante click y despliegue de informacion
      seleccionarPlanta(filaIndex, columnaIndex) {
        this.plantaSeleccionada = { fila: filaIndex, columna: columnaIndex };
        const planta = this.matriz[filaIndex][columnaIndex];
        this.cultivoSeleccionado = planta ? planta.cultivo : null;
      }

    }
    
}
</script>

<style>
    .cbp-rfgrid {
  margin: 35px 0 0 0;
  padding: 0;
  list-style: none;
  position: relative;
  width: 100%;
}

.cbp-rfgrid li {
  position: relative;
  float: left;
  overflow: hidden;
  width: 16.6666667%;
  width: -webkit-calc(100% / 6);
  width: calc(100% / 8);
}

.cbp-rfgrid li a, .cbp-rfgrid li a img {
  display: block;
  width: 100%;
  cursor: pointer;
}

.cbp-rfgrid li a img {
  max-width: 1000%;
}

.cbp-rfgrid li a div {
  position: absolute;
  left: 20px;
  top: 20px;
  right: 20px;
  bottom: 20px;
  background: rgba(71,163,218,0.2);
  display: -webkit-flex;
  display: -moz-flex;
  display: -ms-flex;
  display: flex;
  -webkit-align-items: center;
  -moz-align-items: center;
  -ms-align-items: center;
  align-items: center;
  text-align: center;
  opacity: 0;
}

.cbp-rfgrid li a:hover div {
  opacity: 1;
}

.cbp-rfgrid li a div h3 {
  width: 100%;
  color: #fff;
  text-transform: uppercase;
  font-size: 1.4em;
  letter-spacing: 2px;
  padding: 0 10px;
}

@media screen and (max-width: 1190px) {
  .cbp-rfgrid li {
    width: 20%;
    width: -webkit-calc(100% / 5);
    width: calc(100% / 5);
  }
}

@media screen and (max-width: 945px) {
  .cbp-rfgrid li {
    width: 25%;
    width: -webkit-calc(100% / 4);
    width: calc(100% / 4);
  }
}

@media screen and (max-width: 660px) {
  .cbp-rfgrid li {
    width: 33.3333333%;
    width: -webkit-calc(100% / 3);
    width: calc(100% / 3);
  }
}

@media screen and (max-width: 660px) {
  .cbp-rfgrid li {
    width: 33.3333333%;
    width: -webkit-calc(100% / 3);
    width: calc(100% / 3);
  }
}

@media screen and (max-width: 400px) {
  .cbp-rfgrid li {
    width: 50%;
    width: -webkit-calc(100% / 2);
    width: calc(100% / 2);
  }
}

@media screen and (max-width: 300px) {
  .cbp-rfgrid li {
    width: 100%;
  }
}

.text-bg-light {
  color: #000!important;
  background-color: RGBA(248,249,250);
}
</style>
