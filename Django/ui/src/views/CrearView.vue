<template>
 <div class="about">
    <h1>Pagina para crear</h1>
  </div>
</template>

<script>



export default{
  data(){
    return{
      'api' : 'http://localhost:8000/api',
      'lineas_investigacion':{
          'nombre': '',
          'imagen': null,   
      },
    }
  },

  mounted(){
  console.log('DOM rendered')
  },

  created(){
  console.log('DOM creadted')
  },

  methods : {
       
  },

   
}
</script>
<style>
</style>