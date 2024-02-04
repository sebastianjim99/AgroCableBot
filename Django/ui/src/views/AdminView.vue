<template>

    <div class="">
        <navbar_monitoreo />
    </div>
    
    <!-- Crear nuevo usuario  -->
  <div>
      <router-link class="btn btn-primary" to="/CrearCuenta"> Agregar usuario </router-link>
  </div>

  <div class="users">
      <UsersList />
  </div>
  
    <div class="Lineas_servicios">
      <Lineas />
  </div>


</template>

<script>
import navbar_monitoreo from '/src/components/agrocablebot/base.vue'
import Lineas from '../components/imacuna/Lineas.vue'
import UsersList from '../components/UsersList.vue'


export default {
    name: "ListUsers",
    components:{
        navbar_monitoreo,
        UsersList,
        Lineas, 
    }
}
</script>

<style>
    
</style>