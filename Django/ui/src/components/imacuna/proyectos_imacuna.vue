<template>    
  <section>
      <div class="container py-4 py-xl-5">
        <div class="row mb-5">
          <div class="col-md-8 col-xl-6 text-center mx-auto" >
              <h2>PROYECTOS DEL SEMILLERO IMACUNA</h2>
              <p class="w-lg-50"> Cosechando innovación </p>
          </div>
        </div>
        <div class="row gy-4 row-cols-1 row-cols-md-2 row-cols-xl-3"  >
          <div class="col" v-for="proyecto in proyectos" :key="proyecto.id" >
            <div v-for="imagen in proyecto.imagenesProyectos" :key="imagen.id">
            <img :src="imagen.imagen" alt="Imagen de proyecto" class="rounded img-fluid d-block w-100 fit-cover" style="height: 200px;">
          </div>
          <!-- <div v-for="video in proyecto.videoProyectos" :key="video.id">
            <video :src="video.archivo_video" controls></video>
          </div> -->
          <div class="py-4">
              <h2>{{ proyecto.nombre }}</h2>
              <p>{{ proyecto.descripcion }}</p>
          </div>
        </div>
      </div>
    </div>

  </section>
   
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      proyectos: []
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
