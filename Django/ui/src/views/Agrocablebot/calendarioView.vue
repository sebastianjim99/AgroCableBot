<template>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" >
    
    <div class="">
        <navbar_monitoreo />
    </div>
      <!--   titulo control manual   -->
    <section>
        <listaTareasProgramadas/>
    </section>

    <section>
        <footer_imacuna />
    </section>



</template>


<script>
import navbar_monitoreo from '/src/components/agrocablebot/base.vue'
import footer_imacuna from '/src/components/footer.vue'
import listaTareasProgramadas from '/src/components/agrocablebot/calendario/listaTareasProgramadas.vue'


export default{
    components:{
        navbar_monitoreo,
        footer_imacuna,
        listaTareasProgramadas,

       
    }
}
</script>