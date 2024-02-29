<template>

    <div class="">
        <navbar_monitoreo />
    </div>

    <div class="">
        <trasmisionVue />
    </div>

    <div>
        <CultivoVue />
    </div>
    
    <div>
        <Calendar_resum />
    </div>


    <section>
        <footer_imacuna />
    </section>

</template>

<script>
import navbar_monitoreo from '/src/components/agrocablebot/base.vue'
import trasmisionVue from '/src/components/agrocablebot/trasmision.vue'
import CultivoVue from '/src/components/agrocablebot/monitoreo/cultivo.vue'
import Calendar_resum from '/src/components/agrocablebot/monitoreo/calendarResum.vue'
import footer_imacuna from '/src/components/footer.vue'



export default{
    components:{
        navbar_monitoreo,
        trasmisionVue,
        CultivoVue,
        Calendar_resum,
        footer_imacuna,
    },
    
}
</script>