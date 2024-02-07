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
                            </div>
                        </div>
                    </div>
                    <div class="col" style="">
                        <div class="card"><img class="card-img-top w-100 d-block fit-cover" style="" :src="videoStreamUrl2"  />
                            <div class="card-body p-4">
                                <p class="card-text">Cámara Efector final</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
                       
        </div>

    </div>
</template>


<script>
// import axios from 'axios';

export default {

    name:"trasmisionVue", 

    data(){
        return {
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
        }


    }
}
</script>