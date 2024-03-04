<template>
    <!--  SECCION DE SERVICIOS -->
    <section>
        <div>
            <div class="container" style="padding-bottom: 1px; justify-content: center; display: flex;">
                <h1 class="servicios-tittle"  >Servicios</h1>
            </div>
            <div class="container py-4 py-xl-5">  
            <div class="row gy-4 row-cols-1 row-cols-md-2 row-cols-xl-3 row-cols-xl-4" >
                <div class="col" v-for ="servicios in Servicios" :key="servicios.id" >
                <div class="text-center d-flex flex-column align-items-center align-items-xl-center content-servicios ">
                    <div class=""><img class="imagen-zoom" :src="servicios.imagen" height="200" width="200" style="padding:10px" alt=""> </div>
                    <div class="px-1" style=" font-size: medium;"  >
                        <h4 style="text-align:center; font-size: 25px" > {{servicios.nombre}} </h4>
                    </div>
                </div>
            </div>
            </div>
        </div>
        </div>
    </section>
  <!-- SECCION DE CRUD  -->
   

</template>

<script>
import axios from 'axios';
import FormData from 'form-data';

export default{
    name: 'Part_servicios',
  data(){
    return{
      Servicios:[],
      currentLineas: {},
      'api': `${process.env.VUE_APP_API_URL}`,
      'servicios':{
          'nombre': '',
          'imagen': null,
      },
    }
  },
  
  mounted(){
    console.log('DOM rendered')
    this.getServicios()
  },

  created(){
    console.log('DOM creadted')
  },

  methods : {
    getServicios(){
      axios.get(this.api + '/api/Servicios/ ').then(
        Response => {
          console.log(Response.data)
          this.Servicios = Response.data;
        }
      ).catch(error =>{
        console.error(error)
      })
    },

    onImageChanged: function(event) {
      // Preview imagen
      this.servicios.imagen = event.target.files[0];
    },

    createData() {
      // Crear un objeto FormData para enviar el nombre y la imagen
      const requestData = {
      nombre: this.servicios.nombre,
      imagen: this.servicios.imagen,
      };

      var formData = this.toFormData(requestData)

      // Enviar el formulario al backend
      axios.post( this.api + '/api/Servicios/', formData, {"content-type": "multipart/form-data"})
        .then(response => {
          console.log("Datos subidos exitosamente", response.data);
          this.getServicios()
        })
        .catch(error => {
          console.error("Error al subir los datos", error);
        });
        
    },

    toFormData(obj) {
    // funcion que convierte a formData
            var formData = new FormData()
            for (var key in obj) {
                formData.append(key, obj[key])
            }
            return formData
    },

    editData(id) {
      // Redirige a la página de edición con el ID del dato
      this.$router.push(`/editar/${id}`);
    },

    deleteData(id) {
      axios.delete(this.api + `/api/Servicios/${id}/`).then(
        response => {
          console.log('Datos eliminados exitosamente', response.data);
          this.getServicios(); // Actualiza la lista después de la eliminación
        })
        .catch(error => {
          console.error('Error al eliminar los datos', error);
        });
    },

  },
}

</script>