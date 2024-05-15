<template>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" >
    
    <div>
        <navbar_monitoreo />
    </div>
    
    <section>
        <mqtt_pagina/>
    </section>

</template>

<script>
import navbar_monitoreo from '/src/components/agrocablebot/base.vue'
import mqtt_pagina from '/src/components/mqtt/mqtt_server.vue'

export default {

        components:{
            navbar_monitoreo,
            mqtt_pagina
        
    },
}
</script>
