<template>
    
    <div class="">
        <navbar_monitoreo />
    </div>
    <div class="">
        <informacion_cultivo />
    </div>

    <div class="">
        <contacto_soporte />
    </div>

    <div class="">
        <footer_imacuna />
    </div>




</template>


<script>
import navbar_monitoreo from '/src/components/agrocablebot/base.vue'
import footer_imacuna from '/src/components/footer.vue'
import informacion_cultivo from '/src/components/agrocablebot/soporte/infoCultivo.vue'
import contacto_soporte from '/src/components/agrocablebot/soporte/contactoSoporte.vue'

export default{
    components:{
        navbar_monitoreo,
        footer_imacuna,
        informacion_cultivo,
        contacto_soporte
       
    }
}
</script>