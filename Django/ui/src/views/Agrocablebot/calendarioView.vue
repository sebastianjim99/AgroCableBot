<template>
    
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
// import vistaCalendario from '/src/components/agrocablebot/calendario/vistaCalendario.vue'
import listaTareasProgramadas from '/src/components/agrocablebot/calendario/listaTareasProgramadas.vue'
// import ejecucionTareas from '/src/components/agrocablebot/calendario/ejecucionTareas.vue'

export default{
    components:{
        navbar_monitoreo,
        footer_imacuna,
        // vistaCalendario,
        listaTareasProgramadas,
        // ejecucionTareas,
       
    }
}
</script>