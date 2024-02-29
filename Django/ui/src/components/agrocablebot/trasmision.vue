<template>
    <!-- Seccion de Trasmision en vivo camas -->
    <div class="live-stream-section" style="background: rgba(230, 230, 230, 0.47)">
        <div class="container py-4 py-xl-5">
            <div class="text-center mb-5">
                <h1 class="text-danger mb-3" style="font-family: Questrial; font-weight: 400; font-size: 70px;">Transmisión en vivo</h1>
                <h2 class="text-primary mb-5" style="font-family: Roboto; font-weight: 300; font-size: 50px;">AgroCableBot</h2>
            </div>
            <div class="row gy-4" >
                <div class=" col h-100 d-flex justify-content-center align-items-center"  >
                    <div class="card ">
                        <img class="card-img-top" :src="videoStreamUrl" alt="Cámara Posicion">
                        <div class="card-body text-center">
                            <p class="card-text">Cámara Posicion</p>
                            <a href="#" class="btn btn-primary" @click="capturar()">Capturar</a>
                        </div>
                    </div>
                </div>
                <div class="col h-100 d-flex justify-content-center align-items-center ">
                    <div class="card ">
                        <img class="card-img-top" :src="videoStreamUrl2" alt="Cámara Efector final">
                        <div class="card-body text-center">
                            <p class="card-text">Cámara Efector final</p>
                            <a href="#" class="btn btn-primary" @click="capturar2()">Capturar</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
 import axios from 'axios';

export default {

    name:"trasmisionVue", 

    data(){
        return {
            'api' : `${process.env.VUE_APP_API_URL}`,
            videoStreamUrl: (this.api + '/aboveCam/' ),
            videoStreamUrl2: (this.api + '/aboveCam2/'),
        };
    },
    mounted(){
    console.log('DOM rendered')

        setInterval(() => {
        this.updateStreamUrl();
        }, 1000);
    
    },

    methods: {
        updateStreamUrl() {
        // Agregar un timestamp a la URL para evitar el almacenamiento en caché
        this.videoStreamUrl = (this.api + '/aboveCam/' ) ;
        this.videoStreamUrl2 =(this.api + '/aboveCam2/') ;
        },

        capturar(){
            axios.get(this.api + '/captura/?camara=/aboveCam/')
            .then(Response => {
            // Manejar la respuesta si es necesario
            console.log('Solicitud exitosa:', Response);
            })
            .catch(error => {
            // Manejar el error si ocurre
            console.error('Error al ejecutar la URL:', error);
            });

        },
        capturar2(){
            axios.get(this.api +  '/captura/?camara=/aboveCam2/')
            .then(Response => {
            // Manejar la respuesta si es necesario
            console.log('Solicitud exitosa:', Response);
            })
            .catch(error => {
            // Manejar el error si ocurre
            console.error('Error al ejecutar la URL:', error);
            });

        },
    }
}
</script>

<style>
    .live-stream-section {
    width: 100%;
    height: 100%;
    position: relative;
    }

    .live-stream-section .container {
        position: relative;
    }

    .live-stream-section .card {
        border: none;
        border-radius: 10px;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    }

    .live-stream-section .card-img-top {
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
    }

    .live-stream-section .card-body {
        padding: 1.5rem;
        
    }

    .live-stream-section .btn {
        width: 100%;
        max-width: 200px;
    }

    @media (min-width: 768px) {
        .live-stream-section .card {
            transition: transform 0.3s ease-in-out;
        }

        .live-stream-section .card:hover {
            transform: translateY(-10px);
        }
    }
</style>