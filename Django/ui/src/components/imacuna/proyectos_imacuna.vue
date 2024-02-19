<template>    
  <section>

      <div class="container">
        <div class="row mb-5">
          <div class="col-md-8 col-xl-6 text-center mx-auto" >
              <h2>PROYECTOS DEL SEMILLERO IMACUNA</h2>
              <p class="w-lg-50"> Cosechando innovación </p>
          </div>
        </div>
        <div class="row gy-4 row-cols-1 row-cols-md-2"  >
          <div class="col-md " style=" object-fit: cover;" v-for="proyecto in proyectos" :key="proyecto.id" >

            <div class="cardcontent">
              <div class="card-proyecto"  >
               <swiper :effect="'cards'" :grabCursor="true" :modules="modules" class="mySwiperCards"  >
                  <swiper-slide v-for="imagen in proyecto.imagenesProyectos" :key="imagen.id" >
                    <img class="img-proyecto" :src="imagen.imagen" alt="img-proyecto" > 
                  </swiper-slide> 
               </swiper>
                <div class="content-text">
                    <h2 class="title-proyecto" > {{ proyecto.nombre }}    </h2>
                    <p class="descripcion-proyecto " >  <span> {{ proyecto.descripcion }}  </span>  </p>
                    <button class="btn btn-primary botton-vermas"  > Mostrar mas </button>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>

  </section>
   
</template>

<script>
import axios from 'axios';
import 'swiper/css/effect-cards';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { EffectCards } from 'swiper/modules';

export default {
  data() {
    return {
      proyectos: []
    };
  },
  components: {
      Swiper,
      SwiperSlide,
    },
    setup() {
      return {
        modules: [EffectCards],
      };
    },
  mounted() {
    axios.get('http://localhost:8000/api/proyectos/')
      .then(response => {
        console.log("proyectos")
        console.log(response.data)
        this.proyectos = response.data;
      })
      .catch(error => {
        console.error('Error al obtener proyectos:', error);
      });
  }
};
</script>
