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
          <swiper id="mySwiper"
          :slidesPerView="slidesPerView"
          :spaceBetween="spaceBetween" 
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
                        <img :src="integrantes.imagen" alt="" class="card-img imagen-zoom ">
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
import {  Autoplay, Pagination, Navigation } from 'swiper/modules';

export default {
    name: "Integrantes_imacuna",

    components:{
      Swiper,
      SwiperSlide,
    },
    setup() {
      return {
        modules: [Autoplay, Pagination, Navigation],
      };
    },
    data(){
    return{
      Integrantes:[],
      currentLineas: {},
      slidesPerView: 3,
      spaceBetween:90,
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
    window.addEventListener('resize', this.updateSlidesPerView);
    this.updateSlidesPerView();
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
    updateSlidesPerView() {
      // Verifica el ancho de la ventana y ajusta slidesPerView en consecuencia
      if (window.innerWidth <= 768) {
        this.slidesPerView = 1;
        this.spaceBetween = 60;
      } else {
        this.slidesPerView = 3;
        this.spaceBetween = 90;
      }
    },
  
    beforeDestroy() {
      // Elimina el event listener para evitar fugas de memoria
      window.removeEventListener('resize', this.updateSlidesPerView);
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


</style>
