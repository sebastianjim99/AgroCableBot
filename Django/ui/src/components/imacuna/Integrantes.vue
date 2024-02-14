<template>    
   <!-- Vendor CSS Files -->
    <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
    <link href="assets/vendor/aos/aos.css" rel="stylesheet">
    <link href="assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
    <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">


    <!--  SECCION DE INTEGRANTES  -->
    <section class="py-4 py-xl-5">
      <div class="container">
        <div>
            <h1>INTEGRANTES</h1>
        </div>
      </div>
      <div class="container">
        <div class="slider-container">
          <swiper 
          :slidesPerView="3" 
          :spaceBetween="20" 
          :centeredSlides="true" 
          :grabCursor="true" 
          :pagination="{ 
            clickable: true,
          }" 
          :modules="modules" 
          class="mySwiper" 
          >
            <swiper-slide  v-for ="integrantes in Integrantes" :key="integrantes.id" >  
              <div class="slider-content">
                <div class="card-wrapper" >
                  <div class="card" >
                    <div class="image-integrante"  >
                      <span class="overlay"> </span>
                      <div class="card-image"  >
                        <img :src="integrantes.imagen" alt="" class="card-img">
                      </div>
                    </div>  
                    <div class="card-content">
                      <h2 class="name-integrante"> {{integrantes.nombres}} {{integrantes.primer_apellido}} {{integrantes.segundo_apellido}} </h2>
                      <p class="descripcion-integrante"> {{integrantes.correo}} </p>
                      <p class="descripcion-integrante"> {{integrantes.facultades}} {{integrantes.programa}} </p>
                      <p class="descripcion-integrante"> {{integrantes.tipo_Integrante}} </p>
                      <button class="button"> Mostrar mas </button>
                    </div>
                  </div>
                </div>
              </div>
            </swiper-slide>
          </swiper>
        </div>
      </div>
    </section>

</template>

<script>

import axios from 'axios';

// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue';
import {  Pagination } from 'swiper/modules';

export default {
    name: "Integrantes_imacuna",

    components:{
      Swiper,
      SwiperSlide,
    },
    setup() {
      return {
        modules: [Pagination],
      };
    },
    data(){
    return{
      Integrantes:[],
      currentLineas: {},
      'api' : 'http://localhost:8000/api',
      'integrantes':{
          'primer_apellido': '',
          'segundo_apellido': '',
          'nombres': '',
          'fecha_nacimiento': '',
          'correo': '',
          'sexo': '',
          'imagen': null,
          'facultades': '',
          'programa': '',
          'tipo_Integrante':'',

      },
    }
  },
  
  mounted(){
    console.log('DOM rendered')
    this.getIntegrantes()
  },

  created(){
    console.log('DOM creadted')
  },

  methods : {
    getIntegrantes(){
      axios.get(this.api + /integrante/ ).then(
        Response => {
          this.Integrantes= Response.data;
        }
      ).catch(error =>{
        console.error(error)
      })
    },

    onImageChanged: function(event) {
      // Preview imagen
      this.Integrantes.imagen = event.target.files[0];
    },

  },
}
</script>

<style scoped>
    .mx-auto {
    margin-right: auto !important;
    margin-left: auto !important;
    }
    .img-fluid {
    max-width: 278px;
    height: 278px;
    }

  .autoplay-progress {
  position: absolute;
  right: 16px;
  bottom: 16px;
  z-index: 10;
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  color: var(--swiper-theme-color);
}

.autoplay-progress svg {
  --progress: 0;
  position: absolute;
  left: 0;
  top: 0px;
  z-index: 10;
  width: 100%;
  height: 100%;
  stroke-width: 4px;
  stroke: var(--swiper-theme-color);
  fill: none;
  stroke-dashoffset: calc(125.6 * (1 - var(--progress)));
  stroke-dasharray: 125.6;
  transform: rotate(-90deg);
}


</style>
