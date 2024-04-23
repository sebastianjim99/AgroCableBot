<template>

<nav class="navbar navbar-expand-md bg-body py-3">
    <div class="container">
        <a class="navbar-brand d-flex align-items-center" >
            <h1>AgroCableBot</h1>

        </a>
        <img class="img-fluid" src="@/assets/iconos/cultivar.png" width="50" height="36" loading="auto" style="margin-left: 10px;" />
        <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navcol-3">
            <span class="visually-hidden">Toggle navigation</span>
            <span class="navbar-toggler-icon"> </span>
        </button>

                <div id="navcol-3" class="collapse navbar-collapse">
                <ul class="navbar-nav mx-auto">
                <li class="nav-item"><a class="nav-link active" href="/monitoreo">Monitoreo</a></li>
                <li class="nav-item"><a class="nav-link" href="/control">Control</a></li>
                <li class="nav-item"><a class="nav-link" href="/Calendario">Calendario</a></li>
                <li class="nav-item"><a class="nav-link" href="/Estadisticas">Estadísticas</a></li>
                <li class="nav-item"><a class="nav-link" href="/soporte"> Soporte </a></li>
                <li class="nav-item"><a class="nav-link" href="/Mqtt">Mqtt</a></li>
                <li class="nav-item"><a class="nav-link" :href="this.api + '/admin/' " >Admin</a></li>
            </ul>
            <button @click="logout" type="submit" class="btn btn-primary" >Cerrar Sesión</button>
        </div>
        
    </div>
</nav>


</template>

<script>
export default{

  name: "navbar_monitoreo",
  data(){
        return{
            'api' : `${process.env.VUE_APP_API_URL}`,
        }
    },

    mounted(){
        console.log(this.username, this.password);
    },

    methods: {

        // obtenerListaDeCultivos() {
        //     axios.get(this.api + '/api/tipoCultivo').then(response => {
        //         this.listaDeCultivos = response.data;
        //     }).catch(error => {
        //         console.error('Error al obtener la lista de cultivos:', error);
        //     });
        // },

        logout(){
            this.$store.commit('removeToken');
            this.$router.push('/')
        },

    },
}

</script>


