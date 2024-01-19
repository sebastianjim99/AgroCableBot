<template>    
     SECCION DE PROYECTOS 
    <!-- <section class="py-4 py-xl-5">
        <div class="container">
        <div>
            <h1>INTEGRANTES</h1>
        </div>
            <br>
            <div class="row" >
                <div class="col-sm-6 col-lg-4 mb-4 text-center" v-for ="integrantes in Integrantes" :key="integrantes.id" >
                    <img class="rounded-circle img-fluid d-block mx-auto" :src="integrantes.imagen" height="278" width="278"/>
                    <h3 class="m-0">{{integrantes.nombres}}  {{integrantes.primer_apellido}}  {{integrantes.segundo_apellido}} </h3>
                    <h5 class="my-1">{{integrantes.facultades}} {{integrantes.programa}} </h5>
                    <p>{{integrantes.tipo_Integrante}}</p>
                </div>
            </div>
    </div>
    </section> -->
        


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
          'videoProyectos': '',
          'imagenesProyectos': '',
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
