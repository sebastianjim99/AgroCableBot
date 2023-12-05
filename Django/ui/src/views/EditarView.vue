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
    <label for="imageFile">Imagen:</label>
    <input type="file" @change="handleFileChange" />
    <button @click="updateData">Actualizar Datos</button>
  </div>
</template>
<script>

import axios from 'axios';

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


    handleFileChange(event) {
      this.lineas_investigacion.imagen = event.target.files[0];
    },
    async updateData() {

      const requestData = {
      nombre: this.lineas_investigacion.nombre,
      // Convertir la imagen a Base64
      //imagen: this.lineas_investigacion.imagen? await this.convertImageToBase64() : null,
      };

      axios.put(this.api + `/Lineas_investigacion/${this.lineas_investigacion.id}/`, requestData).then(
        response => {
          console.log('Datos actualizados exitosamente', response.data);
          this.goToHome(); // Redirige a la página principal
          
        })
        .catch(error => {
          console.error('Error al actualizar los datos', error);
        });
    },

    async convertImageToBase64() {
      return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onloadend = () => {
          resolve(reader.result);
        };
        reader.onerror = reject;
        reader.readAsDataURL(this.lineas_investigacion.imagen);
      });
    },

    goToHome() {
      // Redirige a la página principal usando Vue Router
      this.$router.push('/');
    },
  },
};
</script>