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

    



    
</template>

<script>
import navbar_monitoreo from '/src/components/agrocablebot/base.vue'
export default{
    components:{
        navbar_monitoreo,
    }
}
</script>