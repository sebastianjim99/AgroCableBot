<template>    
  <section>
    <div class="container py-4 py-xl-5">
        <div class="row mb-5">
            <div class="col-md-8 col-xl-6 text-center mx-auto" >
                <h2>PROYECTOS DEL SEMILLERO IMACUNA</h2>
                <p class="w-lg-50"> EL MEJOR SEMILLERO DEL MUNDO </p>
            </div>
        </div>
        <div class="row gy-4 row-cols-1 row-cols-md-2 row-cols-xl-3" v-for ="proyectos in Proyectos" :key="proyectos.id" >
            <div class="col">
                <div><img class="rounded img-fluid d-block w-100 fit-cover" style="height: 200px;" src="C:/Users/SEBASTIAN/OneDrive/Escritorio/AgroCableBot/Django/public/media/imagenesProyectos/2024/01/19/AgroCableBot.png" />
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
import FormData from 'form-data';

export default {
    name: "Proyectos_imacuna",
    components:{

    },
    data(){
    return{
      Proyectos:[],
      'api' : 'http://localhost:8000/api',
      'proyetos':{
          'nombre': '',
          'descripcion': '',
          'videoProyectos': null,
          'imagenesProyectos': null,
      },
    }
  },
  
  mounted(){
    console.log('DOM rendered')
    this.getProyectos()
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

    onImageChanged: function(event) {
      // Preview imagen
      this.proyetos.imagenesProyectos = event.target.files[0];
    },

    toFormData(obj) {
    // funcion que convierte a formData
            var formData = new FormData()
            for (var key in obj) {
                formData.append(key, obj[key])
            }
            return formData
    },
  },
}
</script>

<style scoped>
    

</style>
