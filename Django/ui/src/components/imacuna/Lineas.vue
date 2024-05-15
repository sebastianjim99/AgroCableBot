<template>
     <!--  SECCION DE LINEAS DE INVESTIGACIÓN -->
    <section>
        <div>
            <div class="container"   style=" padding-bottom: 5px; display: flex; justify-content: center; " >
            <div class="lineas-tittle" >
              <h1 class="lineas">Líneas de investigación</h1>   
            </div> 
            </div>
            <div class="container py-4 py-xl-5">  
            <div class="row gy-4 row-cols-1 row-cols-md-2 row-cols-xl-3 row-cols-xl-4" >
                <div class="col " style="padding: 10px;"  v-for ="lineas_investigacion in Lineas_investigacion" :key="lineas_investigacion.id"  >
                <div class="text-center d-flex flex-column align-items-center align-items-xl-center lineas-container">
                    <div class="">
                      <img class="imagen-zoom" :src="lineas_investigacion.imagen" height="200" width="200"  style="padding: 10px;"  alt=""> 
                    </div>
                    <div class="px-1" style="color: white; font-size: medium;">
                      <h4 style="text-align:center; font-size: 25px;" > {{lineas_investigacion.nombre}} </h4>
                    </div>
                </div>
            </div>
            </div>
        </div>
        </div>
    </section>

</template>


<script>
export const RUTA_SERVIDOR = process.env.VUE_APP_API_URL;
import axios from 'axios';
import FormData from 'form-data';

export default{
    name: 'LineasService',
  data(){
    return{
      Lineas_investigacion:[],
      currentLineas: {},
      'api': `${process.env.VUE_APP_API_URL}`,
      'lineas_investigacion':{
          'nombre': '',
          'imagen': null,
      },
    }
  },
  
  mounted(){
    console.log('DOM rendered')
    this.getLineas_investigacion()
  },

  created(){
    console.log('DOM creadted')
  },

  methods : {
    getLineas_investigacion(){
      axios.get(this.api + '/api/Lineas_investigacion/' ).then(
        Response => {
          console.log(Response.data)
          this.Lineas_investigacion = Response.data;
        }
      ).catch(error =>{
        console.error(error)
      })
    },
    onImageChanged: function(event) {
      // Preview imagen
      this.lineas_investigacion.imagen = event.target.files[0];
    },
    createData() {
      // Crear un objeto FormData para enviar el nombre y la imagen
      const requestData = {
      nombre: this.lineas_investigacion.nombre,
      imagen: this.lineas_investigacion.imagen,
      };

      var formData = this.toFormData(requestData)

      // Enviar el formulario al backend
      axios.post(this.api + '/api/Lineas_investigacion/', formData, {"content-type": "multipart/form-data"})
        .then(response => {
          console.log("Datos subidos exitosamente", response.data);
          this.getLineas_investigacion()
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
      axios.delete(this.api + `/api/Lineas_investigacion/${id}/`).then(
        response => {
          console.log('Datos eliminados exitosamente', response.data);
          this.getLineas_investigacion(); // Actualiza la lista después de la eliminación
        })
        .catch(error => {
          console.error('Error al eliminar los datos', error);
        });
    },

  },
}

</script>