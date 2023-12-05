<template>

<section>
    <div>
        <div class="container">
          <h1>Líneas de investigación</h1>
        </div>
        <div class="container py-4 py-xl-5">  

          <div class="row gy-4 row-cols-1 row-cols-md-2 row-cols-xl-3">
            <div class="col" v-for ="lineas_investigacion in Lineas_investigacion" :key="lineas_investigacion.id" >
              <div class="text-center d-flex flex-column align-items-center align-items-xl-center">
                <div class="bs-icon-lg bs-icon-rounded bs-icon-primary d-flex flex-shrink-0 justify-content-center align-items-center d-inline-block mb-3 bs-icon lg"><img src="@/assets/logo.png" height="100" width="100"  alt=""> </div>
                <div class="px-3">
                    <h4 style="text-align:center; font-size: 18px;" > {{lineas_investigacion.nombre}} </h4>
                </div>
              <div class="row">
                <div class="col"><button class="btn btn-primary" type="button">Editar</button></div>
                <div class="col"><button class="btn btn-primary" type="button">Eliminar</button></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</section>
 

</template>

<script >
    
</script>

<style>
    
</style>