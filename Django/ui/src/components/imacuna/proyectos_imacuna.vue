<template>    
  <section>
    <div class="container py-4 py-xl-5">
        <div class="row mb-5">
            <div class="col-md-8 col-xl-6 text-center mx-auto" >
                <h2>PROYECTOS DEL SEMILLERO IMACUNA</h2>
                <p class="w-lg-50"> EL MEJOR SEMILLERO DEL MUNDO </p>
            </div>
        </div>
        <div class="row gy-4 row-cols-1 row-cols-md-2 row-cols-xl-3"  >
            <div class="col" v-for ="proyectos in Proyectos" :key="proyectos.id" >
                 <div v-for ="imagenesProyectos in ImagenesProyectos" :key="imagenesProyectos.id"> 
                  <img :src="imagenesProyectos.imagen" class="rounded img-fluid d-block w-100 fit-cover" style="height: 200px;" />
                  <div class="py-4">
                      <h4>{{proyectos.nombre}} </h4>
                      <p>{{proyectos.descripcion}}</p>
                  </div>
                </div>
            </div>
        </div>
    </div>
</section>
   


</template>

<script>
import axios from 'axios';
// import FormData from 'form-data';

export default {
    name: "Proyectos_imacuna",
    components:{

    },
    data(){
    return{
      Proyectos:[],
      'api' : 'http://localhost:8000/api',
      'ImagenesProyectos':{
        'nombre':'',
        'descripcion':'',
        'imagen':'',
      },
      'proyetos':{
          'nombre': '',
          'descripcion': '',
          'videoProyectos': [],
          'imagenesProyectos': [],
      },
    }
  },
  
  mounted(){
    console.log('DOM rendered')
    this.getProyectos()
    this.getImagenes()
  },

  created(){
    console.log('DOM creadted')
  },

  methods : {
    getProyectos(){
      axios.get(this.api + /proyectos/ ).then(
        Response => {
          console.log("proyectos")
          console.log(Response.data)
          this.Proyectos= Response.data;
        }
      ).catch(error =>{
        console.error(error)
      })
    },

    getImagenes(){
      axios.get(this.api + /imagenesProyectos/ ).then(
        Response => {
          console.log("imagenes")
          console.log(Response.data)
          this.ImagenesProyectos = Response.data;
        }
      ).catch(error =>{
        console.error(error)
      })
    },
  },
}
</script>

<style scoped>
    

</style>
