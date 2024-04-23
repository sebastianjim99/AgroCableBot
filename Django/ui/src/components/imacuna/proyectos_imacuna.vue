<template>    
  <section>

      <div class="container">
        <div class="row mb-2">
          <div class="col-md-8 col-xl-6 text-center mx-auto" >
              <h2 class="" >Proyectos del semillero Imacuna</h2>
              <p class="" style="font-style: italic; font-size: 25px;" > Cosechando innovación </p>
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
                    <!-- <button class="btn btn-primary botton-vermas"  > Mostrar mas </button> -->
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
        'api': `${process.env.VUE_APP_API_URL}`,
      };
    },
  mounted() {
    axios.get(this.api + '/api/proyectos/')
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

<style scoped>
h2 {
  font-size: 2.5rem; /* Tamaño de la fuente para los títulos */
  color: #343a40; /* Color oscuro para los títulos */
  margin-bottom: 1rem;
}

p {
  font-size: 1.25rem; /* Tamaño de la fuente para los párrafos */
  color: #6c757d; /* Color gris para los párrafos */
  margin-bottom: 2rem;
}

.cardcontent {
  display: flex;
  flex-direction: column;
  overflow: hidden;
  border-radius: 0.5rem; /* Bordes redondeados */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Sombra suave */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Transición suave para hover */
}

.cardcontent:hover {
  transform: translateY(-5px); /* Eleva la tarjeta un poco cuando se hace hover */
  box-shadow: 0 12px 16px rgba(0, 0, 0, 0.2); /* Sombra más profunda en hover */
}

.card-proyecto {
  background: #ffffff; /* Fondo blanco para las tarjetas */
}

.img-proyecto {
  display: flex; /* Usamos flexbox */
  justify-content: center; /* Centrado horizontal */
  width: 100%; 
  height: 400px; 
  object-fit: contain; 
}

.content-text {
  padding: 1rem;
}

.title-proyecto {
  font-size: 1.5rem;
  color: black;/* Un azul que usualmente se asocia con enlaces para el título */
  margin-bottom: 0.5rem;
}

.descripcion-proyecto {
  font-size: 1rem;
  color: #495057; /* Color gris oscuro para la descripción */
  margin-bottom: 1rem;
}


/* Estilos para pantallas medianas (tablets) */
@media (max-width: 1024px) {
  .card-proyecto {
    width: 48%; /* Dos tarjetas por fila */
  }
}

/* Estilos para pantallas pequeñas (móviles) */
@media (max-width: 768px) {
  .row {
    gap: 1rem;
  }

  .card-proyecto {
    width: 100%; /* Una tarjeta por fila */
    margin-bottom: 1rem;
  }

  .img-proyecto {
    height: auto; /* La altura se ajusta para mantener la relación de aspecto */
  }
}
</style>

