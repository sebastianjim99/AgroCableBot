<template>

  <nav class="navbar navbar-expand-md bg-body">
      <div class="container-fluid"><button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navcol-1"><span class="visually-hidden">Toggle navigation</span><span class="navbar-toggler-icon"></span></button>
          <div id="navcol-1" class="collapse navbar-collapse text-center" style="width: initial;"><img class="img-fluid" src="@/assets/logos/imacuna.png" width="171" height="76" loading="auto" style="margin-left: 60px;" />
              <ul class="navbar-nav mx-auto">
                  <li class="nav-item"><a class="nav-link active" href="#">Inicio</a></li>
                  <li class="nav-item"><a class="nav-link" href="#">Quienes somos</a></li>
                  <li class="nav-item"><a class="nav-link" href="#">productos</a></li>
                  <li class="nav-item"><a class="nav-link" href="#">Contactanos</a></li>
              </ul><button class="btn btn-primary" type="button" style="border-radius: 10;border-style: solid;margin-left: 2px;margin-right: 102px;">Ingresar</button>
          </div>
      </div>
  </nav>
    
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
import Lineas from '../components/imacuna/Lineas.vue'
import UsersList from '../components/UsersList.vue'


export default {
    name: "ListUsers",
    components:{
        UsersList,
        Lineas, 
    }
}
</script>

<style>
    
</style>