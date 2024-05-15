<template>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" >
    
    <div class="">
        <navbar_monitoreo />
    </div>
    <div class="">
        <informacion_cultivo />
    </div>

    
    <div class="">
        <control_motores />
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
import control_motores from '/src/components/agrocablebot/control/control_motores.vue'

export default{
    components:{
        navbar_monitoreo,
        footer_imacuna,
        informacion_cultivo,
        contacto_soporte,
        control_motores,
    }
}

</script>