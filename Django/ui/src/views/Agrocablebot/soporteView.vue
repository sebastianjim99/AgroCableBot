<template>
    
    <div class="">
        <navbar_monitoreo />
    </div>

    <div class="">
        <footer_imacuna />
    </div>




</template>


<script>
import navbar_monitoreo from '/src/components/agrocablebot/base.vue'
import footer_imacuna from '/src/components/footer.vue'

export default{
    components:{
        navbar_monitoreo,
        footer_imacuna
       
    }
}
</script>