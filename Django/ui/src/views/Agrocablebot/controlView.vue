<template>

    <div class="">
        <navbar_monitoreo />
    </div>

    <div>   <!--   titulo control manual  y boton para sacar la informacion del control -->
        <section>
            <div style="text-align: center;">
                <h2 class="divider-style">
                    <span>
                        Control Manual     
                        <svg  @click = "abrirModal"  style="cursor: pointer;"   xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-question-circle" viewBox="0 0 16 16">
                            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                            <path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286m1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94"/>
                        </svg>            
                    </span>
                </h2>
                <p style="font-size: 25px;"> x: {{this.posActualX}}, y:{{this.posActualY}}    </p> 
            </div>
        </section>
    </div>

    <section>
        <nav class="navbar navbar-expand-md bg-body py-3">
            <div class="container">
                    <div class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navcol-5" >
                        <!-- Yoystik  para el control del robot -->
                        <div class="container">
                            <div class="row ">
                                <div class="col-md-10 icon-link " >
                                    <svg class="bi bi-arrow-left-circle" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 40px;margin: 5px;">
                                        <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-4.5-.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5z"></path>
                                    </svg>      
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-4 icon-link">
                                    <svg class="bi bi-arrow-up-circle" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 40px;padding: 0%;">
                                        <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-7.5 3.5a.5.5 0 0 1-1 0V5.707L5.354 7.854a.5.5 0 1 1-.708-.708l3-3a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 5.707z"></path>
                                    </svg>
                                </div>
                                <div class="col-md-2 icon-link">
                                    <svg class="bi bi-circle" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 40px;margin: 5px;">
                                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"></path>
                                    </svg>
                                </div>
                                <div class="col-md-2 icon-link ">
                                    <svg class="bi bi-arrow-down-circle" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 40px;padding: 0%;;margin-top: 5px;margin-bottom: 5px;">
                                        <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0M8.5 4.5a.5.5 0 0 0-1 0v5.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293z"></path>
                                    </svg>    
                                </div>
                            </div>
                            
                            <div class="row">
                                <div class="col-md-3 icon-link " style="padding: 0px 0px;">
                                    <svg class="bi bi-arrow-right-circle" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 40px;margin: 5px;">
                                        <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0M4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5z"></path>
                                    </svg>
                                </div>
                            </div>                   
                        </div>
                    </div>
                <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navcol-5">
                    <svg class="bi bi-justify" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 50px;padding: 0%;margin-left: 40%;margin-top: 5px;margin-bottom: 5px;">
                    <path fill-rule="evenodd" d="M2 12.5a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5m0-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5m0-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5m0-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5"></path>
                    </svg>
                </button>
                
                <div id="navcol-3" class="collapse navbar-collapse">
                    <div>
                        <div class="row" style="width: 300px;"  >
                            <div class="col-md-9 " @click="Y_positivo" >
                                <svg class="bi bi-arrow-up-circle icono" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 50px;padding: 0%;margin-left: 0%;margin-top: 10px;margin-bottom: 5px;">
                                    <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-7.5 3.5a.5.5 0 0 1-1 0V5.707L5.354 7.854a.5.5 0 1 1-.708-.708l3-3a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 5.707z"></path>
                                </svg>
                            </div>
                            <div class="col-md-3 " @click="movZ_up">
                                <svg class="bi bi-arrow-up-circle icono" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 50px;padding: 0%;margin-left: 0%;margin-top: 10px;margin-bottom: 5px;">
                                    <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-7.5 3.5a.5.5 0 0 1-1 0V5.707L5.354 7.854a.5.5 0 1 1-.708-.708l3-3a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 5.707z"></path>
                                </svg>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-3 " @click="X_negativo" >
                                <svg class="bi bi-arrow-left-circle icono" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 50px;margin: 3px;">
                                    <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-4.5-.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5z"></path>
                                </svg>
                            </div>
                            <div class="col-md-3 " @click="home" >
                                    <svg class="bi bi-house-door icono " xmlns="http://www.w3.org/2000/svg" width="1em" height="1em"  fill="currentColor" viewBox="0 0 16 16" style="font-size: 50px;margin: 3px;">
                                        <path d="M8.354 1.146a.5.5 0 0 0-.708 0l-6 6A.5.5 0 0 0 1.5 7.5v7a.5.5 0 0 0 .5.5h4.5a.5.5 0 0 0 .5-.5v-4h2v4a.5.5 0 0 0 .5.5H14a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.146-.354L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293zM2.5 14V7.707l5.5-5.5 5.5 5.5V14H10v-4a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5v4z"/>
                                    </svg>
                            </div>
                            <div class="col-md-3 " @click="X_positivo" >
                                <svg class="bi bi-arrow-right-circle icono" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 50px;margin: 3px;">
                                    <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0M4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5z"></path>
                                </svg>
                            </div>
                            <div class="col-md-3">
                                <p class="justify-content-center align-items-center" style="font-size: 30px; margin:7px 0 0 0; " > {{this.posActualZ}} </p>
                            </div>
                        </div>
                        <div class="row" style="width: 300px;"  >
                            <div class="col-md-9 " @click="Y_negativo" >
                                <svg class="bi bi-arrow-down-circle icono" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 50px; padding: 0%; margin-left: 0%; margin-top: 5px;margin-bottom: 5px;">
                                    <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0M8.5 4.5a.5.5 0 0 0-1 0v5.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293z"></path>
                                </svg>
                            </div>

                            <div class="col-md-3 " @click="movZ_Down"  >
                                <svg class="bi bi-arrow-down-circle icono" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 50px; padding: 0%; margin-left: 0%; margin-top: 5px;margin-bottom: 5px;">
                                    <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0M8.5 4.5a.5.5 0 0 0-1 0v5.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293z"></path>
                                </svg>
                            </div>
                        </div>
                    </div>

                    <ul class="navbar-nav mx-auto">
                        <li class="">
                            <p class="nav-link" style="margin-top: 11px;">Plantar</p> </li>
                        <li class="nav-item">
                            <a class="nav-link active" @click="movZ_Down">
                                <svg class="bi bi-play-circle icono" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 50px;">
                                    <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"></path>
                                    <path d="M6.271 5.055a.5.5 0 0 1 .52.038l3.5 2.5a.5.5 0 0 1 0 .814l-3.5 2.5A.5.5 0 0 1 6 10.5v-5a.5.5 0 0 1 .271-.445"></path>
                                </svg>
                            </a>
                        </li>
                        <li class="nav-item">
                            <p class="nav-link active" style="margin-top: 11px;">Rutina1</p>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" >
                                <svg class="bi bi-play-circle icono" @click="Rutina1" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 50px;">
                                    <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"></path>
                                    <path d="M6.271 5.055a.5.5 0 0 1 .52.038l3.5 2.5a.5.5 0 0 1 0 .814l-3.5 2.5A.5.5 0 0 1 6 10.5v-5a.5.5 0 0 1 .271-.445"></path>
                                </svg></a></li>
                        <li class="nav-item">
                            <p class="nav-link active"  style="margin-top: 11px;">Rutina 2</p>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" >
                                <svg class="bi bi-play-circle icono" @click="Rutina2" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 50px;">
                                    <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"></path>
                                    <path d="M6.271 5.055a.5.5 0 0 1 .52.038l3.5 2.5a.5.5 0 0 1 0 .814l-3.5 2.5A.5.5 0 0 1 6 10.5v-5a.5.5 0 0 1 .271-.445"></path>
                                </svg>
                            </a>
                        </li>
                        <li class="nav-item">
                            <p class="nav-link active"  style="margin-top: 11px;">Censar</p>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" @click="doPublish"  href="#">
                                <svg class="bi bi-play-circle icono" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 50px;">
                                    <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"></path>
                                    <path d="M6.271 5.055a.5.5 0 0 1 .52.038l3.5 2.5a.5.5 0 0 1 0 .814l-3.5 2.5A.5.5 0 0 1 6 10.5v-5a.5.5 0 0 1 .271-.445"></path>
                                </svg>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </section> 


    <!-- Trasmisión Video Stream-->
    <div>
        <trasmisionVue />
    </div>

    <!-- sensores -->
    <section>
        <div class="row">
            <div class="col">
                <div class="container">
                    <div class="row">
                        <div class="col-xxl-4" style="flex: 0 0 auto !important; width: 469px !important;">
                            <div style="text-align: center;">
                                <h2 class="divider-style"><span>Sensores</span></h2>
                            </div>
                            
                            <ul class="list-group">
                                <li class="list-group-item" style="background: var(--bs-body-bg);"><span>Planta # {{ this.posicionPlanta }}</span></li>
                                <li class="list-group-item" style="" > <span style="justify-content: start;" >Coordenada (x,y): ({{ this.coordenadaX }},{{ this.coordenadaY }}) </span> <button @click="move" class="btn btn-primary" style="justify-content: end;"> Mover </button> </li>
                                <li class="list-group-item"><span>Humedad: 50%</span></li>
                                <li class="list-group-item"><span>Temperatura: 25°C</span></li>
                                <li class="list-group-item"><span>Otro dato</span></li>
                            </ul>
                            <div style="text-align: center;">
                                <h2 class="divider-style"><span>Ambiente</span></h2>
                            </div>
                            <ul class="list-group">
                                <li class="list-group-item" style="background: var(--bs-body-bg);"><span>Humedad: {{this.humedad}}%</span></li>
                                <li class="list-group-item" style="background: var(--bs-body-bg);"><span>Temperatura: {{this.temperatura}}°C</span></li>
                                <li class="list-group-item" style="background: var(--bs-body-bg);"><span>Presión: {{this.presion}}</span></li>
                            </ul>
                            <div style="text-align: center;">
                                <h2 class="divider-style"><span>Giroscopio efector</span></h2>
                            </div>
                            <ul class="list-group">
                                <li class="list-group-item" style="background: var(--bs-body-bg);"><span>roll: {{this.giroscopio_pitch}}°</span></li>
                                <li class="list-group-item" style="background: var(--bs-body-bg);"><span>Pitch: {{this.giroscopio_roll}}°</span></li>
                                <li class="list-group-item" style="background: var(--bs-body-bg);"><span>yaw: {{this.giroscopio_yaw}}°</span></li>
                            </ul>
                        </div>
                        <div class="col-12 col-xl-6">
                            <h1 class="text-center mb-4">Distribución del cultivo</h1>
                            <table class="table">
                                <tbody>
                                    <tr v-for="(fila, filaIndex) in matriz" :key="filaIndex">
                                        <td v-for="(planta, columnaIndex) in fila" :key="columnaIndex" class="position-relative" @click="seleccionarPlanta(filaIndex, columnaIndex)"  :style="{ backgroundColor: plantaSeleccionada && filaIndex === plantaSeleccionada.fila && columnaIndex === plantaSeleccionada.columna ? 'rgb(178,218,250, 0.5)' : '' }">
                                            <div class="text-center">
                                                <p v-if="planta">{{ planta.nombre }}</p>
                                                <img v-if="planta" :src="planta.cultivo.iconosPlantas" alt="Imagen de planta" width="40" height="40">
                                                <p v-else>{{ obtenerContadorPosicion(filaIndex, columnaIndex) }}
                                                <img src="@/assets/iconos/sin_imagen.png" alt="Sin imagen de planta" width="40" height="40"></p>
                                            </div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <div>
        <listCultivo />
    </div>
    

    <section>
        <footer_imacuna />
    </section>

    <div v-if="mostrarModal" class="modal-ayuda" >
        <div class="modal-dialog-ayuda">
            <div class="modal-content-ayuda" >
                <span class="close" style="font-size: 24px;cursor: pointer; position: absolute; top: 10px; right: 10px;" data-dismiss="modal-ayuda" aria-label="Close" @click="cerrarModal">&times;</span>
                <img class="img-fluid" style="  width: 700px ; height: 200px ;" src="@/assets/logos/Uso_AgroCableBot.png" alt="Uso adecuado de los motores del robot Agrocablebot">
            </div>
        </div>
    </div>

</template>



<script>
import axios from 'axios'
import navbar_monitoreo from '/src/components/agrocablebot/base.vue'
import trasmisionVue from '/src/components/agrocablebot/trasmision.vue'
import listCultivo from '/src/components/agrocablebot/monitoreo/ListCultivo.vue'
import footer_imacuna from '/src/components/footer.vue'
import mqtt from 'mqtt';
import Swal from 'sweetalert2';

export default{
    components:{
        navbar_monitoreo,
        trasmisionVue, 
        listCultivo,
        footer_imacuna,
    },

    data(){

        return{
            'api': `${process.env.VUE_APP_API_URL}`,
            tipo_cultivo:[],
            cultivos:[],
            plantas:[],
            matriz: [],
            Datos_sensores: [],
            plantaSeleccionada: null,
            cultivoSeleccionado:null, 
            posicionPlanta:null,
            coordenadaX:null,
            coordenadaY:null,
            
            // Servidor mqtt 
            posActualX: null,
            posActualY: null,
            posActualZ: null,

            connection: {
                protocol: "ws",
                host: '172.17.91.30' ,               //"imacunamqtt.live",
                // ws: 8083; wss: 8084
                port: 8083,
                endpoint: "/mqtt",
                clean: true,
                connectTimeout: 30 * 1000, // ms
                reconnectPeriod: 4000, // ms
                clientId: "emqx_vue_" + Math.random().toString(16).substring(2, 8),
                username: "imacuna",
                password: "pi",
            },
            subscription: {
                topic: "sensores/",
                qos: 0,
            },
            publish: {
                topic: "comandos",
                qos: 0,
                payload: '{ "interface": "send_aio" }',
            },
            receiveNews: "",
            qosList: [0, 1, 2],
            client: {
                connected: false,
            },
            subscribeSuccess: false,
            connecting: false,
            mostrarModal: false,
            retryTimes: 0,         
        }
    },

    mounted(){
        this.createConnection();
        this.obtenerDatosSensores();
        this.PosActual();
        
        //Lectura tipo de cultivo
        axios.get(this.api + '/api/tipoCultivo').then(response =>{
            this.tipo_cultivo=response.data    
        }).catch(
            error =>{
                console.log(error)
            })

        //Lectura de cultivo
        axios.get( this.api + '/api/cultivo').then(response =>{
            this.cultivos=response.data
        }).catch(error =>{
            console.log(error)
        })
        
        //Lectura de plantas
        axios.get( this.api + '/api/plantas').then(response =>{
            this.plantas=response.data
            this.initializeMatriz()
        }).catch(error =>{
            console.log(error)
        })
      
    },

    methods: {
        // Función para inicializar la matriz con los datos de las plantas
        initializeMatriz() {
            for (let i = 0; i < 9; i++) {
            this.matriz.push(new Array(9).fill(null));
            }

            // Asignar las plantas a la matriz según el número de planta asignado
            this.plantas.forEach(planta => {
            const fila = Math.floor((planta.numeroPlanta - 1) / 9);
            const columna = (planta.numeroPlanta - 1) % 9;
            this.matriz[fila][columna] = planta;  
            }); 
        },
        
        obtenerContadorPosicion(filaIndex, columnaIndex) {
            // Calcula el contador de posición basado en los índices de fila y columna
            return filaIndex * this.matriz[0].length + columnaIndex + 1;
        },
        // Seleccion de la planta mediante click y despliegue de informacion
        seleccionarPlanta(filaIndex, columnaIndex) {
            this.plantaSeleccionada = { fila: filaIndex, columna: columnaIndex };
            //console.log("Planta seleccionada", this.plantaSeleccionada)
            const planta = this.matriz[filaIndex][columnaIndex];
            this.cultivoSeleccionado = planta ? planta.cultivo : null;
            this.posicionPlanta =filaIndex * this.matriz[0].length + columnaIndex + 1;
            this.coordenadaX= parseInt(planta.coordenadaX) ;
            this.coordenadaY= parseInt(planta.coordenadaY);
        },
        //  ---------- metodos de sensores----------------
        obtenerDatosSensores() {
            axios.get(this.api + '/api/Sensor_MQTT/')
            .then(response => {
                this.Datos_sensores=response.data
                this.obtenerUltimaActualizacion();
                // console.log(this.Datos_sensores)
            })
            .catch(error => {
                console.error('Error al obtener los datos de los sensores:', error);
            });
        },
        obtenerUltimaActualizacion() {
            // Ordenar los datos por timestamp de forma descendente para obtener la última actualización primero
            const ultimaActualizacion = this.Datos_sensores.sort((a, b) => b.id - a.id)[0];
            
            // Actualizar las variables de la interfaz de usuario con los datos de la última actualización
            this.acelerometro_roll = ultimaActualizacion.acelerometro_roll;
            this.acelerometro_pitch = ultimaActualizacion.acelerometro_pitch;
            this.acelerometro_yaw = ultimaActualizacion.acelerometro_yaw;
            
            this.giroscopio_pitch = ultimaActualizacion.giroscopio_pitch;
            this.giroscopio_roll = ultimaActualizacion.giroscopio_roll;
            this.giroscopio_yaw = ultimaActualizacion.giroscopio_yaw;

            this.humedad = ultimaActualizacion.humedad;
            this.presion = ultimaActualizacion.presion;
            this.temperatura = ultimaActualizacion.temperatura;

        },

        // METODOS PARA CONEXIÓN, RECONEXIÓN, PUBLICACION
        handleOnReConnect() {
            this.retryTimes += 1;
            if (this.retryTimes > 5) {
                try {
                    this.client.end();
                    this.initData();
                    this.$message.error("Limite de reconexiones");
                } catch (error) {
                    this.$message.error(error.toString());
                }
            }
        },

        createConnection() {
            try {
                this.connecting = true;
                const { protocol, host, port, endpoint, ...options } = this.connection;
                const connectUrl = `${protocol}://${host}:${port}${endpoint}`;
                this.client = mqtt.connect(connectUrl, options);
                if (this.client.on) {
                this.client.on("connect", () => {
                    this.connecting = false;
                    Swal.fire({
                        icon: 'success',
                        title: '¡Éxito!',
                        text:  'Conexión exitosa con el servidor mqtt',
                    });
                });
                this.client.on("reconnect", this.handleOnReConnect);
                this.client.on("error", (error) => {
                    console.log("Connection failed", error);
                });
                this.client.on("message", (topic, message) => {
                    this.receiveNews = this.receiveNews.concat(message);
                    console.log(`Received message ${message} from topic ${topic}`);
                });
                }
            } catch (error) {
                this.connecting = false;
                console.log("mqtt.connect error", error);
            }
        },

        doPublish() {
            const { topic, qos, payload } = this.publish
            this.client.publish(topic, payload, { qos }, error => {
            if (error) {
                console.log('Publish error', error)
            }
            })
        },

        PosActual(){
            this.client.subscribe("status", "0", (error) => {
                if (error) {
                    console.log('Subscribe to topics error', error)
                }
            })
            this.client.publish("comandos",'{ "GCODE": "M5" }', "0" , error => {
                if (error) {
                console.log('Publish error', error)
                }
            })

            this.client.on('message', (topic, message) => {
                // console.log(`Received message ${message.toString()} from topic ${topic}`);
                try {
                    // Analizar el mensaje JSON
                    const status_actual = JSON.parse(message.toString());
                    
                    // Verificar si el objeto tiene las propiedades de posición
                    if (status_actual && status_actual.x !== undefined && status_actual.y !== undefined && status_actual.z !== undefined) {
                        // Asignar las propiedades a las variables posActualX, posActualY y posActualZ
                        this.posActualX = status_actual.x;
                        this.posActualY = status_actual.y;
                        this.posActualZ = status_actual.z;
                        
                        // Aquí puedes hacer lo que necesites con las variables posActualX, posActualY y posActualZ
                        console.log('posActualX:', this.posActualX, 'posActualY:', this.posActualY, 'posActualZ:', this.posActualZ);
                    }
                } catch (error) {
                    console.error('Error al analizar el objeto JSON:', error);
                }
                // Vaciar la variable receiveNews
                this.receiveNews = "";
            });

        },

        movZ_up(){
            const nueva_posZ = this.posActualZ + 10; 
            const mensaje = `{ "GCODE": "G1 X${this.posActualX} Y${this.posActualY} Z${nueva_posZ}" }`;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
            this.posActualZ = nueva_posZ 
        },        
        
        movZ_Down(){
            const nueva_posZ = this.posActualZ - 10; 
            const mensaje = `{ "GCODE": "G1 X${this.posActualX} Y${this.posActualY} Z${nueva_posZ}" }`;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
            this.posActualZ = nueva_posZ 
        },

        X_positivo(){
            const nueva_posX = this.posActualX + 100; 
            const mensaje = `{ "GCODE": "G1 X${nueva_posX} Y${this.posActualY} Z${this.posActualZ}" }`;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
            this.posActualX = nueva_posX 
        },

        X_negativo(){
            const nueva_posX = this.posActualX - 100; 
            const mensaje = `{ "GCODE": "G1 X${nueva_posX} Y${this.posActualY} Z${this.posActualZ}" }`;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
            this.posActualX = nueva_posX 
        },

        Y_positivo(){
            const nueva_posY = this.posActualY + 100; 
            const mensaje = `{ "GCODE": "G1 X${this.posActualX} Y${nueva_posY} Z${this.posActualZ}" }`;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
            this.posActualY = nueva_posY
        },

        Y_negativo(){
            const nueva_posY = this.posActualY - 100; 
            const mensaje = `{ "GCODE": "G1 X${this.posActualX} Y${nueva_posY} Z${this.posActualZ}" }`;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
            this.posActualY = nueva_posY
        },   
        
        home(){
            const mensaje = `{ "GCODE": "G1 X0 Y0 Z${this.posActualZ}" }`;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
        },

        move(){
           const mensaje = `{ "GCODE": "G1 X${this.coordenadaX} Y${this.coordenadaY} Z${this.posActualZ}" }`;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
            this.posActualX =  this.coordenadaX;
            this.posActualY =  this.coordenadaY;
        },

        abrirModal() {       
            this.mostrarModal = true;   // Mostrar el modal
        },
        cerrarModal() {       
            this.mostrarModal = false;   // Mostrar el modal
        },

        Rutina1(){
            if (this.posActualX === 0 && this.posActualY === 0) {
                // Realizar la diagonal 
                this.coordenadaX = -100
                this.coordenadaX =  100
                const mensaje = `{ "GCODE": "G1 X${this.coordenadaX} Y${this.coordenadaY} Z${this.posActualZ}" }`;
                this.client.publish("comandos", mensaje, "0", error => {
                    if (error) {
                    console.log('Publish error', error)
                    }
                });
                const PosAnteriorX = this.coordenadaX
                const PosAnteriorY = this.coordenadaY
                      // Esperar un segundo
                setTimeout(() => {
                    this.PosActual();
                    if (this.posActualX === PosAnteriorX  && this.posActualY ===  PosAnteriorY ){
                        this.posActualX ==  "muy bien"
                    } 
                }, 1000); 



            } else{
                // Ejecutar Swal.fire si posActualX y posActualY no son iguales a 0
                Swal.fire({
                    icon: 'error',
                    title: '¡Error!',
                    text:  'Retorne la posición HOME del robot',
                });
            }
        },

        Rutina2(){

        }
    },
}

</script>


<style>
    .modal-ayuda {
        /* Contenedor principal del modal */
        display: block; /* Mostrar como bloque */
        position: fixed; /* Fijar la posición en relación con la ventana del navegador */
        z-index: 9999; /* Colocar sobre otros elementos */
        left: 0; /* Posición izquierda */
        top: 0; /* Posición superior */
        width: 100%; /* Ancho completo */
        height: 100%; /* Altura completa */
        overflow: auto; /* Agregar desplazamiento automático si es necesario */
        background-color: rgba(0, 0, 0, 0.4); /* Fondo oscuro semi-transparente */
    }

    .modal-dialog-ayuda{
        position: relative; /* Posición relativa para posicionar elementos secundarios */
        margin: auto; /* Centrar horizontalmente dentro del modal */
        padding: 20px; /* Espaciado interno */
        background-color: #fefefe; /* Color de fondo */
        border: 1px solid #888; /* Borde sólido */
        width: 90%; /* Ancho del 90% del contenedor padre */
        max-width: 800px; /* Ancho máximo */
        top: 90px;
    }

    .modal-content-ayuda {
        margin: auto; /* Centrar horizontalmente */
        top: 90px; 
        background-color: #fff; /* Fondo blanco */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); /* Sombra suave */
        max-width: 700px; /* Ancho máximo del contenido */
        margin: 0 auto; /* Centrar horizontalmente */
    }

    .icono:hover {
        fill: blue; /* Cambia el color de relleno al pasar el mouse sobre el icono */
    }

    .icono:active {
        fill: red; /* Cambia el color de relleno al hacer clic en el icono */
    }

    .divider-style:before {
    content: "";
    display: block;
    border-top: solid 1px black;
    width: 100%;
    height: 1px;
    position: absolute;
    top: 50%;
    z-index: 1;
    }

    .divider-style {
    margin-top: 0px;
    position: relative;
    margin-right: 40px;
    margin-left: 40px;
    }

    .divider-style span {
    background: #fff;
    padding: 0 20px;
    position: relative;
    z-index: 5;
    }

    @media (min-width:768px) {
    .col-md-12 {
    flex: 0 0 auto;
    width: 100%;
  }
}

.row > * {
  flex-shrink: 0;
  width: 100%;
  max-width: 100%;
  padding-right: calc(var(--bs-gutter-x) * .5);
  padding-left: calc(var(--bs-gutter-x) * .5);
  margin-top: var(--bs-gutter-y);
}

.navbar {
  --bs-navbar-padding-x: 0;
  --bs-navbar-padding-y: 0.5rem;
  --bs-navbar-color: rgba(var(--bs-emphasis-color-rgb), 0.65);
  --bs-navbar-hover-color: rgba(var(--bs-emphasis-color-rgb), 0.8);
  --bs-navbar-disabled-color: rgba(var(--bs-emphasis-color-rgb), 0.3);
  --bs-navbar-active-color: rgba(var(--bs-emphasis-color-rgb), 1);
  --bs-navbar-brand-padding-y: 0.3125rem;
  --bs-navbar-brand-margin-end: 1rem;
  --bs-navbar-brand-font-size: 1.25rem;
  --bs-navbar-brand-color: rgba(var(--bs-emphasis-color-rgb), 1);
  --bs-navbar-brand-hover-color: rgba(var(--bs-emphasis-color-rgb), 1);
  --bs-navbar-nav-link-padding-x: 0.5rem;
  --bs-navbar-toggler-padding-y: 0.25rem;
  --bs-navbar-toggler-padding-x: 0.75rem;
  --bs-navbar-toggler-font-size: 1.25rem;
  --bs-navbar-toggler-icon-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%2833, 37, 41, 0.75%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
  --bs-navbar-toggler-border-color: rgba(var(--bs-emphasis-color-rgb), 0.15);
  --bs-navbar-toggler-border-radius: var(--bs-border-radius);
  --bs-navbar-toggler-focus-width: 0.25rem;
  --bs-navbar-toggler-transition: box-shadow 0.15s ease-in-out;
  position: relative;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  padding: var(--bs-navbar-padding-y) var(--bs-navbar-padding-x);
}





    


</style>