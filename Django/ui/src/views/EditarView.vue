<template>
  <div>
    <h2>Editar Datos</h2>
     <div>
      <p><strong>Nombre:</strong> {{ lineas_investigacion.nombre }}</p>
      <strong>Imagen:</strong> <img :src="lineas_investigacion.imagen" alt="Imagen existente" />
    </div>
    <!-- Formulario para editar los datos existentes -->
    <label for="chartfieldName">Nombre:</label>
    <input type="text" v-model="lineas_investigacion.nombre" />
    <label class="font-bold">Seleccione una imagen</label>
      <input
          type="file"
          ref="fileupload"
          accept="image/*"
          class="form-control-file"
          @change="onImageChanged"
          name="imagen"
      />
    <button @click="updateData">Actualizar Datos</button>
  </div>

  
</template>
<script>

import axios from 'axios';
import FormData from 'form-data';

export default {
  data() {
    return {
      Lineas_investigacion:[],
      currentLineas: {},
      'api' : 'http://localhost:8000/api',
      'lineas_investigacion':{
          id: this.$route.params.id,
          'nombre': '',
          'imagen': null,
      }
    }
  },
  mounted(){
    console.log('DOM rendered')
    this.getLineas_investigacion()
  },
  methods: {
    getLineas_investigacion(){
      axios.get(this.api + /Lineas_investigacion/ ).then(
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
    
    updateData() {
      const requestData = {
        nombre: this.lineas_investigacion.nombre,
        imagen: this.lineas_investigacion.imagen,
      };
      var formData = this.toFormData(requestData)

      axios.put(this.api + `/Lineas_investigacion/${this.lineas_investigacion.id}/`, formData, {"content-type": "multipart/form-data"})
      .then(response => {
          console.log('Datos actualizados exitosamente', response.data);
          this.getLineas_investigacion()
          this.goToHome(); // Redirige a la página principal
          
        })
        .catch(error => {
          console.error('Error al actualizar los datos', error);
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

    goToHome() {
      // Redirige a la página principal usando Vue Router
      this.$router.push('/');
    },
  },
};
</script>