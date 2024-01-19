<template>    
    <!--  SECCION DE INTEGRANTES  -->
    <section class="py-4 py-xl-5">
        <div class="container">
        <div>
            <h1>INTEGRANTES</h1>
        </div>
            <br>
            <div class="row" >
                <div class="col-sm-6 col-lg-4 mb-4 text-center" v-for ="integrantes in Integrantes" :key="integrantes.id" >
                    <img class="rounded-circle img-fluid d-block mx-auto" :src="integrantes.imagen" height="278" width="278"/>
                    <h3 class="m-0">{{integrantes.nombres}}  {{integrantes.primer_apellido}}  {{integrantes.segundo_apellido}} </h3>
                    <h5 class="my-1">{{integrantes.correo}} </h5>
                    <h5 class="my-1">{{integrantes.facultades}} {{integrantes.programa}} </h5>
                    <p>{{integrantes.tipo_Integrante}}</p>
                </div>
                
            </div>
            <br>
            <br>
            <br>
    </div>
    </section>
        


</template>

<script>
import axios from 'axios';
import FormData from 'form-data';

export default {
    name: "Integrantes_imacuna",
    components:{

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
          console.log("integrantes")
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
    .mx-auto {
    margin-right: auto !important;
    margin-left: auto !important;
    }
    .img-fluid {
    max-width: 278px;
    height: 278px;
}

</style>
