<template>
    <br>
    <section>
        <div class="row">
            <div class="col">
                <div class="container">
                    <div class="row">
                        <div class="col-6 col-xl-6 text-start text-bg-light">
                            <h1 style="text-align: center;padding: 12px;">Distribución del cultivo </h1>
                            <!-- <ul class="text-primary-emphasis justify-content-center cbp-rfgrid"> -->
                             
                            <table>
                              <tbody>
                                <tr v-for="(fila, filaIndex) in matriz" :key="filaIndex">
                                  <td v-for="(planta, columnaIndex) in fila" :key="columnaIndex" style="margin: auto;padding: initial;" width="100px" height="100px">
                                    <div v-if="planta">
                                      <!-- Aquí puedes mostrar los datos de la planta, por ejemplo: -->
                                      <p>{{ planta.nombre }}</p>
                                      <img  :src="planta.cultivo.iconosPlantas" alt="Imagen de planta" style="margin: auto;padding: initial;" width="50px" height="50px">
                                    </div>
                                    <div v-else>
                                      {{ obtenerContadorPosicion(filaIndex, columnaIndex) }}
                                      <img  src="@/assets/iconos/sin_imagen.png" alt="Sin imagen de planta" style="margin: auto;padding: initial;" width="50px" height="50px">
                                    </div>
                                  </td>
                                </tr>
                              </tbody>
                            </table>






                                <!-- <li><a href="#"> </a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                                <li class="text-light"><a href="#"><img class="img-fluid border rounded-0 border-light-subtle focus-ring focus-ring-primary" src="@/assets/iconos/cilantro.png" style="margin: auto;padding: initial;" width="100px" height="100px" /></a></li>
                         -->
                            <!-- </ul> -->
                        </div>
                        <div class="col">
                            <br>
                            <h1 style="text-align: center;">Datos</h1>
                            <br>
                            
                            <ul class="list-group" v-for="tipoCultivo in tipo_cultivo" :key="tipoCultivo.id">
                                <li class="list-group-item" style="background: var(--bs-body-bg);"><span>Tipo de Cultivo: {{tipoCultivo.nombre}}</span></li>
                                <li class="list-group-item"><span> Descripción: {{tipoCultivo.descripcion}} </span></li>
                                <li class="list-group-item" v-for="cultivo in cultivos" :key="cultivo.id"><span>Fecha de siembra: {{cultivo.fechaSiembra}}</span></li>
                                <li class="list-group-item"><span>Temperatura optima: {{tipoCultivo.temperaturaOptimaMin}} - {{tipoCultivo.temperaturaOptimaMax}} °C</span></li>
                                <li class="list-group-item"><span>Estimado para cosechar: {{tipoCultivo.estimadoCosechaMin}} - {{tipoCultivo.estimadoCosechaMax}} Días</span></li>
                                <li class="list-group-item"><span>Estimado de germinación: {{tipoCultivo.estimadoGerminacionMin}} - {{tipoCultivo.estimadoGerminacionMax}} Días</span></li>
                                <li class="list-group-item"><span>Profundidad de siembra: {{ tipoCultivo.profundidadSiembra }} cm </span></li>
                            </ul>
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
        
      }
    },

    mounted(){
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
