<template>  

    <div class="container py-4">
        <div class="row">
            <div class="col-12 text-center">
                <h2 class="divider-style">
                    <span class="title-with-icon"> 
                        Control de motores
                        <svg @click="abrirModal" style="cursor: pointer;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-question-circle mx-2" viewBox="0 0 16 16">
                            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                            <path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286m1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94"/>
                        </svg>
                        <button class="btn btn-primary ms-2" @click="createConnection">Conectarse</button>
                    </span>
                </h2>
            </div>
        </div>

        <div class="row text-center mt-4 g-3">
            <div class="col-md-6">
                <p class="text-motor d-flex align-items-center">
                    <svg @click="Soltar_motorA" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-left-fill d-inline" style="vertical-align: middle;" viewBox="0 0 16 16">
                        <path d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z"/>
                    </svg>
                    <span class="d-inline" style="vertical-align: middle;">Motor A</span>
                    <svg @click="Recoger_motorA" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-right-fill d-inline" style="vertical-align: middle;" viewBox="0 0 16 16">
                        <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
                    </svg>
                    <input type="number" class="form-control d-inline" style="width: 200px" id="numeroInput" placeholder="Ingrese un número (10)" v-model="pasos_motorA">
                </p>
            </div>
            <div class="col-md-6">
                <p class="text-motor d-flex align-items-center">
                    <svg @click="Soltar_motorB" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-left-fill d-inline" style="vertical-align: middle;" viewBox="0 0 16 16">
                        <path d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z"/>
                    </svg>
                    <span class="d-inline" style="vertical-align: middle;">Motor B</span>
                    <svg @click="Recoger_motorB" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-right-fill d-inline" style="vertical-align: middle;" viewBox="0 0 16 16">
                        <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
                    </svg>
                    <input type="number" class="form-control d-inline" style="width: 200px" id="numeroInput" placeholder="Ingrese un número (10)" v-model="pasos_motorB">
                </p>
            </div>
            <div class="col-md-6">
                <p class="text-motor d-flex align-items-center">
                    <svg @click="Soltar_motorC" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-left-fill d-inline" style="vertical-align: middle;" viewBox="0 0 16 16">
                        <path d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z"/>
                    </svg>
                    <span class="d-inline" style="vertical-align: middle;">Motor C</span>
                    <svg @click="Recoger_motorC" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-right-fill d-inline" style="vertical-align: middle;" viewBox="0 0 16 16">
                        <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
                    </svg>
                    <input type="number" class="form-control d-inline" style="width: 200px" id="numeroInput" placeholder="Ingrese un número (10)" v-model="pasos_motorC">
                </p>
            </div>
            <div class="col-md-6">
                <p class="text-motor d-flex align-items-center">
                    <svg @click="Soltar_motorD" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-left-fill d-inline" style="vertical-align: middle;" viewBox="0 0 16 16">
                        <path d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z"/>
                    </svg>
                    <span class="d-inline" style="vertical-align: middle;">Motor D</span>
                    <svg @click="Recoger_motorD" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-right-fill d-inline" style="vertical-align: middle;" viewBox="0 0 16 16">
                        <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
                    </svg>
                    <input type="number" class="form-control d-inline" style="width: 200px" id="numeroInput" placeholder="Ingrese un número (10)" v-model="pasos_motorD">
                </p>
            </div>
        </div>
    </div>

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
import mqtt from 'mqtt';
import Swal from 'sweetalert2';

export default {

    data(){
        return{
            pasos_motorA: 10,
            pasos_motorB: 10,
            pasos_motorC: 10,
            pasos_motorD: 10,

            connection: {
                protocol: "wss",
                host: 'imacunamqtt.live' ,           
                // ws: 8083; wss: 8084
                port: 8084,
                endpoint: "/mqtt",
                clean: true,
                connectTimeout: 30 * 1000, // ms
                reconnectPeriod: 4000, // ms
                clientId: "emqx_vue_" + Math.random().toString(16).substring(2, 8),
                username: "imacuna",
                password: "pi",
            },
            
            mostrarModal: false,
        }
    },

    methods: {
        
        createConnection() {
            try {
                this.connecting = true;
                const { protocol, host, port, endpoint, ...options } = this.connection;
                const connectUrl = `${protocol}://${host}:${port}${endpoint}`;
                this.client = mqtt.connect(connectUrl, options);
                if (this.client.on) {
                    this.client.on("connect", () => {
                        this.connecting = false;
                        console.log("Connection succeeded!");
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
                }
            } catch (error) {
                this.connecting = false;
                console.log("mqtt.connect error", error);
            }
        },

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

        Recoger_motorA(){
            const mensaje = `{ "GCODE": "G10 A${this.pasos_motorA}"} `;
            this.client.publish("comandos", mensaje, "0" , error => {
                console.log(mensaje)
                if (error) {
                    console.log('Publish error', error)
                }
            })
        },
        Soltar_motorA(){
            const mensaje = `{ "GCODE": "G10 A-${this.pasos_motorA}"} `;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
        },
        Recoger_motorB(){
            const mensaje = `{ "GCODE": "G10 B${this.pasos_motorB}"} `;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
        },
        Soltar_motorB(){
            const mensaje = `{ "GCODE": "G10 B-${this.pasos_motorB}"} `;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
        },
        Recoger_motorC(){
            const mensaje = `{ "GCODE": "G10 C${this.pasos_motorC}"} `;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
        },
        Soltar_motorC(){
            const mensaje = `{ "GCODE": "G10 C-${this.pasos_motorC}"} `;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
        },
        Recoger_motorD(){
            const mensaje = `{ "GCODE": "G10 D${this.pasos_motorD}"} `;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
        },
        Soltar_motorD(){
            const mensaje = `{ "GCODE": "G10 D-${this.pasos_motorD}"} `;
            this.client.publish("comandos", mensaje, "0" , error => {
                if (error) {
                    console.log('Publish error', error)
                }
            })
        },

        abrirModal() {       
            this.mostrarModal = true;   // Mostrar el modal
        },
        cerrarModal() {       
            this.mostrarModal = false;   // Mostrar el modal
        },

    }

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
    .content-motor{
        justify-content: center;
    }
    .text-motor{
        width: 100%;
        justify-content: center ;
        align-content: center;
        font-size: 22px;
    }
</style>