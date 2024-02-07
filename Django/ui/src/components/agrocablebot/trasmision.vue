<template>
    <!-- Seccion de Trasmision en vivo camas -->
    <div style="width: 100%; height: 100%; position: relative; background: rgba(230, 230, 230, 0.47)">
        <div class="position-relative bg-success-subtle bg-opacity-50 row">
            <div style="width: 100%; height: 100%; text-align: center; color: #FB6542; font-size: 70px; font-family: Questrial; font-weight: 400; word-wrap: break-word">
                Transmisión en vivo
            </div>
            <div style="width: 100%; height: 100%; color: #375E97; font-size: 50px; font-family: Roboto; font-weight: 300; word-wrap: break-word">
                AgroCableBot
            </div>
            <div class="container py-4 py-xl-5">
                <div class="row gy-4 row-cols-1 row-cols-md-2" style="margin-top: -23px;">
                    <div class="col"  >
                        <div class="card"><img class="card-img-top w-100 d-block fit-cover" style="" :src="videoStreamUrl"  />
                            <div class="card-body p-4">
                                <p class="card-text">Cámara Posicion</p>
                                <a name="captura" id="" class="btn btn-primary" @click="capturar()" role="button"> Capturar </a>
                            </div>
                        </div>
                    </div>
                    <div class="col" style="">
                        <div class="card"><img class="card-img-top w-100 d-block fit-cover" style="" :src="videoStreamUrl2"  />
                            <div class="card-body p-8">
                                <p class="card-text">Cámara Efector final</p> 
                                <a name="captura" id="" class="btn btn-primary" @click="capturar2()" role="button"> Capturar </a> 
                            </div>
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
            'api' : 'http://localhost:8000/api',
            videoStreamUrl: 'http://localhost:8000/aboveCam/',
            videoStreamUrl2: 'http://localhost:8000/aboveCam2/'
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
        this.videoStreamUrl = 'http://localhost:8000/aboveCam/' ;
        this.videoStreamUrl2 = 'http://localhost:8000/aboveCam2/' ;
        },

        capturar(){
            axios.get('http://127.0.0.1:8000/captura/?camara=/aboveCam/')
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
            axios.get('http://127.0.0.1:8000/captura/?camara=/aboveCam2/')
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